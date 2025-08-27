import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = [
            fac.AntdDivider('单层分组', innerTextOrientation='left'),
            fac.AntdTable(
                columns=[
                    {
                        'title': '字段1-1',
                        'dataIndex': '字段1-1',
                        'group': '字段1',
                    },
                    {
                        'title': '字段1-2',
                        'dataIndex': '字段1-2',
                        'group': '字段1',
                    },
                    {'title': '字段2', 'dataIndex': '字段2'},
                    {
                        'title': '字段3-1',
                        'dataIndex': '字段3-1',
                        'group': '字段3',
                    },
                    {
                        'title': '字段3-2',
                        'dataIndex': '字段3-2',
                        'group': '字段3',
                    },
                    {
                        'title': '字段3-3',
                        'dataIndex': '字段3-3',
                        'group': '字段3',
                    },
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
                    {
                        'title': '字段1-2',
                        'dataIndex': '字段1-2',
                        'group': '字段1',
                    },
                    {'title': '字段2', 'dataIndex': '字段2'},
                ],
                data=[
                    {'字段1-1-1': 1, '字段1-1-2': 1, '字段1-2': 1, '字段2': 1}
                ]
                * 3,
                bordered=True,
            ),
        ]

    elif current_locale == 'en-us':
        demo_contents = [
            fac.AntdDivider(
                'Single-level Grouping', innerTextOrientation='left'
            ),
            fac.AntdTable(
                columns=[
                    {
                        'title': 'Field1-1',
                        'dataIndex': 'Field1-1',
                        'group': 'Field1',
                    },
                    {
                        'title': 'Field1-2',
                        'dataIndex': 'Field1-2',
                        'group': 'Field1',
                    },
                    {'title': 'Field2', 'dataIndex': 'Field2'},
                    {
                        'title': 'Field3-1',
                        'dataIndex': 'Field3-1',
                        'group': 'Field3',
                    },
                    {
                        'title': 'Field3-2',
                        'dataIndex': 'Field3-2',
                        'group': 'Field3',
                    },
                    {
                        'title': 'Field3-3',
                        'dataIndex': 'Field3-3',
                        'group': 'Field3',
                    },
                ],
                data=[
                    {
                        'Field1-1': 1,
                        'Field1-2': 1,
                        'Field2': 1,
                        'Field3-1': 1,
                        'Field3-2': 1,
                        'Field3-3': 1,
                    }
                ]
                * 3,
                bordered=True,
                locale='en-us',
            ),
            fac.AntdDivider(
                'Multi-level Grouping', innerTextOrientation='left'
            ),
            fac.AntdTable(
                columns=[
                    {
                        'title': 'Field1-1-1',
                        'dataIndex': 'Field1-1-1',
                        'group': ['Field1', 'Field1-1'],
                    },
                    {
                        'title': 'Field1-1-2',
                        'dataIndex': 'Field1-1-2',
                        'group': ['Field1', 'Field1-1'],
                    },
                    {
                        'title': 'Field1-2',
                        'dataIndex': 'Field1-2',
                        'group': 'Field1',
                    },
                    {'title': 'Field2', 'dataIndex': 'Field2'},
                ],
                data=[
                    {
                        'Field1-1-1': 1,
                        'Field1-1-2': 1,
                        'Field1-2': 1,
                        'Field2': 1,
                    }
                ]
                * 3,
                bordered=True,
                locale='en-us',
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdDivider('Single-level Grouping', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {'title': 'Field1-1', 'dataIndex': 'Field1-1', 'group': 'Field1'},
            {'title': 'Field1-2', 'dataIndex': 'Field1-2', 'group': 'Field1'},
            {'title': 'Field2', 'dataIndex': 'Field2'},
            {'title': 'Field3-1', 'dataIndex': 'Field3-1', 'group': 'Field3'},
            {'title': 'Field3-2', 'dataIndex': 'Field3-2', 'group': 'Field3'},
            {'title': 'Field3-3', 'dataIndex': 'Field3-3', 'group': 'Field3'},
        ],
        data=[
            {
                'Field1-1': 1,
                'Field1-2': 1,
                'Field2': 1,
                'Field3-1': 1,
                'Field3-2': 1,
                'Field3-3': 1,
            }
        ]
        * 3,
        bordered=True,
    ),
    fac.AntdDivider('Multi-level Grouping', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {
                'title': 'Field1-1-1',
                'dataIndex': 'Field1-1-1',
                'group': ['Field1', 'Field1-1'],
            },
            {
                'title': 'Field1-1-2',
                'dataIndex': 'Field1-1-2',
                'group': ['Field1', 'Field1-1'],
            },
            {'title': 'Field1-2', 'dataIndex': 'Field1-2', 'group': 'Field1'},
            {'title': 'Field2', 'dataIndex': 'Field2'},
        ],
        data=[{'Field1-1-1': 1, 'Field1-1-2': 1, 'Field1-2': 1, 'Field2': 1}]
        * 3,
        bordered=True,
    ),
]
"""
            }
        ]
