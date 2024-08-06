import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发全局提示', id='message-basic-demo-new', type='primary'
        ),
        html.Div(id='message-basic-demo'),
    ]

    return demo_contents


@app.callback(
    Output('message-basic-demo', 'children'),
    Input('message-basic-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_basic_demo(nClicks):
    return fac.AntdMessage(content='Hello, feffery-antd-components!', type='info')


code_string = [
    {
        'code': """
fac.AntdButton(
    '触发全局提示', id='message-basic-demo-new', type='primary'
),
html.Div(id='message-basic-demo'),

...

@app.callback(
    Output('message-basic-demo', 'children'),
    Input('message-basic-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_basic_demo(nClicks):
    return fac.AntdMessage(content='Hello, feffery-antd-components!', type='info')
"""
    }
]
