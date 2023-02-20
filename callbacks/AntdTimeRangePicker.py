from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('time-range-picker-demo-output', 'children'),
    Input('time-range-picker-demo', 'value')
)
def time_range_picker_demo(value):

    return f'value: {value}'


@app.callback(
    Output('time-range-picker-format-demo-output', 'children'),
    Input('time-range-picker-format-demo', 'value')
)
def time_range_picker_format_demo(value):

    return f'value: {value}'
