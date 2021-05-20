from dash.dependencies import Input, Output

from server import app

@app.callback(
    Output('date-picker-demo-output', 'children'),
    Input('date-picker-demo', 'selectedDate')
)
def date_picker_callback_demo(selectedDate):
    if selectedDate:
        return selectedDate

    return ''