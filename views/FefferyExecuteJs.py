from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('execute-js-demo-output', 'jsString'),
    Input('execute-js-demo', 'nClicks'),
    prevent_initial_call=True
)
def execute_js_demo(nClicks):

    return 'alert("FefferyExecuteJs示例");'
