import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDropdown(
                    title='触发点',
                    buttonMode=True,
                    menuItems=[
                        {'title': '子页面1'},
                        {'title': '子页面2'},
                        {'isDivider': True},
                        {'title': '子页面3-1'},
                        {'title': '子页面3-2'},
                    ],
                ),
                fac.AntdDropdown(
                    title='触发点',
                    buttonMode=True,
                    buttonProps={'size': 'large', 'type': 'dashed'},
                    menuItems=[
                        {'title': '子页面1'},
                        {'title': '子页面2'},
                        {'isDivider': True},
                        {'title': '子页面3-1'},
                        {'title': '子页面3-2'},
                    ],
                ),
                fac.AntdDropdown(
                    title='触发点',
                    buttonMode=True,
                    buttonProps={
                        'size': 'small',
                        'type': 'primary',
                        'danger': True,
                    },
                    menuItems=[
                        {'title': '子页面1'},
                        {'title': '子页面2'},
                        {'isDivider': True},
                        {'title': '子页面3-1'},
                        {'title': '子页面3-2'},
                    ],
                ),
            ]
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDropdown(
                    title='Trigger point',
                    buttonMode=True,
                    menuItems=[
                        {'title': 'Subpage1'},
                        {'title': 'Subpage2'},
                        {'isDivider': True},
                        {'title': 'Subpage3-1'},
                        {'title': 'Subpage3-2'},
                    ],
                ),
                fac.AntdDropdown(
                    title='Trigger point',
                    buttonMode=True,
                    buttonProps={'size': 'large', 'type': 'dashed'},
                    menuItems=[
                        {'title': 'Subpage1'},
                        {'title': 'Subpage2'},
                        {'isDivider': True},
                        {'title': 'Subpage3-1'},
                        {'title': 'Subpage3-2'},
                    ],
                ),
                fac.AntdDropdown(
                    title='Trigger point',
                    buttonMode=True,
                    buttonProps={
                        'size': 'small',
                        'type': 'primary',
                        'danger': True,
                    },
                    menuItems=[
                        {'title': 'Subpage1'},
                        {'title': 'Subpage2'},
                        {'isDivider': True},
                        {'title': 'Subpage3-1'},
                        {'title': 'Subpage3-2'},
                    ],
                ),
            ]
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            menuItems=[
                {'title': '子页面1'},
                {'title': '子页面2'},
                {'isDivider': True},
                {'title': '子页面3-1'},
                {'title': '子页面3-2'},
            ],
        ),
        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            buttonProps={'size': 'large', 'type': 'dashed'},
            menuItems=[
                {'title': '子页面1'},
                {'title': '子页面2'},
                {'isDivider': True},
                {'title': '子页面3-1'},
                {'title': '子页面3-2'},
            ],
        ),
        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            buttonProps={
                'size': 'small',
                'type': 'primary',
                'danger': True,
            },
            menuItems=[
                {'title': '子页面1'},
                {'title': '子页面2'},
                {'isDivider': True},
                {'title': '子页面3-1'},
                {'title': '子页面3-2'},
            ],
        ),
    ]
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdDropdown(
            title='Trigger point',
            buttonMode=True,
            menuItems=[
                {'title': 'Subpage1'},
                {'title': 'Subpage2'},
                {'isDivider': True},
                {'title': 'Subpage3-1'},
                {'title': 'Subpage3-2'},
            ],
        ),
        fac.AntdDropdown(
            title='Trigger point',
            buttonMode=True,
            buttonProps={'size': 'large', 'type': 'dashed'},
            menuItems=[
                {'title': 'Subpage1'},
                {'title': 'Subpage2'},
                {'isDivider': True},
                {'title': 'Subpage3-1'},
                {'title': 'Subpage3-2'},
            ],
        ),
        fac.AntdDropdown(
            title='Trigger point',
            buttonMode=True,
            buttonProps={
                'size': 'small',
                'type': 'primary',
                'danger': True,
            },
            menuItems=[
                {'title': 'Subpage1'},
                {'title': 'Subpage2'},
                {'isDivider': True},
                {'title': 'Subpage3-1'},
                {'title': 'Subpage3-2'},
            ],
        ),
    ]
)
"""
            }
        ]
