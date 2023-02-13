from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('date-range-picker-demo1-output', 'children'),
    Input('date-range-picker-demo1', 'value')
)
def date_range_picker_demo1(value):

    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo2-output', 'children'),
    Input('date-range-picker-demo2', 'value')
)
def date_range_picker_demo2(value):

    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo3-output', 'children'),
    Input('date-range-picker-demo3', 'value')
)
def date_range_picker_demo3(value):

    return f'value: {value}'
