import os
import re
import dash
from flask import request, abort

from config import Config


class CustomDash(dash.Dash):

    def interpolate_index(self, **kwargs):
        scripts = kwargs.pop('scripts')

        # 提取scripts部分符合条件的外部js资源
        external_scripts = re.findall(
            '(<script src="http.*?"></script>)',
            scripts
        )

        # 将原有的script标签内容替换为带备用地址错误切换的版本
        for external_script in external_scripts:
            # 排除fuc被onmicrosoft封禁的情况
            if 'markdown' not in external_script:
                scripts = scripts.replace(
                    external_script,
                    '''<script src="{}" onerror='this.remove(); let fallbackScript = document.createElement("script"); fallbackScript.src = "{}"; document.querySelector("head").prepend(fallbackScript);'></script>'''.format(
                        re.findall('"(.*?)"', external_script)[0]
                        .replace('https://unpkg.com/', 'https://npm.onmicrosoft.cn/'),
                        re.findall('"(.*?)"', external_script)[0]
                    )
                )

        scripts = '''<script>
window.onerror = async function(message, source, lineno, colno, error) {
    if (message.includes('is not defined') !== -1) {
        await waitForModules();
    }
}

async function waitForModules() {
    const requiredModules = [
        'DashRenderer',
        'dash_html_components',
        'dash_core_components',
        'feffery_antd_components',
        'feffery_utils_components',
        'feffery_markdown_components'
    ];

    while (!areModulesDefined(requiredModules)) {
        await delay(100); // 延迟100毫秒
    }

    // 变量已定义，触发事件
    var renderer = new DashRenderer();
}

function areModulesDefined(modules) {
    return modules.every(module => window[module]);
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
</script>
''' + scripts

        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)


app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=[
        './documents',
        './change_logs'
    ],
    compress=True
)

app.title = 'feffery-antd-components在线文档'

server = app.server

try:
    os.mkdir(Config.caches_path)
except FileExistsError:
    pass


@app.server.before_request
def ban_external_upload_request():
    if 'upload' in request.path and 'feffery' not in request.path:
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            abort(403)


# 这里的app即为Dash实例
@app.server.route('/upload/', methods=['POST'])
def upload():
    '''
    构建文件上传服务
    :return:
    '''

    # 获取上传id参数，用于指向保存路径
    uploadId = request.values.get('uploadId')

    # 获取上传的文件名称
    filename = request.files['file'].filename

    # 基于上传id，若本地不存在则会自动创建目录
    try:
        os.mkdir(os.path.join(Config.caches_path, uploadId))
    except FileExistsError:
        pass

    # # 流式写出文件到指定目录
    # with open(os.path.join(Config.caches_path, uploadId, filename), 'wb') as f:
    #     # 流式写出大型文件，这里的10代表10MB
    #     for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
    #         f.write(chunk)

    return {'filename': filename}
