from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('segmented-demo-output', 'children'),
    Input('segmented-demo', 'value')
)
def segmented_callback_demo(value):
    return f'value: {value}'
