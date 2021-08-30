from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('menu-demo-output', 'children'),
    Input('menu-demo', 'currentKey'),
    prevent_initial_call=True
)
def menu_callback_demo(currentKey):
    import time;time.sleep(1)

    return currentKey
