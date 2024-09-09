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
                    'props': {'key': '子菜单1', 'title': '子菜单1'},
                    'children': [
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '子菜单1-1',
                                'title': '子菜单1-1',
                            },
                            'children': [
                                {
                                    'component': 'SubMenu',
                                    'props': {
                                        'key': '子菜单1-1-1',
                                        'title': '子菜单1-1-1',
                                    },
                                    'children': [
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': '菜单项示例',
                                                'title': '菜单项示例',
                                            },
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
            defaultOpenKeys=['子菜单1', '子菜单1-1', '子菜单1-1-1'],
            mode='inline',
            inlineIndent=50,
            style={'width': 300},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdMenu(
            menuItems=[
                {
                    'component': 'SubMenu',
                    'props': {'key': 'SubMenu1', 'title': 'SubMenu1'},
                    'children': [
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': 'SubMenu1-1',
                                'title': 'SubMenu1-1',
                            },
                            'children': [
                                {
                                    'component': 'SubMenu',
                                    'props': {
                                        'key': 'SubMenu1-1-1',
                                        'title': 'SubMenu1-1-1',
                                    },
                                    'children': [
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': 'Item1',
                                                'title': 'Item1',
                                            },
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ],
            defaultOpenKeys=['SubMenu1', 'SubMenu1-1', 'SubMenu1-1-1'],
            mode='inline',
            inlineIndent=50,
            style={'width': 300},
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
            'props': {'key': '子菜单1', 'title': '子菜单1'},
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': '子菜单1-1',
                        'title': '子菜单1-1',
                    },
                    'children': [
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': '子菜单1-1-1',
                                'title': '子菜单1-1-1',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': '菜单项示例',
                                        'title': '菜单项示例',
                                    },
                                }
                            ],
                        }
                    ],
                }
            ],
        }
    ],
    defaultOpenKeys=['子菜单1', '子菜单1-1', '子菜单1-1-1'],
    mode='inline',
    inlineIndent=50,
    style={'width': 300},
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
            'props': {'key': 'SubMenu1', 'title': 'SubMenu1'},
            'children': [
                {
                    'component': 'SubMenu',
                    'props': {
                        'key': 'SubMenu1-1',
                        'title': 'SubMenu1-1',
                    },
                    'children': [
                        {
                            'component': 'SubMenu',
                            'props': {
                                'key': 'SubMenu1-1-1',
                                'title': 'SubMenu1-1-1',
                            },
                            'children': [
                                {
                                    'component': 'Item',
                                    'props': {
                                        'key': 'Item1',
                                        'title': 'Item1',
                                    },
                                }
                            ],
                        }
                    ],
                }
            ],
        }
    ],
    defaultOpenKeys=['SubMenu1', 'SubMenu1-1', 'SubMenu1-1-1'],
    mode='inline',
    inlineIndent=50,
    style={'width': 300},
)
"""
            }
        ]
