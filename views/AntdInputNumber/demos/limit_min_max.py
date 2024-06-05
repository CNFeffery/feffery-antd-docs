import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdInputNumber(
        min=0,
        max=100,
        placeholder='请尝试输入0~100以外的数值查看效果',
        style={'width': 275},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdInputNumber(
    min=0,
    max=100,
    placeholder='请尝试输入0~100以外的数值查看效果',
    style={'width': 275},
)
"""
    }
]
