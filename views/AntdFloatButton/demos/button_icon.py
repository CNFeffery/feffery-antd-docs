import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-question')),
        fac.AntdFloatButton(
            type='primary',
            icon=fac.AntdIcon(icon='antd-bulb'),
            style={'right': 84},
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-question')),
    fac.AntdFloatButton(
        type='primary',
        icon=fac.AntdIcon(icon='antd-bulb'),
        style={'right': 84},
    ),
]
"""
    }
]
