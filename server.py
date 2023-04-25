import os
import dash
from flask import request, abort

from config import Config


class CustomDash(dash.Dash):

    def interpolate_index(self, **kwargs):
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'https://unpkg.zhimg.com/')
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'http://npm.elemecdn.com/')
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'https://fastly.jsdelivr.net/npm/')

        scripts = kwargs.pop('scripts')

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
    compress=True,
    assets_ignore='dark.css'
)

app.title = 'feffery-antd-components在线文档'

server = app.server

try:
    os.mkdir(Config.caches_path)
except FileExistsError:
    pass


@app.server.before_request
def ban_external_upload_request():
    if 'upload' in request.path:
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
