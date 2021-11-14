import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('popconfirm-demo-output-1', 'children'),
     Output('popconfirm-demo-output-2', 'children')],
    [Input('popconfirm-demo', 'confirmCounts'),
     Input('popconfirm-demo', 'cancelCounts')],
    prevent_initial_call=True
)
def popconfirm_demo_callback(confirmCounts, cancelCounts):
    return str(confirmCounts), str(cancelCounts)
