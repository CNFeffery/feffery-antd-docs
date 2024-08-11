import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCheckbox(label='选择框', readOnly=True),
            fac.AntdCheckbox(label='选择框', checked=True, readOnly=True),
            fac.AntdCheckbox(label='选择框', indeterminate=True, readOnly=True),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCheckbox(label='选择框', readOnly=True),
        fac.AntdCheckbox(label='选择框', checked=True, readOnly=True),
        fac.AntdCheckbox(label='选择框', indeterminate=True, readOnly=True),
    ]
)
"""
    }
]
