import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = [
            fac.AntdDivider('冻结在左侧', innerTextOrientation='left'),
            html.Div(
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}',
                            'fixed': 'left' if i == 1 else None,
                        }
                        for i in range(1, 6)
                    ],
                    data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
                    maxWidth=900,
                ),
                style={'maxWidth': 700, 'margin': '0 auto'},
            ),
            fac.AntdDivider('冻结在右侧', innerTextOrientation='left'),
            html.Div(
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}',
                            'fixed': 'right' if i == 5 else None,
                        }
                        for i in range(1, 6)
                    ],
                    data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
                    maxWidth=900,
                ),
                style={'maxWidth': 700, 'margin': '0 auto'},
            ),
            fac.AntdDivider('双侧同时冻结', innerTextOrientation='left'),
            html.Div(
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}',
                            'fixed': (
                                'left'
                                if i == 1
                                else ('right' if i == 5 else None)
                            ),
                        }
                        for i in range(1, 6)
                    ],
                    data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
                    maxWidth=900,
                ),
                style={'maxWidth': 700, 'margin': '0 auto'},
            ),
        ]

    elif current_locale == 'en-us':
        demo_contents = [
            fac.AntdDivider('Frozen on the Left', innerTextOrientation='left'),
            html.Div(
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'Field {i}',
                            'dataIndex': f'Field {i}',
                            'fixed': 'left' if i == 1 else None,
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {f'Field {i}': 'Example Content' for i in range(1, 6)}
                    ]
                    * 3,
                    maxWidth=900,
                    locale='en-us',
                ),
                style={'maxWidth': 700, 'margin': '0 auto'},
            ),
            fac.AntdDivider('Frozen on the Right', innerTextOrientation='left'),
            html.Div(
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'Field {i}',
                            'dataIndex': f'Field {i}',
                            'fixed': 'right' if i == 5 else None,
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {f'Field {i}': 'Example Content' for i in range(1, 6)}
                    ]
                    * 3,
                    locale='en-us',
                    maxWidth=900,
                ),
                style={'maxWidth': 700, 'margin': '0 auto'},
            ),
            fac.AntdDivider(
                'Frozen on Both Sides', innerTextOrientation='left'
            ),
            html.Div(
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'Field {i}',
                            'dataIndex': f'Field {i}',
                            'fixed': (
                                'left'
                                if i == 1
                                else ('right' if i == 5 else None)
                            ),
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {f'Field {i}': 'Example Content' for i in range(1, 6)}
                    ]
                    * 3,
                    maxWidth=900,
                    locale='en-us',
                ),
                style={'maxWidth': 700, 'margin': '0 auto'},
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdDivider('冻结在左侧', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'字段{i}',
                    'dataIndex': f'字段{i}',
                    'fixed': 'left' if i == 1 else None,
                }
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdDivider('冻结在右侧', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'字段{i}',
                    'dataIndex': f'字段{i}',
                    'fixed': 'right' if i == 5 else None,
                }
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdDivider('双侧同时冻结', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'字段{i}',
                    'dataIndex': f'字段{i}',
                    'fixed': (
                        'left' if i == 1 else ('right' if i == 5 else None)
                    ),
                }
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
]
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdDivider('Frozen on the Left', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'Field {i}',
                    'dataIndex': f'Field {i}',
                    'fixed': 'left' if i == 1 else None,
                }
                for i in range(1, 6)
            ],
            data=[{f'Field {i}': 'Example Content' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdDivider('Frozen on the Right', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'Field {i}',
                    'dataIndex': f'Field {i}',
                    'fixed': 'right' if i == 5 else None,
                }
                for i in range(1, 6)
            ],
            data=[{f'Field {i}': 'Example Content' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdDivider('Frozen on Both Sides', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'Field {i}',
                    'dataIndex': f'Field {i}',
                    'fixed': (
                        'left' if i == 1 else ('right' if i == 5 else None)
                    ),
                }
                for i in range(1, 6)
            ],
            data=[{f'Field {i}': 'Example Content' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
]
"""
            }
        ]
