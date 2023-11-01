**id:** *string* or *dict*

　　Used to set the unique ID information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, enabling the effect of forcing a redraw of the current component.

**style:** *dict*

　　Used to set the CSS style for the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name for the current component, supporting [dynamic CSS](/advanced-classname).

**locale:** *string*, default is `'zh-cn'`

　　Used to set the language for the functional text of the current component. Available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**apiUrl:** *string*

　　Used to set the file upload service API address for the current upload component. The request type is `POST` and it should accept the parameters `uploadId` and `filename`. The `uploadId` parameter is automatically passed from the current component's `uploadId` parameter, and the `filename` parameter is used to pass the name of the target uploaded file. Below are examples of upload interfaces using `flask` and `fastapi`:

- `flask`

```python
import os
from flask import request

# The app here refers to the Dash instance
@app.server.route('/upload/', methods=['POST'])
def upload():
    '''
    Build file upload service
    :return:
    '''

    # Get the uploadId parameter for pointing to the save path
    uploadId = request.values.get('uploadId')

    # Get the uploaded file name
    filename = request.files['file'].filename

    # Create a directory based on the uploadId, if it doesn't exist locally
    try:
        os.mkdir(os.path.join('custom_cache_root', uploadId))
    except FileExistsError:
        pass

    # Stream write the file to the specified directory
    with open(os.path.join('custom_cache_root', uploadId, filename), 'wb') as f:
        # Stream write large files, where 10 represents 10MB
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

# Define the cache root directory
config = {
    'cache_root_path': './caches'
}

app = FastAPI()

# Set CORS permissions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/upload/')
def upload_file(uploadId: str, file: UploadFile = File(...)):
    # Create a directory based on the uploadId, if it doesn't exist locally
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

**apiUrlExtraParams：** *dict* type

　　Used to set additional parameters required for file upload services.

**headers:** *dict*

　　Used to set additional headers information for the upload request.

**withCredentials：** *bool* type, default: `False`

　　Used to set whether to carry credential information such as cookies when making upload requests. This parameter setting is invalid when the upload interface is on the same domain as the front-end page.

**downloadUrl：** *string* type

　　Used to set the file download service interface when a download link needs to be added to an uploaded file. The request type is `GET`, and it requires the parameters `taskId` and `filename`, where `taskId` is automatically passed as the `uploadId` parameter of the current component, and `filename` is the filename of the target file for download.

**downloadUrlExtraParams：** *dict* type

　　Used in conjunction with `downloadUrl` to set additional parameters for download links. After setting, the download link will automatically append the parameters.

**downloadUrlFromBackend：** *bool* type, default: `False`

　　Used to set a custom backend download interface for completed uploads. The interface response must have a `url` parameter, and its priority is lower than `downloadUrl`. When `downloadUrlFromBackend=True` is set and the upload interface response has a `url` parameter, the `url` parameter in the file list's related listener parameters will automatically listen for the `url` parameter returned by the backend interface.

**fileListMaxLength：** *int* type, default: `3`

　　Used to set the maximum number of records in the uploaded file list.

**fileTypes：** `list[string]` type

　　Used to set the file extension types accepted by the current upload component, for example, `['csv', 'tsv', 'txt']`. There is no restriction by default.

**buttonContent：** *component* type

　　Used to set the content inside the trigger button of the current upload component.

**buttonProps：** *dict* type

　　Used to configure parameters related to the upload button. Available key-value pairs include:

- **size：** *string* type, default: `'middle'`. Used to set the size of the upload button. Available options are `'small'`, `'middle'`, and `'large'`.
- **type：** *string* type, default: `'default'`. Used to set the style of the upload button. Available options are `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`, and `'default'`.
- **danger：** *bool* type, default: `False`. Used to set whether the upload button is rendered as a dangerous warning state.
- **block:** A *boolean* (bool) value, with a default of `False`, used to *determine whether the upload button should stretch to fill its parent element*.
- **style：** *dict* type. Used to set the CSS style of the upload button.
- **className：** *string* type. Used to set the CSS class name of the upload button.

**uploadId：** *string* type

　　Used to set the unique ID information used by the current upload component for calling file upload, download, and other services. By default, a random UUID is generated as the `uploadId` when not set.

**fileMaxSize：** *int* or *float* type, default: `500`

　　Used to set the maximum file size limit for the current upload component, in megabytes.

**multiple：** *bool* type, default: `False`

　　Used to set whether to allow uploading multiple files at once.

**directory：** *bool* type, default: `False`

　　Used to enable the whole folder upload mode.

**failedTooltipInfo：** *string* type

　　Used to set the tooltip text content when hovering over an uploaded file that failed to upload.

**showUploadList：** *bool* type, default: `True`

　　Used to set whether to display the uploaded file list.

**confirmBeforeDelete：** *bool* type, default: `False`

　　Used to add a confirmation modal for deleting uploaded files.

**showPercent：** *bool* type, default: `False`

　　Used to add progress percentage text information to the file upload progress bar.

**progressProps：** *dict* type

　　Used to configure parameters related to the file upload progress bar. Available key-value pairs include:

- **strokeColor：** *string* or *dict* type. Used to set the color of the progress bar. When a *dict* type input is provided, it can specify a gradient color. Available key-value pairs include:
  - **from：** *string* type. Used to set the starting color of the progress bar.
  - **to：** *string

* type. Used to set the ending color of the progress bar.
- **strokeWidth：** *int* type. Used to set the pixel line width of the progress bar.
- **format：** *dict* type. Used to configure the percentage text content. Available key-value pairs include:
  - **prefix：** *string* type, default: `''`. Used to set the prefix text of the progress bar percentage.
  - **suffix：** *string* type, default: `'%'`. Used to set the suffix text of the progress bar percentage.

**showSuccessMessage：** *bool* type, default: `True`

　　Used to show a corresponding message prompt after each new file upload succeeds.

**showErrorMessage：** *bool* type, default: `True`

　　Used to show a corresponding message prompt after each new file upload fails.

**lastUploadTaskRecord：** *dict* or *list[dict]* type

　　Used to monitor the information of the most recent file uploaded by the user. In single-file upload mode, it is a single dictionary, and in multiple file or folder upload mode, it is a list of dictionaries. Each dictionary contains the following key-value pairs:

- **fileName：** Used to record the corresponding file name.
- **fileSize：** Used to record the corresponding file size.
- **completeTimestamp：** Used to record the timestamp when the current file upload is completed.
- **taskStatus：** Used to record the upload status of the current file. `'success'` indicates a successful upload, and `'failed'` indicates a failed upload.
- **taskId：** Same as the `uploadId` of the current upload component.
- **url：** *string* type. Used to set the download link of the current file.
- **uploadResponse：** Used to listen to the response information from the upload interface.

**listUploadTaskRecord：** *list[dict]* type

　　Used to monitor the information of the currently uploaded file list. Each dictionary contains the following key-value pairs:

- **fileName：** Used to record the corresponding file name.
- **fileSize：** Used to record the corresponding file size.
- **completeTimestamp：** Used to record the timestamp when the current file upload is completed.
- **taskStatus：** Used to record the upload status of the current file. `'success'` indicates a successful upload, and `'failed'` indicates a failed upload.
- **taskId：** Same as the `uploadId` of the current upload component.
- **uid：** Used to uniquely identify the current file.
- **url：** When the `downloadUrl` parameter is provided or `downloadUrlFromBackend=True` is set, it is used to record the download link of the current file.
- **uploadResponse：** Used to listen to the response information from the upload interface.

**defaultFileList：** *list[dict]* type

　　Used to set the initial uploaded file list for display purposes only. Each dictionary contains the following key-value pairs:

- **name：** *string* type. Used to set the current file name.
- **status：** *string* type. Used to set the display status of the current file. Available options are `'done'` (successfully uploaded) and `'error'` (upload failed).
- **uid：** *string* type. Used to uniquely identify the current file.
- **url：** *string* type. Used to set the download link of the current file.
- **uploadResponse：** Used to listen to the response information from the upload interface.
- **taskId：** *string* type. Used as the default `uploadId` when the current component's `uploadId` is not set.
- **fileSize：** *int* type. Used to set the size of the current file.

**disabled：** *bool* type, default: `False`

　　Used to disable the current component.

**status：** *string* type

　　Used to forcefully set the status of the component. Available options are `'error'`

 and `'done'`.