**apiUrl：** *string*型

　　用于自定义上传服务对应的POST请求*接口url*，下面提供`flask`与`fastapi`的文件上传服务创建方式示例仅供参考：

> flask

```python
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
        with open(os.path.join('自定义缓存根目录', uploadId, filename), 'wb') as f:
            # 流式写出大型文件，这里的10代表10MB
            for chunk in tqdm(iter(lambda: request.files['file'].read(1024 * 1024 * 10), b'')):
                f.write(chunk)

    return {'filename': filename}
```

> fastapi

```python
import os
import uvicorn
from tqdm import tqdm
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# 定义缓存根目录
config = {
    'cache_root_path': r'../caches'
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

　　譬如上面`flask`的例子中我们是基于`Dash()`实例化对象自身创建的服务，因此`apiUrl`直接填入`/upload/`即可

