import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdMenu(
                id='menu-advanced-demo',
                currentKey='1-1-1',
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
                mode='horizontal',
            ),
            html.Pre(
                id='menu-advanced-demo-output',
                style={'maxHeight': 400, 'overflowY': 'auto'},
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdMenu(
                id='menu-advanced-demo',
                currentKey='1-1-1',
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
                mode='horizontal',
            ),
            html.Pre(
                id='menu-advanced-demo-output',
                style={'maxHeight': 400, 'overflowY': 'auto'},
            ),
        ]

    return demo_contents


@app.callback(
    Output('menu-advanced-demo-output', 'children'),
    [
        Input('menu-advanced-demo', 'currentItem'),
        Input('menu-advanced-demo', 'currentKeyPath'),
        Input('menu-advanced-demo', 'currentItemPath'),
    ],
)
def menu_advanced_callback_demo(currentItem, currentKeyPath, currentItemPath):
    return json.dumps(
        dict(
            currentItem=currentItem,
            currentKeyPath=currentKeyPath,
            currentItemPath=currentItemPath,
        ),
        indent=4,
        ensure_ascii=False,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdMenu(
        id='menu-advanced-demo',
        currentKey='1-1-1',
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
        mode='horizontal',
    ),
    html.Pre(
        id='menu-advanced-demo-output',
        style={'maxHeight': 400, 'overflowY': 'auto'},
    ),
]

...

@app.callback(
    Output('menu-advanced-demo-output', 'children'),
    [
        Input('menu-advanced-demo', 'currentItem'),
        Input('menu-advanced-demo', 'currentKeyPath'),
        Input('menu-advanced-demo', 'currentItemPath'),
    ],
)
def menu_advanced_callback_demo(currentItem, currentKeyPath, currentItemPath):
    return json.dumps(
        dict(
            currentItem=currentItem,
            currentKeyPath=currentKeyPath,
            currentItemPath=currentItemPath,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdMenu(
        id='menu-advanced-demo',
        currentKey='1-1-1',
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
        mode='horizontal',
    ),
    html.Pre(
        id='menu-advanced-demo-output',
        style={'maxHeight': 400, 'overflowY': 'auto'},
    ),
]

...

@app.callback(
    Output('menu-advanced-demo-output', 'children'),
    [
        Input('menu-advanced-demo', 'currentItem'),
        Input('menu-advanced-demo', 'currentKeyPath'),
        Input('menu-advanced-demo', 'currentItemPath'),
    ],
)
def menu_advanced_callback_demo(currentItem, currentKeyPath, currentItemPath):
    return json.dumps(
        dict(
            currentItem=currentItem,
            currentKeyPath=currentKeyPath,
            currentItemPath=currentItemPath,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
