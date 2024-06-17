import feffery_antd_components as fac
import feffery_markdown_components as fmc


def render(tip_type: str):
    """渲染一些特殊的小贴士信息"""

    if tip_type == 'upload api demo':
        return fac.AntdCollapse(
            fac.AntdTabs(
                items=[
                    {
                        'label': 'Flask',
                        'key': 'Flask',
                        'children': fmc.FefferySyntaxHighlighter(
                            codeString="""
import os
from flask import request

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
        os.mkdir(os.path.join('自定义缓存根目录', uploadId))
    except FileExistsError:
        pass

    # 流式写出文件到指定目录
    with open(os.path.join('自定义缓存根目录', uploadId, filename), 'wb') as f:
        # 流式写出大型文件，这里的10代表10MB
        for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
            f.write(chunk)

    return {'filename': filename}
""",
                            language='python',
                            codeTheme='dracula',
                            codeBlockStyle={'overflowX': 'auto'},
                        ),
                    },
                    {
                        'label': 'FastAPI',
                        'key': 'FastAPI',
                        'children': fmc.FefferySyntaxHighlighter(
                            codeString="""
import os
import uvicorn
from tqdm import tqdm
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# 定义缓存根目录
config = {
    'cache_root_path': './caches'
}

app = FastAPI()

# 设置允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/upload/')
def upload_file(uploadId: str, file: UploadFile = File(...)):
    # 基于上传id，若本地不存在则会自动创建目录
    try:
        os.mkdir(os.path.join(config.get("cache_root_path"), uploadId))
    except FileExistsError:
        pass

    with open(os.path.join(config.get("cache_root_path"), uploadId, file.filename), 'wb') as f:
        # 流式写出大型文件，这里的10代表10MB
        for chunk in tqdm(iter(lambda: file.file.read(1024 * 1024 * 10), b'')):
            f.write(chunk)

    return {"filename": file.filename}
""",
                            language='python',
                            codeTheme='dracula',
                            codeBlockStyle={'overflowX': 'auto'},
                        ),
                    },
                ],
                centered=True,
            ),
            title='小贴士：文件上传服务接口示例',
            ghost=True,
            isOpen=False,
            className='tip-collapse',
        )
