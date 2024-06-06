import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSelect(
        options=[
            {'label': f'选项{i}', 'value': f'选项{i}'} for i in range(1, 6)
        ],
        style={'width': 350},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSelect(
    options=[
        {'label': f'选项{i}', 'value': f'选项{i}'} for i in range(1, 6)
    ],
    style={'width': 350},
)
"""
    }
]
