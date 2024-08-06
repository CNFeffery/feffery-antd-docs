import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发10s全局提示', id='message-duration-demo-new', type='primary'
        ),
        html.Div(id='message-duration-demo'),
    ]

    return demo_contents


@app.callback(
    Output('message-duration-demo', 'children'),
    Input('message-duration-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_duration_demo(nClicks):
    return fac.AntdMessage(
        content='这是一条成功提示消息，将在10s后自动消失',
        duration=10,
        type='success',
    )


code_string = [
    {
        'code': """
fac.AntdButton(
        '触发10s全局提示', id='message-duration-demo-new', type='primary'
    ),
    html.Div(id='message-duration-demo'),
]

...

@app.callback(
    Output('message-duration-demo', 'children'),
    Input('message-duration-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_duration_demo(nClicks):
    return fac.AntdMessage(
        content='这是一条成功提示消息，将在10s后自动消失',
        duration=10,
        type='success',
    )
"""
    }
]
