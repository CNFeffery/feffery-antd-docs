import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发10s全局通知提醒',
            id='notification-duration-demo-new',
            type='primary',
        ),
        html.Div(id='notification-duration-demo'),
    ]

    return demo_contents


@app.callback(
    Output('notification-duration-demo', 'children'),
    Input('notification-duration-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def notification_duration_demo(nClicks):
    return fac.AntdNotification(
        message='通知延时',
        description='这是一条成功通知消息，将在10s后自动消失',
        duration=10,
        type='success',
    )


code_string = [
    {
        'code': """
fac.AntdButton(
    '触发10s全局通知提醒',
    id='notification-duration-demo-new',
    type='primary',
),
html.Div(id='notification-duration-demo'),

...

@app.callback(
    Output('notification-duration-demo', 'children'),
    Input('notification-duration-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def notification_duration_demo(nClicks):
    return fac.AntdNotification(
        message='通知延时',
        description='这是一条成功通知消息，将在10s后自动消失',
        duration=10,
        type='success',
    )
"""
    }
]
