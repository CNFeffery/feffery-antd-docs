from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('slider-demo-output', 'children'),
    [Input('slider-demo-1', 'value'),
     Input('slider-demo-2', 'value')],
    prevent_initial_call=True
)
def transfer_callback_demo(value, range_value):
    import time;time.sleep(0.5)
    return f'单值选择当前值：{value}   范围选择当前值：{range_value}'
