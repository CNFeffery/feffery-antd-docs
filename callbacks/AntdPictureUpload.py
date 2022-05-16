import json
from dash.dependencies import Input, Output

from server import app


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
