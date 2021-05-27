import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('date-range-picker-demo-output', 'children'),
    [Input('date-range-picker-demo', 'selectedStartDate'),
    Input('date-range-picker-demo', 'selectedEndDate')],
    prevent_initial_call=True
)
def date_picker_callback_demo(selectedStartDate, selectedEndDate):
    import time;time.sleep(0.5)
    if selectedStartDate and selectedEndDate:
        return f'{selectedStartDate} ~ {selectedEndDate}'

    return dash.no_update
