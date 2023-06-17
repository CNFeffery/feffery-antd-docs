**id:** *string* or *dict*

　　Used to set the unique ID for the current component.

**key:** *string*

　　Updates the `key` value of the current component, enabling a forced redraw of the component.

**style:** *dict*

　　Used to set the CSS styles for the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**draggerStyle:** *dict*

　　Used to set the CSS styles for the drag area.

**draggerClassName:** *string* or *dict*

　　Used to set the CSS class name for the drag area, supports [dynamic CSS](/advanced-classname).

**locale:** *string*, default is `'zh-cn'`

　　Used to set the language for the functional text of the current component. Available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**apiUrl:** *string*

　　Used to set the file upload service endpoint for the current upload component. The request type is `POST` and it should accept the parameters `uploadId` and `filename`. The `uploadId` parameter is automatically passed from the current component's `uploadId`, and the `filename` parameter is used to pass the name of the target upload file. Below are examples of upload endpoints using Flask and FastAPI:

- Flask

```python
import os
from flask import request

# Here, 'app' refers to the Dash instance
@app.server.route('/upload/', methods=['POST'])
def upload():
    '''
    Construct the file upload service
    :return:
    '''

    # Get the uploadId parameter for the save path
    uploadId = request.values.get('uploadId')

    # Get the uploaded file name
    filename = request.files['file'].filename

    # Based on the uploadId, automatically create a directory if it doesn't exist locally
    try:
        os.mkdir(os.path.join('custom_cache_root_directory', uploadId))
    except FileExistsError:
        pass

    # Stream the file to the specified directory
    with open(os.path.join('custom_cache_root_directory', uploadId, filename), 'wb') as f:
        # Stream write large files, where 10 represents 10MB
        for chunk in iter(lambda: request.files['file'].read(1024 * 1024 * 10), b''):
            f.write(chunk)

    return {'filename': filename}
```

- FastAPI

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

# Set up cross-origin resource sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/upload/')
def upload_file(uploadId: str, file: UploadFile = File(...)):
    # Based on the uploadId, automatically create a directory if it doesn't exist locally
    try:
        os.mkdir(os.path.join(config.get("cache_root_path"), uploadId))
    except FileExistsError:
        pass

    with open(os.path.join(config.get("cache_root_path"), uploadId, file.filename), 'wb') as f:
        # Stream write large files, where 10 represents 10MB
        for chunk in tqdm(iter(lambda: file.file.read(1024 * 1024 * 10), b'')):
            f.write(chunk)

    return {"filename": file.filename}
```

**headers:** *dict*

　　Used to set additional headers for the upload request.

**downloadUrl:** *string* type

　　Used to set the file download service interface when adding download links to uploaded files. The request type is `GET`, and it requires parameters `taskId` and `filename`. Among them, `taskId` automatically passes the `uploadId` parameter of the current component, and `filename` passes the file name of the target download file.

**text:** *component* type

　　Used to set the main content of the drag-and-drop area.

**hint:** *string* type

　　Used to set the secondary content of the drag-and-drop area.

**fileListMaxLength:** *int* type, default: `3`

　　Used to set the maximum number of records in the uploaded file list.

**fileTypes:** *list[string]* type

　　Used to set the file extension types accepted by the current upload component, such as `['csv', 'tsv', 'txt']`. There is no restriction by default.

**uploadId:** *string* type

　　Used to set the unique ID information used by the current upload component when calling file upload, download, and other services. When not set, a random UUID will be generated as the `uploadId`.

**fileMaxSize:** *int* or *float* type, default: `500`

　　Used to set the maximum file size limit for individual files in the current upload component, in megabytes (MB).

**multiple:** *bool* type, default: `False`

　　Used to set whether to allow uploading multiple files at once.

**directory:** *bool* type, default: `False`

　　Used to set whether to enable the folder upload mode.

**failedTooltipInfo:** *string* type

　　Used to set the mouse hover tooltip text content for failed uploaded files in the uploaded list.

**showUploadList:** *bool* type, default: `True`

　　Used to set whether to display the list of uploaded files.

**confirmBeforeDelete:** *bool* type, default: `False`

　　Used to add a confirmation modal for deleting uploaded files.

**showPercent:** *bool* type, default: `False`

　　Used to add progress percentage text to the file upload progress bar.

**progressProps:** *dict* type

　　Used to configure parameters related to the file upload progress bar. The available key-value pairs are:

- **strokeColor:** *string* or *dict* type, used to set the progress bar color. When a *dict* type is passed, it can set gradient colors. The available key-value pairs are:
  - **from:** *string* type, used to set the start color of the progress bar.
  - **to:** *string* type, used to set the end color of the progress bar.
- **strokeWidth:** *int* type, used to set the pixel width of the progress bar.
- **format:** *dict* type, used to configure the percentage text content. The available key-value pairs are:
  - **prefix:** *string* type, default: `''`, used to set the prefix text of the progress bar percentage.
  - **suffix:** *string* type, default: `'%'`, used to set the suffix text of the progress bar percentage.

**showSuccessMessage:** *bool* type, default: `True`

　　Used to set whether to display a corresponding message after each successful file upload.

**showErrorMessage:** *bool* type, default: `True`

　　Used to set whether to display a corresponding message after each failed file upload.

**lastUploadTaskRecord:** *dict* or *list[dict]* type

　　Used to monitor the information of the most recent file uploaded by the user. In single file upload mode, it is a single dictionary, and in multiple file or folder upload mode, it is a list of dictionaries. Each dictionary has the following key-value pairs:

- **fileName:** Used to record the corresponding file name.
- **fileSize:** Used to record the corresponding file size.
- **completeTimestamp:** Used to record the timestamp when the current file upload is completed.
- **taskStatus:** Used to record the upload status of the current file. `'success'` indicates a successful upload, `'failed'` indicates a failed upload.
- **taskId:** Same as the `uploadId` of the current upload component.

**listUploadTaskRecord:** *list[dict]* type

　　Used to monitor the information of the currently uploaded file list. Each dictionary in the list has the following key-value pairs:

- **fileName:** Used to record the corresponding file name.
- **fileSize:** Used to record the corresponding file size.
- **completeTimestamp:** Used to record the timestamp when the current file upload is completed.
- **taskStatus:** Used to record the upload status of the current file. `'success'` indicates a successful upload, `'failed'` indicates a failed upload.
- **taskId:** Same as the `uploadId` of the current upload component.
- **uid:** Used to uniquely identify the current file.
- **url:** Used to record the download link of the current file when the `downloadUrl` parameter exists.

**defaultFileList:** *list[dict]* type

　　Used to set the initial list of uploaded files for display purposes only. Each dictionary in the list has the following key-value pairs:

- **name:** *string* type, used to set the current file name.
- **status:** *string* type, used to set the display status of the current file. Possible values are `'done'` (successful upload status) and `'error'` (upload failed status).
- **uid:** *string* type, used to uniquely identify the current file.
- **url:** *string* type, used to set the download link of the current file.
- **taskId:** *string* type, used to indicate the `uploadId` status corresponding to the current uploaded record. When a value is passed in, it will be used as the default `uploadId` when the `uploadId` of the current component is not set.
- **fileSize:** *int* type, used to set the size of the current file.

**disabled:** *bool* type, default: `False`

　　Used to set whether the current component is disabled.

**status:** *string* type

　　Used to forcibly set the status of the component. Possible values are `'error'` and `'warning'`.