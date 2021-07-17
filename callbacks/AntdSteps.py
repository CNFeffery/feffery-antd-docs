import dash
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('steps-demo', 'current'),
    [Input('steps-demo-go-next', 'nClicks'),
     Input('steps-demo-go-last', 'nClicks'),
     Input('steps-demo-restart', 'nClicks')],
    State('steps-demo', 'current'),
    prevent_initial_call=True
)
def steps_callback_demo_part1(go_next, go_last, restart, current):
    import time;time.sleep(0.5)
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'].startswith('steps-demo-go-next'):
        return current + 1

    elif ctx.triggered[0]['prop_id'].startswith('steps-demo-go-last'):
        return max(current - 1, 0)

    else:
        return 0


@app.callback(
    Output('steps-demo-current', 'children'),
    Input('steps-demo', 'current'),
    prevent_initial_call=True
)
def steps_callback_demo_part2(current):

    return f'当前步骤为：步骤{current}'
