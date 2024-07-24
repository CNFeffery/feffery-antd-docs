import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTooltip(
        fac.AntdButton('锚点元素'), title='信息提示示例', arrow='hide'
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTooltip(
    fac.AntdButton('锚点元素'), title='信息提示示例', arrow='hide'
)
"""
    }
]
