from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('rate-demo-output', 'children'),
    Input('rate-demo', 'value'),
    prevent_initial_call=True
)
def rate_demo_callback(value):
    return value
