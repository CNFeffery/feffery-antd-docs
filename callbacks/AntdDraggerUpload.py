import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('dragger-upload-demo-output', 'children'),
    Input('dragger-upload-demo', 'lastUploadTaskRecord'),
    prevent_initial_call=True
)
def upload_callback_demo(lastUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(lastUploadTaskRecord, indent=4, ensure_ascii=False)
