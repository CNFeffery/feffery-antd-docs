import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdMenu(
        menuItems=[
            {
                'component': 'SubMenu',
                'props': {'key': f'{sub_menu}', 'title': f'子菜单{sub_menu}'},
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

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdMenu(
    menuItems=[
        {
            'component': 'SubMenu',
            'props': {'key': f'{sub_menu}', 'title': f'子菜单{sub_menu}'},
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
