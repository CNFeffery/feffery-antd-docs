import feffery_antd_components as fac
import feffery_utils_components as fuc
import uuid
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


@app.callback(
    Output('dropdown-free-position-demo-container', 'children'),
    Input('dropdown-free-position-demo-trigger', 'contextMenuEvent'),
    prevent_initial_call=True
)
def dropdown_free_position_demo(contextMenuEvent):

    if contextMenuEvent:

        return fac.AntdDropdown(
            key=str(uuid.uuid4()),
            visible=True,
            freePosition=True,
            freePositionStyle={
                'left': contextMenuEvent['clientX'],
                'top': contextMenuEvent['clientY']
            },
            menuItems=[
                {
                    'title': f'右键菜单选项{i}',
                    'key': f'右键菜单选项{i}'
                }
                for i in range(1, 6)
            ],
            trigger='click'
        )


code_string = [
    {
        'code': """
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
        'alignItems': 'center'
    }
),

html.Div(id='dropdown-free-position-demo-container')

...

import uuid

...

@app.callback(
    Output('dropdown-free-position-demo-container', 'children'),
    Input('dropdown-free-position-demo-trigger', 'contextMenuEvent'),
    prevent_initial_call=True
)
def dropdown_free_position_demo(contextMenuEvent):

    if contextMenuEvent:

        return fac.AntdDropdown(
            key=str(uuid.uuid4()),
            visible=True,
            freePosition=True,
            freePositionStyle={
                'left': contextMenuEvent['clientX'],
                'top': contextMenuEvent['clientY']
            },
            menuItems=[
                {
                    'title': f'右键菜单选项{i}',
                    'key': f'右键菜单选项{i}'
                }
                for i in range(1, 6)
            ],
            trigger='click'
        )
"""
    }
]
