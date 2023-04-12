import dash
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('sider-custom-trigger-demo', 'collapsed'),
    Input('sider-custom-trigger-button-demo', 'nClicks'),
    State('sider-custom-trigger-demo', 'collapsed'),
    prevent_initial_call=True
)
def sider_custom_trigger_demo(nClicks, collapsed):
    if nClicks:
        return not collapsed

    return dash.no_update
