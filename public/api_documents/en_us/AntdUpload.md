- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- name (string; optional):
    Used with `AntdForm` for batch value collection/control, serving as the field name of the current form item, with `id` as the default value.

- enableBatchControl (boolean; default True):
    Controls whether the current component participates in the effective `AntdForm` batch value collection/control feature. Default: `True`.

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- apiUrl (string; optional):
    File upload endpoint URL.

- apiUrlExtraParams (dict; optional):
    Additional parameters for file upload requests.

- headers (dict; optional):
    Additional headers for file upload requests.

- withCredentials (boolean; default False):
    Whether upload requests include credentials such as cookies. Default: `False`.

- withOriginFileObj (boolean; default False):
    Whether `listUploadTaskRecord` includes the browser's native `originFileObj` information. Default: `False`.

- downloadUrl (string; optional):
    `GET` download endpoint for uploaded files. Requests include `taskId` and `filename`.

- downloadUrlExtraParams (dict; optional):
    Additional file download request parameters used with `downloadUrl`.

- downloadUrlFromBackend (boolean; default False):
    Whether to use the upload response's `url` as the download link. Default: `False`.

- fileListMaxLength (number; optional):
    Maximum number of files in the uploaded file list.

- fileTypes (list of strings; optional):
    Allowed file extensions; unrestricted by default.

- buttonContent (a list of or a singular dash component, string or number; optional):
    Custom upload button content. Supports components.

- buttonIcon (a list of or a singular dash component, string or number; optional):
    Custom upload button icon. Supports components.

- buttonProps (dict; optional):
    Upload button settings.

    `buttonProps` is a dict with keys:

    - size (a value equal to: 'default', 'small', 'large'; optional):
        Button size. Supported values: `'default'`, `'small'`, `'large'`. Default: `'default'`.

    - type (a value equal to: 'primary', 'ghost', 'dashed', 'link', 'text', 'default'; optional):
        Button type, options include `'default'`, `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`. Default value: `'default'`.

    - danger (boolean; optional):
        Whether the button uses the danger state. Default: `False`.

    - block (boolean; optional):
        Whether the button fills its parent width. Default: `False`.

    - style (dict; optional):
        Button CSS style.

    - className (string; optional):
        Button CSS class name.

- uploadId (string; optional):
    Custom `uploadId` sent with upload requests, which can help the backend determine the upload directory.

- fileMaxSize (number; default 500):
    Maximum upload size in megabytes.

- multiple (boolean; default False):
    Whether multiple files can be uploaded. Default: `False`.

- directory (boolean; default False):
    Whether folder uploads are enabled. Default: `False`.

- failedTooltipInfo (string; optional):
    Message displayed when file upload fails. Default: `'上传失败'`.

- showUploadList (boolean; default True):
    Whether to show the uploaded file list. Default: `True`.

- confirmBeforeDelete (boolean; default False):
    Whether deleting an uploaded file requires confirmation in a modal. Default: `False`.

- showPercent (boolean; default False):
    Whether to show upload progress. Default: `False`.

- progressProps (dict; optional):
    Upload progress bar settings.

    `progressProps` is a dict with keys:

    - strokeColor (dict; optional):
        Progress bar color.

        `strokeColor` is a string

      Or dict with keys:

        - from (string; optional):

            Gradient start color.

        - to (string; optional):

            Gradient end color.

    - strokeWidth (number; optional):
        Progress bar width in pixels.

    - format (dict; optional):
        Progress text format.

        `format` is a dict with keys:

        - prefix (string; optional):
            Progress text prefix.

        - suffix (string; optional):
            Progress text suffix. Default: `'%'`.

- showSuccessMessage (boolean; default True):
    Whether to show a separate message for each successful upload. Default: `True`.

- showErrorMessage (boolean; default True):
    Whether to show a separate message for each failed upload. Default: `True`.

- pastable (boolean; default False):
    Whether pasting a locally copied file anywhere on the page uploads it. Default: `False`.

- lastUploadTaskRecord (dict; optional):
    Information about the most recent upload task.

    `lastUploadTaskRecord` is a dict with keys:

    - fileName (string; optional):
        File name.

    - fileSize (number; optional):
        File size.

    - completeTimestamp (number; optional):
        Upload completion timestamp.

    - taskStatus (string; optional):
        Upload task status: `'success'` for successful uploads or `'failed'` for failed uploads.

    - taskId (string; optional):
        Unique upload task ID; omitted when the task status is `'failed'`.

    - url (string; optional):
        File download URL.

    - uploadResponse (boolean | number | string | dict | list; optional):
        Response returned by the upload endpoint. | list of dicts with keys:

    - fileName (string; optional):
        File name.

    - fileSize (number; optional):
        File size.

    - completeTimestamp (number; optional):
        Upload completion timestamp.

    - taskStatus (string; optional):
        Upload task status: `'success'` for successful uploads or `'failed'` for failed uploads.

    - taskId (string; optional):
        Unique upload task ID; omitted when the task status is `'failed'`.

    - url (string; optional):
        File download URL.

    - uploadResponse (boolean | number | string | dict | list; optional):
        Response returned by the upload endpoint.

- listUploadTaskRecord (list of dicts; optional):
    Upload task information for files in the current uploaded file list.

    `listUploadTaskRecord` is a list of dicts with keys:

    - fileName (string; optional):
        File name.

    - fileSize (number; optional):
        File size.

    - completeTimestamp (number; optional):
        Upload completion timestamp.

    - taskStatus (string; optional):
        Upload task status: `'success'` for successful uploads or `'failed'` for failed uploads.

    - taskId (string; optional):
        Unique upload task ID; omitted when the task status is `'failed'`.

    - uid (string; optional):
        Unique file upload ID generated by the frontend.

    - url (string; optional):
        File download URL.

    - uploadResponse (boolean | number | string | dict | list; optional):
        Response returned by the upload endpoint.

    - originFileObj (boolean | number | string | dict | list; optional):
        Main `originFileObj` information for the current upload task when `withOriginFileObj=True`.

- defaultFileList (list of dicts; optional):
    Initial file list information.

    `defaultFileList` is a list of dicts with keys:

    - name (string; optional):
        File name.

    - status (a value equal to: 'done', 'error', 'removed'; optional):
        File display status. Supported values: `'done'`, `'error'`, `'removed'`.

    - uid (boolean | number | string | dict | list; optional):
        Unique file ID.

    - url (string; optional):
        File download URL.

    - taskId (string; optional):
        A valid supplied value becomes the component's `uploadId`.

    - fileSize (number; optional):
        File size.

- disabled (boolean; default False):
    Whether to disable the current component. Default: `False`.

- status (a value equal to: 'error', 'warning'; optional):
    Control the validation state. Options are `'error'`, `'warning'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.
