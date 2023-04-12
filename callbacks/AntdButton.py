import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('button-click-demo-output', 'children'),
    Input('button-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_click_demo(nClicks):

    return f'nClicks: {nClicks}'


@app.callback(
    Output('button-debounce-click-demo-output', 'children'),
    Input('button-debounce-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_debounce_click_demo(nClicks):

    return f'nClicks: {nClicks}'


@app.callback(
    [Output('button-auto-loading-demo-output', 'children'),
     Output('button-auto-loading-demo', 'loading')],
    Input('button-auto-loading-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_auto_loading_demo(nClicks):

    time.sleep(3)

    return f'nClicks: {nClicks}', False
