import uuid
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fuc.FefferyDiv(
                '请在此区域内任意位置点击鼠标右键',
                id='dropdown-free-position-demo-trigger',
                enableListenContextMenu=True,
                style={
                    'borderRadius': 6,
                    'background': '#adb5bd',
                    'height': 400,
                    'color': 'white',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                },
            ),
            html.Div(id='dropdown-free-position-demo-container'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fuc.FefferyDiv(
                'Please click the mouse right button anywhere in this area',
                id='dropdown-free-position-demo-trigger',
                enableListenContextMenu=True,
                style={
                    'borderRadius': 6,
                    'background': '#adb5bd',
                    'height': 400,
                    'color': 'white',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                },
            ),
            html.Div(id='dropdown-free-position-demo-container'),
        ]

    return demo_contents


@app.callback(
    Output('dropdown-free-position-demo-container', 'children'),
    Input('dropdown-free-position-demo-trigger', 'contextMenuEvent'),
    prevent_initial_call=True,
)
def dropdown_free_position_demo(contextMenuEvent):
    if contextMenuEvent:
        current_locale = get_current_locale()

        if current_locale == 'zh-cn':
            return fac.AntdDropdown(
                key=str(uuid.uuid4()),
                visible=True,
                freePosition=True,
                freePositionStyle={
                    'left': contextMenuEvent['clientX'],
                    'top': contextMenuEvent['clientY'],
                },
                menuItems=[
                    {'title': f'右键菜单选项{i}', 'key': f'右键菜单选项{i}'}
                    for i in range(1, 6)
                ],
                trigger='click',
            )

        elif current_locale == 'en-us':
            return fac.AntdDropdown(
                key=str(uuid.uuid4()),
                visible=True,
                freePosition=True,
                freePositionStyle={
                    'left': contextMenuEvent['clientX'],
                    'top': contextMenuEvent['clientY'],
                },
                menuItems=[
                    {
                        'title': f'Right click menu item{i}',
                        'key': f'Right click menu item{i}',
                    }
                    for i in range(1, 6)
                ],
                trigger='click',
            )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fuc.FefferyDiv(
        '请在此区域内任意位置点击鼠标右键',
        id='dropdown-free-position-demo-trigger',
        enableListenContextMenu=True,
        style={
            'borderRadius': 6,
            'background': '#adb5bd',
            'height': 400,
            'color': 'white',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
        },
    ),
    html.Div(id='dropdown-free-position-demo-container'),
]

...

@app.callback(
    Output('dropdown-free-position-demo-container', 'children'),
    Input('dropdown-free-position-demo-trigger', 'contextMenuEvent'),
    prevent_initial_call=True,
)
def dropdown_free_position_demo(contextMenuEvent):
    if contextMenuEvent:
        return fac.AntdDropdown(
            key=str(uuid.uuid4()),
            visible=True,
            freePosition=True,
            freePositionStyle={
                'left': contextMenuEvent['clientX'],
                'top': contextMenuEvent['clientY'],
            },
            menuItems=[
                {'title': f'右键菜单选项{i}', 'key': f'右键菜单选项{i}'}
                for i in range(1, 6)
            ],
            trigger='click',
        )
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fuc.FefferyDiv(
        'Please click the mouse right button anywhere in this area',
        id='dropdown-free-position-demo-trigger',
        enableListenContextMenu=True,
        style={
            'borderRadius': 6,
            'background': '#adb5bd',
            'height': 400,
            'color': 'white',
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
        },
    ),
    html.Div(id='dropdown-free-position-demo-container'),
]

...

@app.callback(
    Output('dropdown-free-position-demo-container', 'children'),
    Input('dropdown-free-position-demo-trigger', 'contextMenuEvent'),
    prevent_initial_call=True,
)
def dropdown_free_position_demo(contextMenuEvent):
    if contextMenuEvent:
        return fac.AntdDropdown(
            key=str(uuid.uuid4()),
            visible=True,
            freePosition=True,
            freePositionStyle={
                'left': contextMenuEvent['clientX'],
                'top': contextMenuEvent['clientY'],
            },
            menuItems=[
                {
                    'title': f'Right click menu item{i}',
                    'key': f'Right click menu item{i}',
                }
                for i in range(1, 6)
            ],
            trigger='click',
        )
"""
            }
        ]
