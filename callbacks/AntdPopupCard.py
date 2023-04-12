from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('popup-card-basic-demo', 'visible'),
    Input('popup-card-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_basic_demo(nClicks):

    return True


@app.callback(
    Output('popup-card-transition-type-demo', 'transitionType'),
    Input('popup-card-transition-type-demo-select', 'value')
)
def popup_card_transition_type_demo(value):

    return value


@app.callback(
    Output('popup-card-transition-type-demo', 'visible'),
    Input('popup-card-transition-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_transition_type_demo_visible(nClicks):

    return True


@app.callback(
    Output('popup-card-close-icon-type-demo', 'closeIconType'),
    Input('popup-card-close-icon-type-demo-select', 'value')
)
def popup_card_close_icon_type_demo(value):

    return value


@app.callback(
    Output('popup-card-close-icon-type-demo', 'visible'),
    Input('popup-card-close-icon-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_close_icon_type_demo_visible(nClicks):

    return True


@app.callback(
    Output('popup-card-draggable-demo', 'visible'),
    Input('popup-card-draggable-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_draggable_demo(nClicks):

    return True


@app.callback(
    Output('popup-card-custom-position-demo', 'visible'),
    Input('popup-card-custom-position-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_custom_position_demo(nClicks):

    return True
