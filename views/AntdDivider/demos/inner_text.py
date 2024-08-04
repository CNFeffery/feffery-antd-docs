import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        # 默认居中
        fac.AntdDivider('AntdDivider'),
        # 左对齐
        fac.AntdDivider('AntdDivider', innerTextOrientation='left'),
        # 右对齐且设置内嵌文字样式
        fac.AntdDivider(
            'AntdDivider', innerTextOrientation='right', fontStyle='oblique'
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    # 默认居中
    fac.AntdDivider('AntdDivider'),
    # 左对齐
    fac.AntdDivider('AntdDivider', innerTextOrientation='left'),
    # 右对齐且设置内嵌文字样式
    fac.AntdDivider(
        'AntdDivider', innerTextOrientation='right', fontStyle='oblique'
    ),
]
"""
    }
]
