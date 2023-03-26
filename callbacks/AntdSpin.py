import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('spin-basic-demo-output', 'children'),
    Input('spin-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def spin_basic_demo(nClicks):

    time.sleep(2)

    return f'nClicks: {nClicks}'


@app.callback(
    Output('spin-exclude-demo-output1', 'children'),
    Input('spin-exclude-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('spin-exclude-demo-output2', 'children'),
    Input('spin-exclude-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_demo2(nClicks):

    time.sleep(1)

    return f'按钮2: {nClicks}'


@app.callback(
    Output('spin-include-demo-output1', 'children'),
    Input('spin-include-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('spin-include-demo-output2', 'children'),
    Input('spin-include-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_demo2(nClicks):

    time.sleep(1)

    return f'按钮2: {nClicks}'


@app.callback(
    Output('spin-custom-demo-output', 'children'),
    Input('spin-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def spin_custom_demo(nClicks):

    time.sleep(2)

    return f'nClicks: {nClicks}'
