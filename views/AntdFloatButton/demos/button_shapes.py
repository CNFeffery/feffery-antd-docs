import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFloatButton(type='primary'),
        fac.AntdFloatButton(
            type='primary', shape='square', style={'right': 84}
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdFloatButton(type='primary'),
    fac.AntdFloatButton(
        type='primary', shape='square', style={'right': 84}
    ),
]
"""
    }
]
