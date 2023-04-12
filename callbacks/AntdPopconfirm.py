import json
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('popconfirm-demo-output', 'children'),
    [Input('popconfirm-demo', 'confirmCounts'),
     Input('popconfirm-demo', 'cancelCounts')],
    prevent_initial_call=True
)
def popconfirm_demo(confirmCounts, cancelCounts):

    return json.dumps(
        dict(
            confirmCounts=confirmCounts,
            cancelCounts=cancelCounts
        ),
        indent=4,
        ensure_ascii=False
    )
