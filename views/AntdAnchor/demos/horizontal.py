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
                direction='horizontal',
                linkDict=[
                    {
                        'key': f'章节{i}',
                        'title': f'章节{i}',
                        'href': f'#章节{i}',
                    }
                    for i in range(1, 6)
                ],
                align='left',
            ),
            *[
                html.Div(
                    fac.AntdDivider(
                        f'章节{i}',
                        id=f'章节{i}',
                        innerTextOrientation='right',
                    ),
                    style={'paddingBottom': 800},
                )
                for i in range(1, 6)
            ],
            html.Div(style={'height': 300}),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdAnchor(
                direction='horizontal',
                linkDict=[
                    {
                        'key': f'Chapter{i}',
                        'title': f'Chapter{i}',
                        'href': f'#Chapter{i}',
                    }
                    for i in range(1, 6)
                ],
                align='left',
            ),
            *[
                html.Div(
                    fac.AntdDivider(
                        f'Chapter{i}',
                        id=f'Chapter{i}',
                        innerTextOrientation='right',
                    ),
                    style={'paddingBottom': 800},
                )
                for i in range(1, 6)
            ],
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
        direction='horizontal',
        linkDict=[
            {
                'key': f'章节{i}',
                'title': f'章节{i}',
                'href': f'#章节{i}',
            }
            for i in range(1, 6)
        ],
        align='left',
    ),
    *[
        html.Div(
            fac.AntdDivider(
                f'章节{i}',
                id=f'章节{i}',
                innerTextOrientation='right',
            ),
            style={'paddingBottom': 800},
        )
        for i in range(1, 6)
    ],
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
        direction='horizontal',
        linkDict=[
            {
                'key': f'Chapter{i}',
                'title': f'Chapter{i}',
                'href': f'#Chapter{i}',
            }
            for i in range(1, 6)
        ],
        align='left',
    ),
    *[
        html.Div(
            fac.AntdDivider(
                f'Chapter{i}',
                id=f'Chapter{i}',
                innerTextOrientation='right',
            ),
            style={'paddingBottom': 800},
        )
        for i in range(1, 6)
    ],
    html.Div(style={'height': 300}),
]
"""
            }
        ]
