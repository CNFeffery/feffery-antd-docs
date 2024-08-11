import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [fac.AntdButton('子元素', type='primary')] * 25,
        gap='small',
        wrap='wrap',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdFlex(
    [fac.AntdButton('子元素', type='primary')] * 25,
    gap='small',
    wrap='wrap',
)
"""
    }
]
