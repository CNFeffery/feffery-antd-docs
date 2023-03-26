import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('notification-basic-demo', 'children'),
    Input('notification-basic-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def notification_basic_demo(nClicks):

    return fac.AntdNotification(
        message='通知提醒框示例',
        description='内容示例'
    )


@app.callback(
    Output('notification-placement-demo', 'children'),
    Input('notification-placement-demo-new', 'nClicks'),
    State('notification-placement-demo-placement', 'value'),
    prevent_initial_call=True
)
def notification_placement_demo(nClicks, value):

    return fac.AntdNotification(
        message='通知提醒框示例',
        description='内容示例',
        placement=value
    )


@app.callback(
    Output('notification-type-demo', 'children'),
    Input('notification-type-demo-new', 'nClicks'),
    State('notification-type-demo-type', 'value'),
    prevent_initial_call=True
)
def notification_type_demo(nClicks, value):

    return fac.AntdNotification(
        message='通知提醒框示例',
        description='内容示例',
        type=value
    )
