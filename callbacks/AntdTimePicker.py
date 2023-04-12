from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('time-picker-demo-output', 'children'),
    Input('time-picker-demo', 'value')
)
def time_picker_demo(value):

    return f'value: {value}'


@app.callback(
    Output('time-picker-format-demo-output', 'children'),
    Input('time-picker-format-demo', 'value')
)
def time_picker_format_demo(value):

    return f'value: {value}'
