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
            fac.AntdDropdown(
                id='dropdown-demo',
                title='触发点',
                arrow=True,
                placement='topCenter',
                menuItems=[
                    {
                        'title': '子页面1',
                        'key': '子页面1',
                    },
                    {
                        'title': '子页面2',
                        'key': '子页面2',
                    },
                    {'isDivider': True},
                    {'title': '子页面3-1', 'key': '子页面3-1'},
                    {'title': '子页面3-2', 'key': '子页面3-2'},
                ],
            ),
            html.Div(id='dropdown-demo-output'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDropdown(
                id='dropdown-demo',
                title='Trigger point',
                arrow=True,
                placement='topCenter',
                menuItems=[
                    {
                        'title': 'Subpage1',
                        'key': 'Subpage1',
                    },
                    {
                        'title': 'Subpage2',
                        'key': 'Subpage2',
                    },
                    {'isDivider': True},
                    {'title': 'Subpage3-1', 'key': 'Subpage3-1'},
                    {'title': 'Subpage3-2', 'key': 'Subpage3-2'},
                ],
            ),
            html.Div(id='dropdown-demo-output'),
        ]

    return demo_contents


@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'), Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True,
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText('　nClicks: ', strong=True),
        fac.AntdText(nClicks),
    ]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdDropdown(
        id='dropdown-demo',
        title='触发点',
        arrow=True,
        placement='topCenter',
        menuItems=[
            {
                'title': '子页面1',
                'key': '子页面1',
            },
            {
                'title': '子页面2',
                'key': '子页面2',
            },
            {'isDivider': True},
            {'title': '子页面3-1', 'key': '子页面3-1'},
            {'title': '子页面3-2', 'key': '子页面3-2'},
        ],
    ),
    html.Div(id='dropdown-demo-output'),
]

...

@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'), Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True,
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText('　nClicks: ', strong=True),
        fac.AntdText(nClicks),
    ]
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdDropdown(
        id='dropdown-demo',
        title='Trigger point',
        arrow=True,
        placement='topCenter',
        menuItems=[
            {
                'title': 'Subpage1',
                'key': 'Subpage1',
            },
            {
                'title': 'Subpage2',
                'key': 'Subpage2',
            },
            {'isDivider': True},
            {'title': 'Subpage3-1', 'key': 'Subpage3-1'},
            {'title': 'Subpage3-2', 'key': 'Subpage3-2'},
        ],
    ),
    html.Div(id='dropdown-demo-output'),
]

...

@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'), Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True,
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText('　nClicks: ', strong=True),
        fac.AntdText(nClicks),
    ]
"""
            }
        ]
