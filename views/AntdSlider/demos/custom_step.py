import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSlider(
        min=0, max=100, defaultValue=50, step=10, style={'width': 300}
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=50,
    step=10,
    style={
        'width': 300
    }
)
"""
    }
]
