from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('table-demo-output1', 'children'),
     Output('table-demo-output2', 'children')],
    [Input('table-demo', 'currentData'),
     Input('table-demo', 'recentlyChangedRow')],
    prevent_initial_call=True
)
def date_picker_callback_demo(currentData, recentlyChangedRow):
    import time
    time.sleep(0.5)

    return str(currentData), str(recentlyChangedRow)
