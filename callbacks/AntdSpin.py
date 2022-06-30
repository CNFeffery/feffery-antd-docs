from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('spin-basic-demo-output', 'children'),
    Input('spin-basic-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def spin_basic_callback_demo(nClicks):
    import time
    time.sleep(2)

    return f'nClicks: {nClicks}'


@app.callback(
    Output('spin-delay-demo-output1', 'children'),
    Input('spin-delay-demo-input1', 'nClicks'),
    prevent_initial_call=True
)
def spin_delay_callback_demo1(nClicks):
    import time
    time.sleep(0.5)

    return f'0.5秒回调 nClicks: {nClicks}'


@app.callback(
    Output('spin-delay-demo-output2', 'children'),
    Input('spin-delay-demo-input2', 'nClicks'),
    prevent_initial_call=True
)
def spin_delay_callback_demo2(nClicks):
    import time
    time.sleep(2)

    return f'2秒回调 nClicks: {nClicks}'


@app.callback(
    Output('spin-include-demo-output1', 'children'),
    Input('spin-include-demo-input1', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_callback_demo1(nClicks):
    import time
    time.sleep(1)

    return f'未被includeProps指定 nClicks: {nClicks}'


@app.callback(
    Output('spin-include-demo-output2', 'children'),
    Input('spin-include-demo-input2', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_callback_demo2(nClicks):
    import time
    time.sleep(1)

    return f'被includeProps指定 nClicks: {nClicks}'


@app.callback(
    Output('spin-exclude-demo-output1', 'children'),
    Input('spin-exclude-demo-input1', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_callback_demo1(nClicks):
    import time
    time.sleep(1)

    return f'未被excludeProps指定 nClicks: {nClicks}'


@app.callback(
    Output('spin-exclude-demo-output2', 'children'),
    Input('spin-exclude-demo-input2', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_callback_demo2(nClicks):
    import time
    time.sleep(1)

    return f'被excludeProps指定 nClicks: {nClicks}'


@app.callback(
    Output('spin-custom-indicator-demo-output', 'children'),
    Input('spin-custom-indicator-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def spin_custom_indicator_callback_demo(nClicks):
    import time
    time.sleep(2)

    return f'nClicks: {nClicks}'
