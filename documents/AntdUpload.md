**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**apiUrl：** *string*型

　　用于*设置当前上传组件所使用的文件上传服务接口地址*，请求类型为`POST`，需接受参数`uploadId`和`filename`，其中`uploadId`自动传递当前组件的`uploadId`参数，`filename`传递目标上传文件的文件名，下面是`flask`和`fastapi`的上传接口示例：

- `flask`

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

- `fastapi`

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
```

**downloadUrl：** *string*型

　　当需要为已上传的文件添加下载链接时，用于*设置文件下载服务接口*，请求类型为`GET`，需接受参数`taskId`和`filename`，其中`taskId`自动传递当前组件的`uploadId`参数，`filename`传递目标下载文件的文件名

**fileListMaxLength：** *int*型，默认为`3`

　　用于*设置已上传文件列表的最大记录数量*

**fileTypes：** `list[string]`型

　　用于*设置当前上传组件所接收的文件扩展类型*，譬如`['csv', 'tsv', 'txt']`，默认无限制

**buttonContent：** *组件型*

　　用于*设置当前上传组件触发点按钮内的内容*

**uploadId：** *string*型

　　用于*设置当前上传组件在调用文件上传、下载等服务时所使用到的唯一id信息*

**fileMaxSize：** *int*或*float*型，默认为`500`

　　用于*为当前上传组件设置单个文件大小上限*，单位：兆

**multiple：** *bool*型，默认为`False`

　　用于*设置是否允许一次性上传多个文件*

**directory：** *bool*型，默认为`False`

　　用于*设置是否开启文件夹整体上传模式*

**failedTooltipInfo：** *string*型

　　用于*设置已上传列表中上传失败文件鼠标悬停提示文字内容*

**showUploadList：** *bool*型，默认为`True`

　　用于*设置是否展示已上传文件列表*

**confirmBeforeDelete：** *bool*型，默认为`False`

　　用于*设置是否为已上传文件的删除操作添加二次确认模态框*

**showPercent：** *bool*型，默认为`False`

　　用于*设置是否为文件上传进度条添加进度百分比文字信息*

**progressProps：** *dict*型

　　用于*配置文件上传进度条相关参数*，可用的键值对参数有：

- **strokeColor：** *string*或*dict*型，用于*设置进度条颜色*，当传入*dict*型输入时可设置渐变色，可用的键值对参数有：
  - **from：** *string*型，用于*设置进度条起始颜色*
  - **to：** *string*型，用于*设置进度条终点颜色*
- **strokeWidth：** *int*型，用于*设置进度条像素线宽*
- **format：** *dict*型，用于*配置百分比文字内容*，可用的键值对参数有：
  - **prefix：** *string*型，默认为`''`，用于*设置进度条百分比文字内容的前缀文字*
  - **suffix：** *string*型，默认为`'%'`，用于*设置进度条百分比文字内容的后缀文字*

**showSuccessMessage：** *bool*型，默认为`True`

　　用于*设置是否在每次新文件上传成功后弹出相应的消息提示*

**showErrorMessage：** *bool*型，默认为`True`

　　用于*设置是否在每次新文件上传失败后弹出相应的消息提示*

**lastUploadTaskRecord：** `dict`或`list[dict]`型

　　用于*监听最近一次用户所上传文件相关信息*，单文件上传模式下为单个字典，多文件及文件夹上传模式下为字典元素构成的列表，其中每个字典具有的键值对有：

- **fileName：** 用于*记录对应文件名*
- **fileSize：** 用于*记录对应文件大小*
- **completeTimestamp：** 用于*记录当前文件上传完成对应的时间戳信息*
- **taskStatus：** 用于*记录当前文件的上传状态*，`'success'`表示上传成功，`'failed'`表示上传失败
- **taskId：** 同当前上传组件的`uploadId`

**listUploadTaskRecord：** `list[dict]`型

　　用于*监听当前已上传文件列表信息*，其中每个字典具有的键值对有：

- **fileName：** 用于*记录对应文件名*
- **fileSize：** 用于*记录对应文件大小*
- **completeTimestamp：** 用于*记录当前文件上传完成对应的时间戳信息*
- **taskStatus：** 用于*记录当前文件的上传状态*，`'success'`表示上传成功，`'failed'`表示上传失败
- **taskId：** 同当前上传组件的`uploadId`
- **uid：** 用于*唯一标识当前文件*
- **url：** 当参数`downloadUrl`存在时，用于*记录当前文件的下载链接*

**defaultFileList：** `list[dict]`型

　　用于*设置初始化时的已上传文件列表*，仅作展示使用，其中每个字典具有的键值对有：

- **name：** *string*型，用于*设置当前文件名*
- **status：** *string*型，用于*设置当前文件的展示状态*，可选的有`'done'`（成功上传状态）、`'error'`（上传失败状态）
- **uid：** *string*型，用于*唯一表示当前文件*
- **url：** *string*型，用于*设置当前文件的下载链接*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`
