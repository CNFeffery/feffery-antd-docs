import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('dragger-upload-demo', 'multiple'),
    Input('dragger-upload-demo-is-multiple', 'checked')
)
def dragger_upload_is_multiple(checked):
    return checked


@app.callback(
    Output('dragger-upload-demo-output', 'children'),
    [Input('dragger-upload-demo', 'lastUploadTaskRecord'),
     Input('dragger-upload-demo', 'listUploadTaskRecord')],
    prevent_initial_call=True
)
def dragger_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(
            {
                'lastUploadTaskRecord': lastUploadTaskRecord,
                'listUploadTaskRecord': listUploadTaskRecord
            },
            indent=4,
            ensure_ascii=False
        )
