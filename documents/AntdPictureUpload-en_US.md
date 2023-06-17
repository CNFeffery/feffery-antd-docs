**id:** *string* or *dict*

　　Used to set the unique id information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, which can force a re-render of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**draggerStyle:** *dict*

　　Used to set the CSS style of the drag area.

**draggerClassName:** *string*

　　Used to set the CSS class name of the drag area.

**locale:** *string* (default: `'zh-cn'`)

　　Used to set the language for the functional text of the current component, available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**apiUrl:** *string*

　　Used to set the file upload service API endpoint for the current upload component. The request type is `POST` and it should accept the parameters `uploadId` and `filename`. The `uploadId` parameter is automatically passed from the current component, and the `filename` parameter contains the name of the target uploaded file. Below are examples of upload endpoints using Flask and FastAPI:

- Flask:

```python
import os
from flask import request

# Here, `app` refers to the Dash instance
@app.server.route('/upload/', methods=['POST'])
def upload():
    '''
    Construct the file upload service
    :return:
    '''

    # Get the uploadId parameter for specifying the save path
    uploadId = request.values.get('uploadId')

    # Get the uploaded file name
    filename = request.files['file'].filename

    # Create the directory based on the uploadId if it doesn't exist locally
    try:
        os.mkdir(os.path.join('custom_cache_root', uploadId))
    except FileExistsError:
        pass

    # Stream write the file to the specified directory
    with open(os.path.join('custom_cache_root', uploadId, filename), 'wb') as f:
        # Stream write large files, here '10' represents 10MB
        for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
            f.write(chunk)

    return {'filename': filename}
```

- FastAPI:

```python
import os
import uvicorn
from tqdm import tqdm
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# Define the cache root directory
config = {
    'cache_root_path': './caches'
}

app = FastAPI()

# Set CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/upload/')
def upload_file(uploadId: str, file: UploadFile = File(...)):
    # Create the directory based on the uploadId if it doesn't exist locally
    try:
        os.mkdir(os.path.join(config.get("cache_root_path"), uploadId))
    except FileExistsError:
        pass

    with open(os.path.join(config.get("cache_root_path"), uploadId, file.filename), 'wb') as f:
        # Stream write large files, here '10' represents 10MB
        for chunk in tqdm(iter(lambda: file.file.read(1024 * 1024 * 10), b'')):
            f.write(chunk)

    return {"filename": file.filename}
```

**headers:** *dict*

　　Used to set additional headers for the upload request.

**downloadUrl:** *string* type

　　 When you need to add a download link for an uploaded file, it is used to *set the file download service interface*. The request type is `GET`, and it requires the parameters `taskId` and `filename`. The `taskId` parameter is automatically passed with the current component's `uploadId` parameter, and the `filename` parameter is used to pass the file name of the target download file.

**editable:** *bool* type, default is `False`

　　 Used to *set whether to add image cropping, rotation, and other preprocessing functions* before the upload step.

**editConfig:** *dict* type

　　 When `editable=True` is set, it is used to *fine-tune the configuration of image editing-related functions*. The available key-value pair parameters are:

- **aspect:** *int* or *float* type, default is `1`. Used to *set the aspect ratio of the cropping area, i.e., the coefficient of (width / height)*.

- **shape:** *str* type, optional values are `'rect'` (rectangle) and `'round'` (circle), default is `'rect'` . Used to *set the shape mode of the cropping area*.

- **grid:** *bool* type, default is `False`. Used to *set whether to display the grid lines as an aid*.

- **quality:** *float* type, default is `0.4`. Used to *set the image quality level, with a value between 0 and 1*.

- **zoom:** *bool* type, default is `True`. Used to *set whether to enable image zooming*.

- **rotate:** *bool* type, default is `False`. Used to *set whether to enable image rotation*.

- **minZoom:** *int* or *float* type, default is `1`. Used to *set the minimum zoom factor*.

- **maxZoom:** *int* or *float* type, default is `3`. Used to *set the maximum zoom factor*.

- **modalTitle:** *str* type, default is `'编辑图片'` (Edit Image). Used to *set the title of the image editing window*.

- **modalWidth:** *int* or *str* type, default is `520`. Used to *set the width of the image editing window*.

- **modalOk:** *str* type, default is `'确认'` (Confirm). Used to *set the content of the confirmation button in the image editing window*.

- **modalCancel:** *str* type, default is `'取消'` (Cancel). Used to *set the content of the cancel button in the image editing window*.

**fileListMaxLength:** *int* type, default is `3`

　　 Used to *set the maximum number of records in the uploaded file list*.

**fileTypes:** `list[string]` type

