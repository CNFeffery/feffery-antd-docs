import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('plain=False', plain=False),
        fac.AntdDivider('plain=True'),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    return [
        {
            'code': """
[
    fac.AntdDivider('plain=False', plain=False),
    fac.AntdDivider('plain=True'),
]
"""
        }
    ]
