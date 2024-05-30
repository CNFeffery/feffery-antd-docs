import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'),
     Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText('　nClicks: ', strong=True),
        fac.AntdText(nClicks)
    ]


code_string = [
    {
        'code': """
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
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1',
            'key': '子页面3-1'
        },
        {
            'title': '子页面3-2',
            'key': '子页面3-2'
        }
    ]
),

html.Div(
    id='dropdown-demo-output'
)

...

@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'),
     Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText('　nClicks: ', strong=True),
        fac.AntdText(nClicks)
    ]
"""
    }
]
