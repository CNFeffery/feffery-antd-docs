import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            # default
            fac.AntdDivider('AntdDivider'),
            # left
            fac.AntdDivider('AntdDivider', innerTextOrientation='left'),
            # right
            fac.AntdDivider(
                'AntdDivider', innerTextOrientation='right', fontStyle='oblique'
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    # default
    fac.AntdDivider('AntdDivider'),
    # left
    fac.AntdDivider('AntdDivider', innerTextOrientation='left'),
    # right
    fac.AntdDivider(
        'AntdDivider', innerTextOrientation='right', fontStyle='oblique'
    ),
]
"""
            }
        ]
