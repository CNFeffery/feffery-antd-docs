import dash_html_components as html
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('transfer-demo-output', 'children'),
    [Input('transfer-demo', 'targetKeys'),
     Input('transfer-demo', 'moveDirection'),
     Input('transfer-demo', 'moveKeys')],
    prevent_initial_call=True
)
def transfer_callback_demo(targetKeys, moveDirection, moveKeys):
    import time;time.sleep(0.5)
    return [
        f'targetKeys: {targetKeys}',
        html.Br(),
        f'moveDirection: {moveDirection}',
        html.Br(),
        f'moveKeys: {moveKeys}'
    ]
