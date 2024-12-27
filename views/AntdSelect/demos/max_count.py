import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSelect(
        options=[f'选项{i}' for i in range(1, 6)],
        mode='multiple',
        maxCount=2,
        style={'width': 350},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSelect(
    options=[f'选项{i}' for i in range(1, 6)],
    mode='multiple',
    maxCount=2,
    style={'width': 350},
)
"""
    }
]
