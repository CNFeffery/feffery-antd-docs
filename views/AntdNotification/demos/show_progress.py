import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发通知提醒框',
            id='notification-show-progress-demo-new',
            type='primary',
        ),
        html.Div(id='notification-show-progress-demo'),
    ]

    return demo_contents


@app.callback(
    Output('notification-show-progress-demo', 'children'),
    Input('notification-show-progress-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def notification_show_progress_demo(nClicks):
    return fac.AntdNotification(
        message='Notification Title',
        description='Hello, feffery-antd-components!',
        showProgress=True,
    )


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发通知提醒框',
        id='notification-show-progress-demo-new',
        type='primary',
    ),
    html.Div(id='notification-show-progress-demo'),
]

...

@app.callback(
    Output('notification-show-progress-demo', 'children'),
    Input('notification-show-progress-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def notification_show_progress_demo(nClicks):
    return fac.AntdNotification(
        message='Notification Title',
        description='Hello, feffery-antd-components!',
        showProgress=True,
    )
"""
    }
]
