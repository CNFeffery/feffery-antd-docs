import time
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('radio-group-demo-output', 'children'),
    Input('radio-group-demo', 'value')
)
def radio_group_demo_callback(value):
    time.sleep(0.5)
    return str(value)
