import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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
        fac.AntdDivider('章节1-1', id='章节1-1', innerTextOrientation='right'),
        html.Div(style={'height': 300}),
        fac.AntdDivider('章节1-2', id='章节1-2', innerTextOrientation='right'),
        html.Div(style={'height': 300}),
        fac.AntdDivider('章节2', id='章节2', innerTextOrientation='right'),
        html.Div(style={'height': 300}),
        fac.AntdDivider('章节2-1', id='章节2-1', innerTextOrientation='right'),
        html.Div(style={'height': 300}),
        fac.AntdDivider('章节2-2', id='章节2-2', innerTextOrientation='right'),
        html.Div(style={'height': 300}),
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdAnchor(
    linkDict=[
        {
            'title': '章节1',
            'href': '#章节1',
            'children': [
                {
                    'title': '章节1-1',
                    'href': '#章节1-1'
                },
                {
                    'title': '章节1-2',
                    'href': '#章节1-2'
                }
            ]
        },
        {
            'title': '章节2',
            'href': '#章节2',
            'children': [
                {
                    'title': '章节2-1',
                    'href': '#章节2-1'
                },
                {
                    'title': '章节2-2',
                    'href': '#章节2-2'
                }
            ]
        }
    ],
    align='left'
),

fac.AntdDivider(
    '章节1',
    id='章节1',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节1-1',
    id='章节1-1',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节1-2',
    id='章节1-2',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节2',
    id='章节2',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节2-1',
    id='章节2-1',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节2-2',
    id='章节2-2',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
)
"""
    }
]
