import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdDropdown(
            title='触发点',
            menuItems=[
                {'title': '选项1'},
                {'title': '选项2'},
                {'isDivider': True},
                {'title': '选项3-1'},
                {'title': '选项3-2'},
            ],
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdDropdown(
            title='Trigger point',
            menuItems=[
                {'title': 'Option1'},
                {'title': 'Option2'},
                {'isDivider': True},
                {'title': 'Option3-1'},
                {'title': 'Option3-2'},
            ],
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdDropdown(
    title='触发点',
    menuItems=[
        {'title': '选项1'},
        {'title': '选项2'},
        {'isDivider': True},
        {'title': '选项3-1'},
        {'title': '选项3-2'},
    ],
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdDropdown(
    title='Trigger point',
    menuItems=[
        {'title': 'Option1'},
        {'title': 'Option2'},
        {'isDivider': True},
        {'title': 'Option3-1'},
        {'title': 'Option3-2'},
    ],
)
"""
            }
        ]
