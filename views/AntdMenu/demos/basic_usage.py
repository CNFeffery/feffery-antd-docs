import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdMenu(
            menuItems=[
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': f'{sub_menu}',
                        'title': f'子菜单{sub_menu}',
                    },
                    'children': [
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': f'{sub_menu}-{item_group}',
                                'title': f'菜单项分组{sub_menu}-{item_group}',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': f'{sub_menu}-{item_group}-{item}',
                                        'title': f'菜单项{sub_menu}-{item_group}-{item}',
                                    },
                                }
                                for item in range(1, 3)
                            ],
                        }
                        for item_group in range(1, 3)
                    ],
                }
                for sub_menu in range(1, 5)
            ],
            style={'width': 256},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdMenu(
            menuItems=[
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': f'{sub_menu}',
                        'title': f'SubMenu{sub_menu}',
                    },
                    'children': [
                        {
                            'component': 'ItemGroup',
                            'props': {
                                'key': f'{sub_menu}-{item_group}',
                                'title': f'ItemGroup{sub_menu}-{item_group}',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': f'{sub_menu}-{item_group}-{item}',
                                        'title': f'Item{sub_menu}-{item_group}-{item}',
                                    },
                                }
                                for item in range(1, 3)
                            ],
                        }
                        for item_group in range(1, 3)
                    ],
                }
                for sub_menu in range(1, 5)
            ],
            style={'width': 256},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdMenu(
    menuItems=[
        {
            'component': 'SubMenu',
            'props': {
                'key': f'{sub_menu}',
                'title': f'子菜单{sub_menu}',
            },
            'children': [
                {
                    'component': 'ItemGroup',
                    'props': {
                        'key': f'{sub_menu}-{item_group}',
                        'title': f'菜单项分组{sub_menu}-{item_group}',
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': f'{sub_menu}-{item_group}-{item}',
                                'title': f'菜单项{sub_menu}-{item_group}-{item}',
                            },
                        }
                        for item in range(1, 3)
                    ],
                }
                for item_group in range(1, 3)
            ],
        }
        for sub_menu in range(1, 5)
    ],
    style={'width': 256},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdMenu(
    menuItems=[
        {
            'component': 'SubMenu',
            'props': {
                'key': f'{sub_menu}',
                'title': f'SubMenu{sub_menu}',
            },
            'children': [
                {
                    'component': 'ItemGroup',
                    'props': {
                        'key': f'{sub_menu}-{item_group}',
                        'title': f'ItemGroup{sub_menu}-{item_group}',
                    },
                    'children': [
                        {
                            'component': 'Item',
                            'props': {
                                'key': f'{sub_menu}-{item_group}-{item}',
                                'title': f'Item{sub_menu}-{item_group}-{item}',
                            },
                        }
                        for item in range(1, 3)
                    ],
                }
                for item_group in range(1, 3)
            ],
        }
        for sub_menu in range(1, 5)
    ],
    style={'width': 256},
)
"""
            }
        ]
