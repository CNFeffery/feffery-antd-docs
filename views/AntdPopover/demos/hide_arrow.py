import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPopover(
        fac.AntdButton('锚点元素'),
        title='气泡卡片示例',
        content='内容示例',
        arrow='hide',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdPopover(
    fac.AntdButton('锚点元素'),
    title='气泡卡片示例',
    content='内容示例',
    arrow='hide',
)
"""
    }
]
