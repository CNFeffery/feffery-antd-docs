import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdButton(
        'fac文档首页', type='primary', href='/', target='_blank'
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdButton(
    'fac文档首页', type='primary', href='/', target='_blank'
)
"""
    }
]
