import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCheckbox(id='checkbox-demo', label='开启'),
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


code_string = [
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
