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

**editable：** *bool*型，默认为`False`

　　设置*是否开启上传前图片编辑功能*，开启后会在选择图片文件后弹出图片编辑操作框，以支持对原始图片进行缩放、旋转、裁切等操作后再上传至服务器

**editConfig：** *dict*型

　　当设置`editable=True`时，用于*细化配置图片编辑相关功能*，可选的配置项键值对有：

- aspect：*int*或*float*型，默认为`1`，用于*设置裁切区域宽高比，即（宽度 / 高度）的系数*
- shape：*str*型，可选的有`'rect'`（矩形）和`'round'`（圆），默认为`'rect'`，用于*设置裁切区域形状模式*
- grid：*bool*型，默认为`False`，用于*设置是否显示辅助网格线*
- quality：*float*型，默认为`0.4`，用于*设置图片质量水平，取值应当在0到1之间*
- zoom：*bool*型，默认为`True`，用于*设置是否开启图片缩放功能*
- rotate：*bool*型，默认为`False`，用于*设置是否开启图片旋转功能*
- minZoom：*int*或*float*型，默认为`1`，用于*设置最小缩放倍数*
- maxZoom：*int*或*float*型，默认为`3`，用于*设置最大缩放倍数*
- modalTitle：*str*型，默认为`'编辑图片'`，用于*设置图片编辑窗口的标题内容*
- modalWidth：*int*或*str*型，默认为`520`，用于*设置图片编辑窗口的宽度*
- modalOk：*str*型，默认为`'确认'`，用于*设置图片编辑窗口确认按钮的内容*
- modalCancel：*str*型，默认为`'取消'`，用于*设置图片编辑窗口取消按钮的内容*

**fileListMaxLength：** *int*型，默认为`None`

　　用于设置*所记录的已上传图片列表项目数量上限*，默认为`None`即无限制

**fileTypes：** *list*型，默认为`['tiff', 'bmp', 'gif', 'png', 'jpeg', 'jpg', 'webp', 'ico', 'tif']`

　　用于设置*允许上传的文件格式*

**buttonContent：** *string*型

　　用于设置上传组件按钮中的*说明文字内容*

**uploadId：** *string*型

　　配合前面提供的API参考，作为`uploadId`参数，用于在设置的缓存目录下指向被上传文件的实际保存目录，此参数不填写时，`AntdPictureUpload`内部会自动生成具有高度唯一性的`uuid`作为`uploadId`

**fileMaxSize：** *int*型，默认为`10`

　　用于设置单张上传图片允许的最大体积，单位为MB

**failedTooltipInfo：** *string*型，默认为`'上传失败'`

　　用于自定义鼠标悬浮在上传列表中的*失败*任务上时显示的提示信息内容

**lastUploadTaskRecord：** *dict*或*list*型

　　用于在回调中记录最近一次成功或失败上传状态下的相关参数信息，主要包含以下键值对（`multiple=True`或`directory=True`时，`lastUploadTaskRecord`返回由下列结构字典构成的列表）：

- fileName：记录本次任务的上传文件名
- fileSize：记录本次任务的文件体积
- completeTimestamp：记录本次任务对应的时间戳信息
- taskStatus：记录本次任务执行结果（`success`或`failed`）
- taskId：记录了本次成功上传任务对应的`uploadId`信息，方便开发者在回调中获取到上传路径信息

**listUploadTaskRecord：** *list*型

　　用于*记录当前上传组件中所记录的全部已上传文件信息*，格式同`lastUploadTaskRecord`的列表模式



