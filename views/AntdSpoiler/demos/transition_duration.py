import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpoiler(
        fac.AntdParagraph('内容示例' * 100),
        maxHeight=70,
        transitionDuration=0.5,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpoiler(
    fac.AntdParagraph('内容示例' * 100),
    maxHeight=70,
    transitionDuration=0.5,
)
"""
    }
]
