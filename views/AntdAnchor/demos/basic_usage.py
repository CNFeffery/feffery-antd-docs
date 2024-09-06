from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdAnchor(
                linkDict=[
                    {
                        'title': '章节1',
                        'href': '#章节1',
                        'children': [
                            {'title': '章节1-1', 'href': '#章节1-1'},
                            {'title': '章节1-2', 'href': '#章节1-2'},
                        ],
                    },
                    {
                        'title': '章节2',
                        'href': '#章节2',
                        'children': [
                            {'title': '章节2-1', 'href': '#章节2-1'},
                            {'title': '章节2-2', 'href': '#章节2-2'},
                        ],
                    },
                ],
                align='left',
            ),
            fac.AntdDivider('章节1', id='章节1', innerTextOrientation='right'),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                '章节1-1', id='章节1-1', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                '章节1-2', id='章节1-2', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider('章节2', id='章节2', innerTextOrientation='right'),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                '章节2-1', id='章节2-1', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                '章节2-2', id='章节2-2', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdAnchor(
                linkDict=[
                    {
                        'title': 'Chapter1',
                        'href': '#Chapter1',
                        'children': [
                            {'title': 'Chapter1-1', 'href': '#Chapter1-1'},
                            {'title': 'Chapter1-2', 'href': '#Chapter1-2'},
                        ],
                    },
                    {
                        'title': 'Chapter2',
                        'href': '#Chapter2',
                        'children': [
                            {'title': 'Chapter2-1', 'href': '#Chapter2-1'},
                            {'title': 'Chapter2-2', 'href': '#Chapter2-2'},
                        ],
                    },
                ],
                align='left',
            ),
            fac.AntdDivider(
                'Chapter1', id='Chapter1', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                'Chapter1-1', id='Chapter1-1', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                'Chapter1-2', id='Chapter1-2', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                'Chapter2', id='Chapter2', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                'Chapter2-1', id='Chapter2-1', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
            fac.AntdDivider(
                'Chapter2-2', id='Chapter2-2', innerTextOrientation='right'
            ),
            html.Div(style={'height': 300}),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdAnchor(
        linkDict=[
            {
                'title': '章节1',
                'href': '#章节1',
                'children': [
                    {'title': '章节1-1', 'href': '#章节1-1'},
                    {'title': '章节1-2', 'href': '#章节1-2'},
                ],
            },
            {
                'title': '章节2',
                'href': '#章节2',
                'children': [
                    {'title': '章节2-1', 'href': '#章节2-1'},
                    {'title': '章节2-2', 'href': '#章节2-2'},
                ],
            },
        ],
        align='left',
    ),
    fac.AntdDivider('章节1', id='章节1', innerTextOrientation='right'),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        '章节1-1', id='章节1-1', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        '章节1-2', id='章节1-2', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider('章节2', id='章节2', innerTextOrientation='right'),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        '章节2-1', id='章节2-1', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        '章节2-2', id='章节2-2', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
]
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdAnchor(
        linkDict=[
            {
                'title': 'Chapter1',
                'href': '#Chapter1',
                'children': [
                    {'title': 'Chapter1-1', 'href': '#Chapter1-1'},
                    {'title': 'Chapter1-2', 'href': '#Chapter1-2'},
                ],
            },
            {
                'title': 'Chapter2',
                'href': '#Chapter2',
                'children': [
                    {'title': 'Chapter2-1', 'href': '#Chapter2-1'},
                    {'title': 'Chapter2-2', 'href': '#Chapter2-2'},
                ],
            },
        ],
        align='left',
    ),
    fac.AntdDivider(
        'Chapter1', id='Chapter1', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        'Chapter1-1', id='Chapter1-1', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        'Chapter1-2', id='Chapter1-2', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        'Chapter2', id='Chapter2', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        'Chapter2-1', id='Chapter2-1', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
    fac.AntdDivider(
        'Chapter2-2', id='Chapter2-2', innerTextOrientation='right'
    ),
    html.Div(style={'height': 300}),
]
"""
            }
        ]
