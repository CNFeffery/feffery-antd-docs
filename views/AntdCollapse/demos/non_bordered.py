import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCollapse(
        fac.AntdParagraph('内容示例' * 20),
        bordered=False,
        title='折叠面板示例',
        style={'width': 300},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdCollapse(
    fac.AntdParagraph('内容示例' * 20),
    bordered=False,
    title='折叠面板示例',
    style={'width': 300},
)
"""
    }
]
