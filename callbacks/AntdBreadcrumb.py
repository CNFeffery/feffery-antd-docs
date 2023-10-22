import json
from dash.dependencies import Input, Output

from server import app

@app.callback(
    Output('breadcrumnb-demo-output', 'children'),
    Input('breadcrumnb-demo', 'clickedItem'),
    prevent_initial_call=True
)
def breadcrumb_callback_demo(clickedItem):

    return json.dumps(
        dict(clickedItem=clickedItem),
        indent=4,
        ensure_ascii=False
    )