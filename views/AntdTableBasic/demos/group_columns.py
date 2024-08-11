import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('单层分组', innerTextOrientation='left'),
        fac.AntdTable(
            columns=[
                {'title': '字段1-1', 'dataIndex': '字段1-1', 'group': '字段1'},
                {'title': '字段1-2', 'dataIndex': '字段1-2', 'group': '字段1'},
                {'title': '字段2', 'dataIndex': '字段2'},
                {'title': '字段3-1', 'dataIndex': '字段3-1', 'group': '字段3'},
                {'title': '字段3-2', 'dataIndex': '字段3-2', 'group': '字段3'},
                {'title': '字段3-3', 'dataIndex': '字段3-3', 'group': '字段3'},
            ],
            data=[
                {
                    '字段1-1': 1,
                    '字段1-2': 1,
                    '字段2': 1,
                    '字段3-1': 1,
                    '字段3-2': 1,
                    '字段3-3': 1,
                }
            ]
            * 3,
            bordered=True,
        ),
        fac.AntdDivider('更多层分组', innerTextOrientation='left'),
        fac.AntdTable(
            columns=[
                {
                    'title': '字段1-1-1',
                    'dataIndex': '字段1-1-1',
                    'group': ['字段1', '字段1-1'],
                },
                {
                    'title': '字段1-1-2',
                    'dataIndex': '字段1-1-2',
                    'group': ['字段1', '字段1-1'],
                },
                {'title': '字段1-2', 'dataIndex': '字段1-2', 'group': '字段1'},
                {'title': '字段2', 'dataIndex': '字段2'},
            ],
            data=[{'字段1-1-1': 1, '字段1-1-2': 1, '字段1-2': 1, '字段2': 1}]
            * 3,
            bordered=True,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('单层分组', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {'title': '字段1-1', 'dataIndex': '字段1-1', 'group': '字段1'},
            {'title': '字段1-2', 'dataIndex': '字段1-2', 'group': '字段1'},
            {'title': '字段2', 'dataIndex': '字段2'},
            {'title': '字段3-1', 'dataIndex': '字段3-1', 'group': '字段3'},
            {'title': '字段3-2', 'dataIndex': '字段3-2', 'group': '字段3'},
            {'title': '字段3-3', 'dataIndex': '字段3-3', 'group': '字段3'},
        ],
        data=[
            {
                '字段1-1': 1,
                '字段1-2': 1,
                '字段2': 1,
                '字段3-1': 1,
                '字段3-2': 1,
                '字段3-3': 1,
            }
        ]
        * 3,
        bordered=True,
    ),
    fac.AntdDivider('更多层分组', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {
                'title': '字段1-1-1',
                'dataIndex': '字段1-1-1',
                'group': ['字段1', '字段1-1'],
            },
            {
                'title': '字段1-1-2',
                'dataIndex': '字段1-1-2',
                'group': ['字段1', '字段1-1'],
            },
            {'title': '字段1-2', 'dataIndex': '字段1-2', 'group': '字段1'},
            {'title': '字段2', 'dataIndex': '字段2'},
        ],
        data=[{'字段1-1-1': 1, '字段1-1-2': 1, '字段1-2': 1, '字段2': 1}]
        * 3,
        bordered=True,
    ),
]
"""
    }
]
