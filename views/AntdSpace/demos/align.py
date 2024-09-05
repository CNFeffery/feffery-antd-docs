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
            fac.AntdRadioGroup(
                id='space-align-demo-align',
                options=['start', 'end', 'center', 'baseline'],
                value='start',
            ),
            fac.AntdParagraph('水平方向：'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                            'height': '25px',
                            'width': '50px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '10px',
                            'width': '50px',
                        }
                    ),
                ],
                id='space-align-demo-horizontal',
                align='start',
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                    'padding': '10px',
                },
            ),
            fac.AntdParagraph('竖直方向：'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                            'height': '50px',
                            'width': '25px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    ),
                ],
                id='space-align-demo-vertical',
                align='start',
                direction='vertical',
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                    'padding': '10px',
                },
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdRadioGroup(
                id='space-align-demo-align',
                options=['start', 'end', 'center', 'baseline'],
                value='start',
            ),
            fac.AntdParagraph('Horizontal:'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                            'height': '25px',
                            'width': '50px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '10px',
                            'width': '50px',
                        }
                    ),
                ],
                id='space-align-demo-horizontal',
                align='start',
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                    'padding': '10px',
                },
            ),
            fac.AntdParagraph('Vertical:'),
            fac.AntdSpace(
                [
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                            'height': '50px',
                            'width': '25px',
                        }
                    ),
                    html.Div(
                        style={
                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                            'height': '50px',
                            'width': '50px',
                        }
                    ),
                ],
                id='space-align-demo-vertical',
                align='start',
                direction='vertical',
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                    'padding': '10px',
                },
            ),
        ]

    return demo_contents


@app.callback(
    Output('space-align-demo-horizontal', 'align'),
    Output('space-align-demo-vertical', 'align'),
    Input('space-align-demo-align', 'value'),
)
def update_demo_align(value):
    return value, value


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdRadioGroup(
        id='space-align-demo-align',
        options=['start', 'end', 'center', 'baseline'],
        value='start',
    ),
    fac.AntdParagraph('水平方向：'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'height': '25px',
                    'width': '50px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '10px',
                    'width': '50px',
                }
            ),
        ],
        id='space-align-demo-horizontal',
        align='start',
        style={
            'backgroundColor': 'rgba(241, 241, 241, 0.6)',
            'padding': '10px',
        },
    ),
    fac.AntdParagraph('竖直方向：'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'height': '50px',
                    'width': '25px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            ),
        ],
        id='space-align-demo-vertical',
        align='start',
        direction='vertical',
        style={
            'backgroundColor': 'rgba(241, 241, 241, 0.6)',
            'padding': '10px',
        },
    ),
]

...

@app.callback(
    Output('space-align-demo-horizontal', 'align'),
    Output('space-align-demo-vertical', 'align'),
    Input('space-align-demo-align', 'value'),
)
def update_demo_align(value):
    return value, value
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdRadioGroup(
        id='space-align-demo-align',
        options=['start', 'end', 'center', 'baseline'],
        value='start',
    ),
    fac.AntdParagraph('Horizontal:'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'height': '25px',
                    'width': '50px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '10px',
                    'width': '50px',
                }
            ),
        ],
        id='space-align-demo-horizontal',
        align='start',
        style={
            'backgroundColor': 'rgba(241, 241, 241, 0.6)',
            'padding': '10px',
        },
    ),
    fac.AntdParagraph('Vertical:'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'height': '50px',
                    'width': '25px',
                }
            ),
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            ),
        ],
        id='space-align-demo-vertical',
        align='start',
        direction='vertical',
        style={
            'backgroundColor': 'rgba(241, 241, 241, 0.6)',
            'padding': '10px',
        },
    ),
]

...

@app.callback(
    Output('space-align-demo-horizontal', 'align'),
    Output('space-align-demo-vertical', 'align'),
    Input('space-align-demo-align', 'value'),
)
def update_demo_align(value):
    return value, value
"""
            }
        ]
