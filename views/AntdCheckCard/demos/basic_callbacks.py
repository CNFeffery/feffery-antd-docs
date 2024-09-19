import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdCheckCard(
                fac.AntdText('选择卡片示例' * 10),
                id='check-card-demo',
                defaultChecked=False,
            ),
            fac.AntdParagraph(id='check-card-demo-output'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdCheckCard(
                fac.AntdText('Demo' * 20),
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdCheckCard(
        fac.AntdText('Demo' * 20),
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
