import os
import dash
from flask import request, make_response
from flask_cors import CORS

from config import Config


class CustomDash(dash.Dash):

    def interpolate_index(self, **kwargs):
        # scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'https://unpkg.zhimg.com/')
        scripts = kwargs.pop('scripts').replace('https://unpkg.com/', 'http://npm.elemecdn.com/')
        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)

    # def interpolate_index(self, **kwargs):
    #     return '''
    #     <!DOCTYPE html>
    #     <html>
    #         <head>
    #             {metas}
    #             <title>{title}</title>
    #             {favicon}
    #             {css}
    #         </head>
    #         <body>
    #             {app_entry}
    #             <footer>
    #                 {config}
    #                 {scripts}
    #                 {renderer}
    #             </footer>
    #         </body>
    #     </html>
    #     '''.format(
    #         metas=kwargs['metas'],
    #         css=kwargs['css'],
    #         favicon=kwargs['favicon'],
    #         title=kwargs['title'],
    #         app_entry=kwargs['app_entry'],
    #         config=kwargs['config'],
    #         scripts=kwargs['scripts'].replace('https://unpkg.com/', 'https://unpkg.zhimg.com/'),
    #         renderer=kwargs['renderer'])


app = CustomDash(
    __name__,
    suppress_callback_exceptions=True,
    update_title=None,
    serve_locally=False,
    extra_hot_reload_paths=[
        './documents'
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
