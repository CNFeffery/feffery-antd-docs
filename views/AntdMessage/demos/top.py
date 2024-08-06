import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发距离顶端200px全局提示',
            id='message-top-demo-new',
            type='primary',
        ),
        html.Div(id='message-top-demo'),
    ]

    return demo_contents


@app.callback(
    Output('message-top-demo', 'children'),
    Input('message-top-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_top_demo(nClicks):
    return fac.AntdMessage(content='全局提示示例', top=200, type='success')


code_string = [
    {
        'code': """
fac.AntdButton(
    '触发距离顶端200px全局提示',
    id='message-top-demo-new',
    type='primary',
),
html.Div(id='message-top-demo'),

...

@app.callback(
    Output('message-top-demo', 'children'),
    Input('message-top-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_top_demo(nClicks):
    return fac.AntdMessage(content='全局提示示例', top=200, type='success')
"""
    }
]
