import dash
from flask import request, abort

# 导入Dash Hooks
from dash_change_cdn_plugin import setup_change_cdn_plugin
from dash_console_filter_plugin import setup_console_filter_plugin

from config import AppConfig
from utils.api_descriptions import get_components_docs

# 启用相关Dash Hooks
setup_change_cdn_plugin()
setup_console_filter_plugin(keywords=['Warning:'])


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=['./changelogs', './public'],
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

    if 'upload' in request.path and request.method == 'POST':
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


@app.server.route('/get-docs')
def get_docs():
    """获取所声明组件参数文档的开放接口"""

    components = request.args.get('components')

    if components:
        # 解析本次请求的组件名称列表
        components = components.split(',')

        return get_components_docs(components)

    return '无效的请求，正确请求范例：/get-docs?components=AntdButton、/get-docs?components=AntdButton,AntdAlert、/get-docs?components=all'
