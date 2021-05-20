from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('button-demo-output', 'children'),
    Input('button-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_callback_demo(nClicks):
    import time;time.sleep(0.5)
    return nClicks
