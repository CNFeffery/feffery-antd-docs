import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('cascader-demo-output', 'children'),
    Input('cascader-demo', 'value')
)
def cascader_demo_callback(value):
    return str(value)


@app.callback(
    Output('cascader-multiple-demo-output', 'children'),
    Input('cascader-multiple-demo', 'value')
)
def cascader_multiple_demo_callback(value):
    return str(value)
