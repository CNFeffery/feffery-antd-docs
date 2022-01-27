from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('skeleton-basic-demo-output', 'children'),
    Input('skeleton-basic-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_basic_callback_demo(nClicks):
    import time
    time.sleep(2)

    return f'nClicks: {nClicks}'


@app.callback(
    Output('skeleton-custom-demo-output', 'children'),
    Input('skeleton-custom-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_custom_callback_demo(nClicks):
    import time
    time.sleep(2)

    return f'nClicks: {nClicks}'
