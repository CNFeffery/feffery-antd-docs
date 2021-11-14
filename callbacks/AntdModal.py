import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('modal-demo-1', 'visible'),
    Input('modal-demo-trigger-1', 'nClicks'),
    prevent_initial_call=True
)
def modal_demo_callback1(nClicks):
    return True


@app.callback(
    Output('modal-demo-2', 'visible'),
    Input('modal-demo-trigger-2', 'nClicks'),
    prevent_initial_call=True
)
def modal_demo_callback2(nClicks):
    return True


@app.callback(
    [Output('modal-demo-2-output-1', 'children'),
     Output('modal-demo-2-output-2', 'children'),
     Output('modal-demo-2-output-3', 'children')],
    [Input('modal-demo-2', 'okCounts'),
     Input('modal-demo-2', 'cancelCounts'),
     Input('modal-demo-2', 'closeCounts')],
    prevent_initial_call=True
)
def modal_demo_callback3(okCounts, cancelCounts, closeCounts):
    return [str(okCounts), str(cancelCounts), str(closeCounts)]
