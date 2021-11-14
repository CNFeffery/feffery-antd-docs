import dash
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('drawer-demo-1', 'visible'),
    Input('drawer-demo-trigger-1', 'nClicks'),
    prevent_initial_call=True
)
def drawer_demo_callback1(nClicks):
    return True


@app.callback(
    [Output('drawer-demo-2-top', 'visible'),
     Output('drawer-demo-2-left', 'visible'),
     Output('drawer-demo-2-bottom', 'visible')],
    [Input('drawer-demo-trigger-2-top', 'nClicks'),
     Input('drawer-demo-trigger-2-left', 'nClicks'),
     Input('drawer-demo-trigger-2-bottom', 'nClicks')],
    prevent_initial_call=True
)
def drawer_demo_callback2(_, __, ___):
    ctx = dash.callback_context

    placement = ctx.triggered[0]['prop_id'].split('.')[0].split('-')[-1]

    if placement == 'top':
        return True, False, False

    elif placement == 'left':
        return False, True, False

    else:
        return False, False, True
