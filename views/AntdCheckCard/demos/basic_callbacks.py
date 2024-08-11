import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdCheckCard(
            fac.AntdText('选择卡片示例' * 10),
            id='check-card-demo',
            defaultChecked=False,
        ),
        fac.AntdParagraph(id='check-card-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('check-card-demo-output', 'children'),
    Input('check-card-demo', 'checked'),
)
def check_card_demo(checked):
    return f'checked: {checked}'


code_string = [
    {
        'code': """
[
    fac.AntdCheckCard(
        fac.AntdText('选择卡片示例' * 10),
        id='check-card-demo',
        defaultChecked=False,
    ),
    fac.AntdParagraph(id='check-card-demo-output'),
]

...

@app.callback(
    Output('check-card-demo-output', 'children'),
    Input('check-card-demo', 'checked'),
)
def check_card_demo(checked):
    return f'checked: {checked}'
"""
    }
]
