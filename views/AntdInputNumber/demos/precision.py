import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdInputNumber(
        precision=5, placeholder='precision=5', style={'width': 150}
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdInputNumber(
    precision=5, placeholder='precision=5', style={'width': 150}
)
"""
    }
]
