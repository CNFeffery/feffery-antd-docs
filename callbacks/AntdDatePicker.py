import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('date-picker-demo-output', 'children'),
    Input('date-picker-demo', 'selectedDate'),
    prevent_initial_call=True
)
def date_picker_callback_demo(selectedDate):
    import time;time.sleep(0.5)
    if selectedDate:
        return selectedDate

    return dash.no_update
