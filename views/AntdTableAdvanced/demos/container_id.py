import numpy as np
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
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
                                    f'字段{j}': np.random.randint(1, 5)
                                    for j in range(1, 6)
                                }
                                for i in range(10)
                            ],
                            filterOptions={
                                '字段1': {'filterMode': 'keyword'},
                                '字段3': {
                                    'filterMode': 'checkbox',
                                    'filterCustomItems': [1, 2, 3],
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
                                    f'字段{j}': np.random.randint(1, 5)
                                    for j in range(1, 6)
                                }
                                for i in range(10)
                            ],
                            filterOptions={
                                '字段1': {'filterMode': 'keyword'},
                                '字段3': {
                                    'filterMode': 'checkbox',
                                    'filterCustomItems': [1, 2, 3],
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

    return demo_contents


code_string = [
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
                                f'字段{j}': np.random.randint(1, 5)
                                for j in range(1, 6)
                            }
                            for i in range(10)
                        ],
                        filterOptions={
                            '字段1': {'filterMode': 'keyword'},
                            '字段3': {
                                'filterMode': 'checkbox',
                                'filterCustomItems': [1, 2, 3],
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
                                f'字段{j}': np.random.randint(1, 5)
                                for j in range(1, 6)
                            }
                            for i in range(10)
                        ],
                        filterOptions={
                            '字段1': {'filterMode': 'keyword'},
                            '字段3': {
                                'filterMode': 'checkbox',
                                'filterCustomItems': [1, 2, 3],
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
