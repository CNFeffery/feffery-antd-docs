import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发全局提示', id='message-max-count-demo-new', type='primary'
        ),
        html.Div(id='message-max-count-demo'),
    ]

    return demo_contents


@app.callback(
    Output('message-max-count-demo', 'children'),
    Input('message-max-count-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_max_count_demo(nClicks):
    return fac.AntdMessage(content='全局提示示例', type='success', maxCount=3)


code_string = [
    {
        'code': """
fac.AntdButton(
    '触发全局提示', id='message-max-count-demo-new', type='primary'
),
html.Div(id='message-max-count-demo'),

...

@app.callback(
    Output('message-max-count-demo', 'children'),
    Input('message-max-count-demo-new', 'nClicks'),
    prevent_initial_call=True,
)
def message_max_count_demo(nClicks):
    return fac.AntdMessage(content='全局提示示例', type='success', maxCount=3)
"""
    }
]
