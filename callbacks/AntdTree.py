from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('tree-demo-output1', 'children'),
    Output('tree-demo-output2', 'children')],
    [Input('tree-demo', 'selectedKeys'),
     Input('tree-demo', 'checkedKeys')],
    prevent_initial_call=True
)
def button_callback_demo(selectedKeys, checkedKeys):
    import time;time.sleep(1)

    return str(selectedKeys), str(checkedKeys)
