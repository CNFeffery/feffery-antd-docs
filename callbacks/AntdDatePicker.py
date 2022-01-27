import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('date-picker-demo-output', 'children'),
    Input('date-picker-demo', 'value'),
    prevent_initial_call=True
)
def date_picker_callback_demo(value):
     
    if value:
        return value

    return dash.no_update
