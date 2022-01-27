from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('radio-group-demo-output', 'children'),
    Input('radio-group-demo', 'value')
)
def radio_group_demo_callback(value):
    return str(value)
