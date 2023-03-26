import time
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('skeleton-basic-demo-output', 'children'),
    Input('skeleton-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_basic_demo(nClicks):

    time.sleep(2)

    return f'nClicks: {nClicks}'


@app.callback(
    Output('skeleton-active-demo-output', 'children'),
    Input('skeleton-active-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_active_demo(nClicks):

    time.sleep(2)

    return f'nClicks: {nClicks}'


@app.callback(
    Output('skeleton-custom-demo-output', 'children'),
    Input('skeleton-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_custom_demo(nClicks):

    time.sleep(2)

    return f'nClicks: {nClicks}'


@app.callback(
    Output('skeleton-exclude-demo-output1', 'children'),
    Input('skeleton-exclude-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_exclude_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('skeleton-exclude-demo-output2', 'children'),
    Input('skeleton-exclude-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_exclude_demo2(nClicks):

    time.sleep(1)

    return f'按钮2: {nClicks}'


@app.callback(
    Output('skeleton-include-demo-output1', 'children'),
    Input('skeleton-include-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_include_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('skeleton-include-demo-output2', 'children'),
    Input('skeleton-include-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_include_demo2(nClicks):

    time.sleep(1)

    return f'按钮2: {nClicks}'
