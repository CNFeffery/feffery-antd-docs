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
            fac.AntdBreadcrumb(
                id='breadcrumnb-demo',
                items=[
                    {'title': '首页', 'key': '首页'},
                    {'title': '下属页面1', 'key': '下属页面1'},
                    {
                        'title': '下属页面1-1',
                        'key': '下属页面1-1',
                        'menuItems': [
                            {
                                'key': '菜单项节点1',
                                'title': '菜单项节点1',
                            },
                            {
                                'key': '菜单项节点2',
                                'title': '菜单项节点2',
                            },
                        ],
                    },
                ],
            ),
            html.Pre(id='breadcrumnb-demo-output'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdBreadcrumb(
                id='breadcrumnb-demo',
                items=[
                    {'title': 'Home', 'key': 'Home'},
                    {'title': 'Subpage1', 'key': 'Subpage1'},
                    {
                        'title': 'Subpage1-1',
                        'key': 'Subpage1-1',
                        'menuItems': [
                            {
                                'key': 'Menu item node1',
                                'title': 'Menu item node1',
                            },
                            {
                                'key': 'Menu item node2',
                                'title': 'Menu item node2',
                            },
                        ],
                    },
                ],
            ),
            html.Pre(id='breadcrumnb-demo-output'),
        ]

    return demo_contents


@app.callback(
    Output('breadcrumnb-demo-output', 'children'),
    Input('breadcrumnb-demo', 'clickedItem'),
    prevent_initial_call=True,
)
def breadcrumb_callback_demo(clickedItem):
    return json.dumps(
        dict(clickedItem=clickedItem), indent=4, ensure_ascii=False
    )


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdBreadcrumb(
        id='breadcrumnb-demo',
        items=[
            {'title': '首页', 'key': '首页'},
            {'title': '下属页面1', 'key': '下属页面1'},
            {
                'title': '下属页面1-1',
                'key': '下属页面1-1',
                'menuItems': [
                    {
                        'key': '菜单项节点1',
                        'title': '菜单项节点1',
                    },
                    {
                        'key': '菜单项节点2',
                        'title': '菜单项节点2',
                    },
                ],
            },
        ],
    ),
    html.Pre(id='breadcrumnb-demo-output'),
]

...

import json

...

@app.callback(
    Output('breadcrumnb-demo-output', 'children'),
    Input('breadcrumnb-demo', 'clickedItem'),
    prevent_initial_call=True
)
def breadcrumb_callback_demo(clickedItem):

    return json.dumps(
        dict(clickedItem=clickedItem),
        indent=4,
        ensure_ascii=False
    )
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdBreadcrumb(
        id='breadcrumnb-demo',
        items=[
            {'title': 'Home', 'key': 'Home'},
            {'title': 'Subpage1', 'key': 'Subpage1'},
            {
                'title': 'Subpage1-1',
                'key': 'Subpage1-1',
                'menuItems': [
                    {
                        'key': 'Menu item node1',
                        'title': 'Menu item node1',
                    },
                    {
                        'key': 'Menu item node2',
                        'title': 'Menu item node2',
                    },
                ],
            },
        ],
    ),
    html.Pre(id='breadcrumnb-demo-output'),
]

...

import json

...

@app.callback(
    Output('breadcrumnb-demo-output', 'children'),
    Input('breadcrumnb-demo', 'clickedItem'),
    prevent_initial_call=True
)
def breadcrumb_callback_demo(clickedItem):

    return json.dumps(
        dict(clickedItem=clickedItem),
        indent=4,
        ensure_ascii=False
    )
"""
            }
        ]
