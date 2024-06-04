import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRadioGroup(
        options=[{'label': f'选项{c}', 'value': c} for c in list('abcdef')],
        defaultValue='a',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRadioGroup(
    options=[
        {
            'label': f'选项{c}',
            'value': c
        }
        for c in list('abcdef')
    ],
    defaultValue='a'
)
"""
    }
]
