from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('select-demo-output', 'children'),
    Input('select-demo', 'value'),
    prevent_initial_call=True
)
def button_callback_demo(value):
    import time;time.sleep(1)

    return str(value)
