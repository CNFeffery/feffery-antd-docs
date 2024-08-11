import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTooltip(
        fac.AntdButton('锚点示例'),
        title='内容示例' * 50,
        overlayStyle={'width': 250},
        overlayInnerStyle={'maxHeight': 150, 'overflowY': 'auto'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTooltip(
    fac.AntdButton('锚点示例'),
    title='内容示例' * 50,
    overlayStyle={'width': 250},
    overlayInnerStyle={'maxHeight': 150, 'overflowY': 'auto'},
)
"""
    }
]
