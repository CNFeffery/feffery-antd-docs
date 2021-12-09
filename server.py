import os
import dash
from flask import request, make_response
from flask_cors import CORS

from config import Config

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    external_scripts=[
        'https://unpkg.zhimg.com/feffery_antd_components@0.0.1-rc7/feffery_antd_components/feffery_antd_components.min.js',
        'https://unpkg.zhimg.com/@babel/polyfill@7.12.1/dist/polyfill.min.js',
        'https://unpkg.zhimg.com/react@16.14.0/umd/react.production.min.js',
        'https://unpkg.zhimg.com/react-dom@16.14.0/umd/react-dom.production.min.js',
        'https://unpkg.zhimg.com/prop-types@15.7.2/prop-types.min.js',
        'https://unpkg.zhimg.com/feffery_utils_components@0.0.4/feffery_utils_components/feffery_utils_components.min.js',
        'https://unpkg.zhimg.com/dash-renderer@1.10.0/build/dash_renderer.min.js',
        'https://unpkg.zhimg.com/dash-core-components@2.0.0/dash_core_components/dash_core_components.js',
        'https://unpkg.zhimg.com/dash-core-components@2.0.0/dash_core_components/dash_core_components-shared.js',
        'https://unpkg.zhimg.com/dash-html-components@2.0.0/dash_html_components/dash_html_components.min.js',
        'https://unpkg.zhimg.com/dash-table@5.0.0/dash_table/bundle.js',
    ]
)

CORS(app.server, supports_credentials=False)

app.title = 'feffery-antd-components在线文档'

server = app.server

try:
    os.mkdir(Config.caches_path)
except FileExistsError:
    pass

# 限制最大传输内容大小为5MB
app.server.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


@app.server.before_request
def ban_external_upload_request():
    if 'upload' in request.path:
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return make_response('<h1>检测到外部上传请求！</h1>')


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
