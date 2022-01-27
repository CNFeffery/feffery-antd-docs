import dash
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    [Output('tabs-demo', 'children'),
     Output('tabs-demo', 'activeKey')],
    [Input('tabs-demo-add', 'nClicks'),
     Input('tabs-demo', 'latestDeletePane')],
    State('tabs-demo', 'children'),
    prevent_initial_call=True
)
def tabs_callback_demo(nClicks, latestDeletePane, children):

    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'] == 'tabs-demo-add.nClicks':
        return children + [
            fac.AntdTabPane(f'标签页{nClicks + 1}', tab=f'标签页{nClicks + 1}', key=f'标签页{nClicks + 1}')
        ], f'标签页{nClicks + 1}'

    elif ctx.triggered[0]['prop_id'] == 'tabs-demo.latestDeletePane':
        return [child for child in children if child['props']['key'] != latestDeletePane], '基础标签页'

    return dash.no_update
