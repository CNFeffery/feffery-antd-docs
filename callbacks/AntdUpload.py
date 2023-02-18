import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('upload-demo', 'multiple'),
    Input('upload-demo-is-multiple', 'checked')
)
def upload_is_multiple(checked):
    return checked


@app.callback(
    Output('upload-demo-output', 'children'),
    [Input('upload-demo', 'lastUploadTaskRecord'),
     Input('upload-demo', 'listUploadTaskRecord')],
    prevent_initial_call=True
)
def upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(
            {
                'lastUploadTaskRecord': lastUploadTaskRecord,
                'listUploadTaskRecord': listUploadTaskRecord
            },
            indent=4,
            ensure_ascii=False
        )
