from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdMenu(
            id='menu-demo',
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
        html.Div(
            id='menu-demo-output',
            style={
                'height': '200px',
                'background': '#a5d8ff',
                'color': 'white',
                'fontSize': '24px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
        ),
    ]

    return demo_contents


@app.callback(
    Output('menu-demo-output', 'children'), Input('menu-demo', 'currentKey')
)
def menu_callback_demo(currentKey):
    return f'currentKey: {currentKey}'


code_string = [
    {
        'code': """
[
    fac.AntdMenu(
        id='menu-demo',
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
    html.Div(
        id='menu-demo-output',
        style={
            'height': '200px',
            'background': '#a5d8ff',
            'color': 'white',
            'fontSize': '24px',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
        },
    ),
]

...

@app.callback(
    Output('menu-demo-output', 'children'), Input('menu-demo', 'currentKey')
)
def menu_callback_demo(currentKey):
    return f'currentKey: {currentKey}'
"""
    }
]
