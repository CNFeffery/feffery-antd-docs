import dash
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