　　 Used to *set the file extension types accepted by the current upload component*, for example, `['csv', 'tsv', 'txt']`, with no restrictions by default.

**buttonContent:** *component type*

　　 Used to *set the content of the upload button*.

**uploadId:** *string* type

　　 Used to *set the unique ID information used by the current upload component when calling file upload, download, and other services*. If not set, a random UUID will be generated as the `uploadId` by default.

**fileMaxSize:** *int* or *float* type, default is `500`

　　 Used to *set the maximum file size for the current upload component*, in megabytes.

**failedTooltipInfo:** *string* type

　　 Used to *set the tooltip text content when hovering over a failed uploaded file in the uploaded list*.

**showRemoveIcon:** *bool* type, default is `True`

　　 Used to *set whether to render a delete button for each uploaded image*.

**showPreviewIcon:** *bool* type, default is `True`

　　 Used to *set whether to render a preview button for each uploaded image*.

**confirmBeforeDelete:** *bool* type, default is `False`

　　 Used to *add a confirmation modal for the delete operation of uploaded files*.

**showPercent:** *bool* type, default is `False`

　　 Used to *add progress percentage information to the file upload progress bar*.

**progressProps:** *dict* type

　　 Used to *configure parameters related to the file upload progress bar*. The available key-value pair parameters are:

- **strokeColor:** *string* or *dict* type, used to *set the color of the progress bar*. When a *dict* type is passed as input, gradient colors can be set. The available key-value pair parameters are:
  - **from:** *string* type, used to *set the starting color of the progress bar*.
  - **to:** *string* type, used to *set the ending color of the progress bar*.
- **strokeWidth:** *int* type, used to *set the pixel width of the progress bar*.
- **format:** *dict* type, used to *configure the content of the percentage text*. The available key-value pair parameters are:
  - **prefix:** *string* type, default is `''`, used to *set the prefix text of the progress bar percentage*.
  - **suffix:** *string* type, default is `'%'`, used to *set the suffix text of the progress bar percentage*.

**showSuccessMessage:** *bool* type, default is `True`

　　 Used to *set whether to display a corresponding message prompt after each successful file upload*.

**showErrorMessage:** *bool* type, default is `True`

　　 Used to *set whether to display a corresponding message prompt after each failed file upload*.

**lastUploadTaskRecord:** `dict` or `list[dict]` type

　　 Used to *listen to the recent information of the uploaded file(s) by the user*. In single-file upload mode, it is a single dictionary, while in multiple-file or folder upload mode, it is a list of dictionaries. Each dictionary has the following key-value pairs:

- **fileName:** Used to *record the corresponding file name*.
- **fileSize:** Used to *record the corresponding file size*.
- **completeTimestamp:** Used to *record the timestamp when the current file upload is completed*.
- **taskStatus:** Used to *record the upload status of the current file*. `'success'` indicates a successful upload, `'failed'` indicates a failed upload.
- **taskId:** Same as the `uploadId` of the current upload component.

**listUploadTaskRecord:** `list[dict]` type

　　 Used to *listen to the information of the currently uploaded file list*. Each dictionary has the following key-value pairs:

- **fileName:** Used to *record the corresponding file name*.
- **fileSize:** Used to *record the corresponding file size*.
- **completeTimestamp:** Used to *record the timestamp when the current file upload is completed*.
- **taskStatus:** Used to *record the upload status of the current file*. `'success'` indicates a successful upload, `'failed'` indicates a failed upload.
- **taskId:** Same as the `uploadId` of the current upload component.
- **uid:** Used to *uniquely identify the current file*.
- **url:** Used to *record the download link of the current file* when the `downloadUrl` parameter is present.

**defaultFileList:** `list[dict]` type

　　 Used to *set the initial list of uploaded files* for display purposes only. Each dictionary has the following key-value pairs:

- **name:** *string* type, used to *set the current file name*.
- **status:** *string* type, used to *set the display status of the current file*. Possible values are `'done'` (successful upload status) and `'error'` (upload failed status).
- **uid:** *string* type, used to *uniquely identify the current file*.
- **url:** *string* type, used to *set the download link of the current file*.
- **taskId:** *string* type, used to *indicate the uploadId status corresponding to the current uploaded record*. When a value is provided, it will be used as the default `uploadId` if the `uploadId` of the current component is not set.
- **fileSize:** *int* type, used to *set the size of the current file*.

**disabled:** *bool* type, default is `False`

　　 Used to *set whether the current component is disabled*.

**status:** *string* type

　　 Used to *forcefully set the status of the component*. Possible values are `'error'` and `'warning'`.