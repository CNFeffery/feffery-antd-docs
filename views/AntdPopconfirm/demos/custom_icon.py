import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPopconfirm(
        fac.AntdButton('触发'), title='确认继续', icon='🤔'
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdPopconfirm(
    fac.AntdButton('触发'), title='确认继续', icon='🤔'
)
"""
    }
]
