from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('drawer-basic-demo', 'visible'),
    Input('drawer-basic-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_basic_demo(nCLicks):

    return True


@app.callback(
    [Output('drawer-placement-demo', 'title'),
     Output('drawer-placement-demo', 'placement')],
    Input('drawer-placement-demo-placement', 'value')
)
def update_drawer_placement_and_title_dmeo(value):

    return [
        f'placement="{value}"',
        value
    ]


@app.callback(
    Output('drawer-placement-demo', 'visible'),
    Input('drawer-placement-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def draw_placement_demo(nClicks):

    return True

@app.callback(
    Output('drawer-footer-demo', 'visible'),
    Input('drawer-footer-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_footer_demo(nClicks):

    return True

@app.callback(
    Output('drawer-extra-demo', 'visible'),
    Input('drawer-extra-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_extra_demo(nClicks):

    return True


@app.callback(
    Output('drawer-local-demo', 'visible'),
    Input('drawer-local-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_local_demo(nClicks):

    return True


@app.callback(
    Output('drawer-free-local-demo', 'visible'),
    Input('drawer-free-local-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_free_local_demo(nClicks):

    return True