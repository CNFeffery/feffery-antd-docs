import feffery_antd_components as fac
import numpy as np
from dash import html
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    # Locale-dependent labels and keys
    if current_locale == 'zh-cn':
        title_text = '左例（未设置） 右例（设置containerId参数）'
        column_label = lambda i: f'字段{i}'
        data_key = lambda j: f'字段{j}'
        filter_key1 = '字段1'
        filter_key3 = '字段3'
    elif current_locale == 'en-us':
        title_text = 'Left (unset)  Right (set containerId parameter)'
        column_label = lambda i: f'Field {i}'
        data_key = lambda j: f'Field {j}'
        filter_key1 = 'Field 1'
        filter_key3 = 'Field 3'
    else:
        # Fallback to Chinese
        title_text = '左例（未设置） 右例（设置containerId参数）'
        column_label = lambda i: f'字段{i}'
        data_key = lambda j: f'字段{j}'
        filter_key1 = '字段1'
        filter_key3 = '字段3'

    def make_table(with_container: bool) -> Component:
        base = dict(
            columns=[
                {'title': column_label(i), 'dataIndex': column_label(i)}
                for i in range(1, 6)
            ],
            data=[
                {
                    data_key(j): np.random.choice(list('abc'))
                    for j in range(1, 6)
                }
                for _ in range(10)
            ],
            filterOptions={
                filter_key1: {'filterMode': 'keyword'},
                filter_key3: {
                    'filterMode': 'checkbox',
                    'filterCustomItems': ['a', 'b', 'c'],
                },
            },
        )
        if with_container:
            base['containerId'] = 'containerId-container-demo'
        return fac.AntdTable(**base)

    demo_contents = [
        fac.AntdTitle(title_text, level=5),
        html.Div(
            [
                html.Div(
                    [
                        make_table(with_container=False),
                        html.Div(style={'height': '400px'}),
                    ],
                    style={
                        'flex': '1',
                        'padding': '20px',
                        'maxHeight': '400px',
                        'overflowY': 'auto',
                    },
                ),
                html.Div(
                    [
                        make_table(with_container=True),
                        html.Div(style={'height': '400px'}),
                    ],
                    id='containerId-container-demo',
                    style={
                        'flex': '1',
                        'padding': '20px',
                        'maxHeight': '400px',
                        'overflowY': 'auto',
                        'position': 'relative',
                    },
                ),
            ],
            style={'display': 'flex'},
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
    fac.AntdTitle('左例（未设置） 右例（设置containerId参数）', level=5),
    html.Div(
        [
            html.Div(
                [
                    fac.AntdTable(
                        columns=[
                            {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
                            for i in range(1, 6)
                        ],
                        data=[
                            {
                                f'字段{j}': np.random.choice(list('abc'))
                                for j in range(1, 6)
                            }
                            for i in range(10)
                        ],
                        filterOptions={
                            '字段1': {'filterMode': 'keyword'},
                            '字段3': {
                                'filterMode': 'checkbox',
                                'filterCustomItems': ['a', 'b', 'c'],
                            },
                        },
                    ),
                    html.Div(style={'height': '400px'}),
                ],
                style={
                    'flex': '1',
                    'padding': '20px',
                    'maxHeight': '400px',
                    'overflowY': 'auto',
                },
            ),
            html.Div(
                [
                    fac.AntdTable(
                        columns=[
                            {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
                            for i in range(1, 6)
                        ],
                        data=[
                            {
                                f'字段{j}': np.random.choice(list('abc'))
                                for j in range(1, 6)
                            }
                            for i in range(10)
                        ],
                        filterOptions={
                            '字段1': {'filterMode': 'keyword'},
                            '字段3': {
                                'filterMode': 'checkbox',
                                'filterCustomItems': ['a', 'b', 'c'],
                            },
                        },
                        containerId='containerId-container-demo',
                    ),
                    html.Div(style={'height': '400px'}),
                ],
                id='containerId-container-demo',
                style={
                    'flex': '1',
                    'padding': '20px',
                    'maxHeight': '400px',
                    'overflowY': 'auto',
                    'position': 'relative',
                },
            ),
        ],
        style={'display': 'flex'},
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
    fac.AntdTitle('Left (unset)  Right (set containerId parameter)', level=5),
    html.Div(
        [
            html.Div(
                [
                    fac.AntdTable(
                        columns=[
                            {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
                            for i in range(1, 6)
                        ],
                        data=[
                            {
                                f'Field {j}': np.random.choice(list('abc'))
                                for j in range(1, 6)
                            }
                            for i in range(10)
                        ],
                        filterOptions={
                            'Field 1': {'filterMode': 'keyword'},
                            'Field 3': {
                                'filterMode': 'checkbox',
                                'filterCustomItems': ['a', 'b', 'c'],
                            },
                        },
                    ),
                    html.Div(style={'height': '400px'}),
                ],
                style={
                    'flex': '1',
                    'padding': '20px',
                    'maxHeight': '400px',
                    'overflowY': 'auto',
                },
            ),
            html.Div(
                [
                    fac.AntdTable(
                        columns=[
                            {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
                            for i in range(1, 6)
                        ],
                        data=[
                            {
                                f'Field {j}': np.random.choice(list('abc'))
                                for j in range(1, 6)
                            }
                            for i in range(10)
                        ],
                        filterOptions={
                            'Field 1': {'filterMode': 'keyword'},
                            'Field 3': {
                                'filterMode': 'checkbox',
                                'filterCustomItems': ['a', 'b', 'c'],
                            },
                        },
                        containerId='containerId-container-demo',
                    ),
                    html.Div(style={'height': '400px'}),
                ],
                id='containerId-container-demo',
                style={
                    'flex': '1',
                    'padding': '20px',
                    'maxHeight': '400px',
                    'overflowY': 'auto',
                    'position': 'relative',
                },
            ),
        ],
        style={'display': 'flex'},
    ),
]
"""
            }
        ]
