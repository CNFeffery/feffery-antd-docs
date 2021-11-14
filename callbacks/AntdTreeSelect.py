import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('tree-select-demo-output', 'children'),
    Input('tree-select-demo', 'value')
)
def tree_select_demo_callback(value):
    time.sleep(0.5)
    return str(value)
