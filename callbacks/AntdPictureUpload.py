import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('picture-upload-icon-hide-demo', 'showRemoveIcon'),
     Output('picture-upload-icon-hide-demo', 'showPreviewIcon')],
    [Input('show-remove-icon', 'checked'),
     Input('show-preview-icon', 'checked')]
)
def picture_upload_icon_hide_demo(showRemoveIcon, showPreviewIcon):

    return showRemoveIcon, showPreviewIcon


@app.callback(
    Output('picture-upload-demo-output', 'children'),
    [Input('picture-upload-demo', 'lastUploadTaskRecord'),
     Input('picture-upload-demo', 'listUploadTaskRecord')],
    prevent_initial_call=True
)
def picture_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(
            {
                'lastUploadTaskRecord': lastUploadTaskRecord,
                'listUploadTaskRecord': listUploadTaskRecord
            },
            indent=4,
            ensure_ascii=False
        )
