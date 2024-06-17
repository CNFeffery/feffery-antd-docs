import re
import dash
from flask import request, abort

from config import DeployConfig, AppConfig


class CustomDash(dash.Dash):
    """
    自定义Dash实例，用于改造默认的CDN访问行为
    """

    def interpolate_index(self, **kwargs):
        scripts = kwargs.pop('scripts')

        # 提取scripts部分符合条件的外部js资源
        external_scripts = re.findall(
            '(<script src="http.*?"></script>)', scripts
        )

        # 将原有的script标签内容替换为带备用地址错误切换的版本
        for external_script in external_scripts:
            # 提取当前资源地址
            origin_script_src = re.findall('"(.*?)"', external_script)[0]
            # 抽取关键信息
            library_name, library_version, library_file = re.findall(
                'com/(.+)@(.+?)/(.+?)$', origin_script_src
            )[0]
            # 基于阿里cdn构建新的资源地址
            new_library_src = f'https://registry.npmmirror.com/{library_name}/{library_version}/files/{library_file}'

            scripts = scripts.replace(
                external_script,
                """<script src="{}" onerror='this.remove(); let fallbackScript = document.createElement("script"); fallbackScript.src = "{}"; document.querySelector("head").prepend(fallbackScript);'></script>""".format(
                    re.findall('"(.*?)"', external_script)[0].replace(
                        origin_script_src,
                        new_library_src,
                    ),
                    re.findall('"(.*?)"', external_script)[0],
                ),
            )

        scripts = (
            """
<script>
const requiredModules = {};
{}
</script>
""".format(
                str(DeployConfig.cdn_modules),
                open(
                    './public/handleModulesLoadError.js', encoding='utf-8'
                ).read(),
            )
            + scripts
        )

        return super(CustomDash, self).interpolate_index(
            scripts=scripts, **kwargs
        )


app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=['./documents', './change_logs'],
    compress=True,
    meta_tags=[
        # 移动端显示优化
        {
            'name': 'viewport',
            'content': 'width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0',
        }
    ],
)

app.title = AppConfig.title

server = app.server


@app.server.before_request
def ban_external_upload_request():
    """拦截恶意请求"""

    if 'upload' in request.path and 'Antd' not in request.path:
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            abort(403)


# 这里的app即为Dash实例
@app.server.route('/upload/', methods=['POST'])
def upload():
    """文档示例用文件上传服务"""

    # 获取上传id参数，用于指向保存路径
    uploadId = request.values.get('uploadId')  # noqa: F841

    # 获取上传的文件名称
    filename = request.files['file'].filename

    return {'filename': filename}
