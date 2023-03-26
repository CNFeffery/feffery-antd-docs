import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('message-basic-demo', 'children'),
    Input('message-basic-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_basic_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        type='success'
    )


@app.callback(
    Output('message-type-demo', 'children'),
    Input('message-type-demo-new', 'nClicks'),
    State('message-type-demo-type', 'value'),
    prevent_initial_call=True
)
def message_type_demo(nClicks, value):

    return fac.AntdMessage(
        content='全局提示示例',
        type=value
    )


@app.callback(
    Output('message-duration-demo', 'children'),
    Input('message-duration-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_duration_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        duration=10,
        type='success'
    )


@app.callback(
    Output('message-top-demo', 'children'),
    Input('message-top-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_top_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        top=200,
        type='success'
    )


@app.callback(
    Output('message-max-count-demo', 'children'),
    Input('message-max-count-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_max_count_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        type='success',
        maxCount=3
    )
