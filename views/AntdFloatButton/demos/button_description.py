import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFloatButton(description='描述信息'),
        fac.AntdFloatButton(
            description='描述信息', shape='square', style={'right': 84}
        ),
        fac.AntdFloatButton(
            description='描述信息',
            shape='square',
            type='primary',
            icon=fac.AntdIcon(icon='antd-question'),
            style={'right': 144},
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdFloatButton(description='描述信息'),
    fac.AntdFloatButton(
        description='描述信息', shape='square', style={'right': 84}
    ),
    fac.AntdFloatButton(
        description='描述信息',
        shape='square',
        type='primary',
        icon=fac.AntdIcon(icon='antd-question'),
        style={'right': 144},
    ),
]
"""
    }
]
