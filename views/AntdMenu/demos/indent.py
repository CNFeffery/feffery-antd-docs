import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


code_string = [
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
