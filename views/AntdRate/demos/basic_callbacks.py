import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdRate(id='rate-demo', count=10, allowHalf=True, defaultValue=1),
        fac.AntdParagraph(id='rate-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('rate-demo-output', 'children'), Input('rate-demo', 'value')
)
def rate_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdRate(
    id='rate-demo',
    count=10,
    allowHalf=True,
    defaultValue=1
),

fac.AntdParagraph(
    id='rate-demo-output'
)

...

@app.callback(
    Output('rate-demo-output', 'children'),
    Input('rate-demo', 'value')
)
def rate_demo(value):

    return f'value: {value}'
"""
    }
]
