from datetime import datetime, timedelta
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('date-picker-demo1-output', 'children'),
    Input('date-picker-demo1', 'value')
)
def date_picker_demo1(value):

    return f'value: {value}'


@app.callback(
    Output('date-picker-demo2-output', 'children'),
    Input('date-picker-demo2', 'value')
)
def date_picker_demo2(value):

    return f'value: {value}'


@app.callback(
    Output('date-picker-demo3-output', 'children'),
    Input('date-picker-demo3', 'value')
)
def date_picker_demo3(value):

    return f'value: {value}'


@app.callback(
    Output('date-picker-dynamic-forbidden-demo', 'disabledDatesStrategy'),
    Input('url', 'pathname')
)
def date_picker_dynamic_forbidden_demo(_):

    return [
        {
            'mode': 'lt',
            'target': 'specific-date',
            'value': datetime.now().strftime('%Y-%m-%d')
        },
        {
            'mode': 'gt',
            'target': 'specific-date',
            'value': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        }
    ]
