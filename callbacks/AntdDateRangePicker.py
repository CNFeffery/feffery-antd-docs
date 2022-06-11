import dash
from datetime import datetime, timedelta
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('date-range-picker-demo-output', 'children'),
    Input('date-range-picker-demo', 'value'),
    prevent_initial_call=True
)
def date_picker_callback_demo(value):
    if value:
        return f'{value[0]} ~ {value[1]}'

    return dash.no_update


@app.callback(
    Output('date-range-picker-disabled-demo', 'disabledDatesStrategy'),
    Input('url', 'pathname')
)
def date_range_picker_disabled_callback_demo(pathname):
    return [
        {
            'mode': 'in-enumerate-dates',
            'value': [
                (datetime.now() + timedelta(days=day)).strftime('%Y-%m-%d')
                for day in range(7)
            ]
        }
    ]
