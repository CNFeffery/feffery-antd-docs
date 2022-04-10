**apiUrl：** *string*型

　　用于自定义上传服务对应的POST请求*接口url*，下面提供`flask`与`fastapi`的文件上传服务创建方式示例仅供参考：

- **flask**

```python
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
```

- **fastapi**

```python
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


if __name__ == '__main__':
    uvicorn.run(app='api:app', host="0.0.0.0", port=8000)
```

　　譬如上面`flask`的例子中我们是基于`Dash()`实例化对象自身的`server`对象创建的`flask`服务，因此`apiUrl`直接填入`'/upload/'`即可

**text：** *string*型

　　用于设置*上传区域主要文字说明内容*

**hint：** *string*型

　　用于设置*上传区域次要文字说明内容*

**fileListMaxLength：** *int*型，默认为`None`

　　用于设置上传组件显示的已上传文件列表项目数量，默认为`None`即无限制

**fileTypes：** *list*型，默认为`[]`

　　用于设置允许上传的文件格式，如`['xlsx', 'xls', 'xlsm']`即代表允许上传常见的excel文件格式，默认接受任意格式文件

**uploadId：** *string*型

　　配合前面提供的API参考，作为`uploadId`参数，用于在设置的缓存目录下指向被上传文件的实际保存目录，此参数不填写时，`AntdUpload`内部会自动生成具有高度唯一性的`uuid`作为`uploadId`

**fileMaxSize：** *int*型，默认为`500`

　　用于设置单个上传文件允许的最大体积，单位为MB

**multiple：** *bool*型，默认为`False`

　　用于设置是否开启多文件上传模式

**directory：** *bool*型，默认为`False`

　　用于设置是否开启文件夹整体上传模式

**failedTooltipInfo：** *string*型，默认为`'上传失败'`

　　用于自定义鼠标悬浮在上传列表中的*失败*任务上时显示的提示信息内容

**lastUploadTaskRecord：** *dict*或*list*型

　　用于在回调中记录最近一次成功或失败上传状态下的相关参数信息，主要包含以下键值对（`multiple=True`或`directory=True`时为由下列格式字典组成的列表）：

- fileName：记录本次任务的上传文件名
- fileSize：记录本次任务的文件体积
- completeTimestamp：记录本次任务对应的时间戳信息
- taskStatus：记录本次任务执行结果（`success`或`failed`）
- taskId：此信息只有状态为`success`时才会携带，记录了本次成功上传任务对应的`uploadId`信息，方便开发者在回调中获取到上传路径信息
