import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdSpace(
            [
                fac.AntdCheckbox(id='checkbox-demo', label='开启'),
                fac.AntdText(id='checkbox-demo-output'),
            ]
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdCheckbox(id='checkbox-demo', label='Enable'),
                fac.AntdText(id='checkbox-demo-output'),
            ]
        )

    return demo_contents


@app.callback(
    Output('checkbox-demo-output', 'children'),
    Input('checkbox-demo', 'checked'),
)
def checkbox_demo(checked):
    return f'checked: {checked}'


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdCheckbox(id='checkbox-demo', label='开启'),
        fac.AntdText(id='checkbox-demo-output'),
    ]
)

...

@app.callback(
    Output('checkbox-demo-output', 'children'),
    Input('checkbox-demo', 'checked'),
)
def checkbox_demo(checked):
    return f'checked: {checked}'
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdCheckbox(id='checkbox-demo', label='Enable'),
        fac.AntdText(id='checkbox-demo-output'),
    ]
)

...

@app.callback(
    Output('checkbox-demo-output', 'children'),
    Input('checkbox-demo', 'checked'),
)
def checkbox_demo(checked):
    return f'checked: {checked}'
"""
            }
        ]
