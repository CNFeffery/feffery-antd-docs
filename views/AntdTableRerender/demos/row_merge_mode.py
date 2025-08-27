import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdTable(
            columns=[
                {
                    'title': 'row-merge示例1',
                    'dataIndex': 'row-merge示例1',
                    'renderOptions': {'renderType': 'row-merge'},
                    'width': '50%',
                },
                {
                    'title': 'row-merge示例2',
                    'dataIndex': 'row-merge示例2',
                    'renderOptions': {'renderType': 'row-merge'},
                    'width': '50%',
                },
            ],
            data=[
                {
                    'row-merge示例1': {'content': '示例1-1', 'rowSpan': 1},
                    'row-merge示例2': {'content': '示例2-1', 'rowSpan': 2},
                },
                {
                    'row-merge示例1': {'content': '示例1-2', 'rowSpan': 2},
                    'row-merge示例2': {'rowSpan': 0},
                },
                {
                    'row-merge示例1': {'rowSpan': 0},
                    'row-merge示例2': {'content': '示例2-2', 'rowSpan': 1},
                },
            ],
            bordered=True,
            style={'width': 300},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdTable(
            locale='en-us',
            columns=[
                {
                    'title': 'row-merge Example 1',
                    'dataIndex': 'row-merge Example 1',
                    'renderOptions': {'renderType': 'row-merge'},
                    'width': '50%',
                },
                {
                    'title': 'row-merge Example 2',
                    'dataIndex': 'row-merge Example 2',
                    'renderOptions': {'renderType': 'row-merge'},
                    'width': '50%',
                },
            ],
            data=[
                {
                    'row-merge Example 1': {
                        'content': 'Example 1-1',
                        'rowSpan': 1,
                    },
                    'row-merge Example 2': {
                        'content': 'Example 2-1',
                        'rowSpan': 2,
                    },
                },
                {
                    'row-merge Example 1': {
                        'content': 'Example 1-2',
                        'rowSpan': 2,
                    },
                    'row-merge Example 2': {'rowSpan': 0},
                },
                {
                    'row-merge Example 1': {'rowSpan': 0},
                    'row-merge Example 2': {
                        'content': 'Example 2-2',
                        'rowSpan': 1,
                    },
                },
            ],
            bordered=True,
            style={'width': 300},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {
            'title': 'row-merge示例1',
            'dataIndex': 'row-merge示例1',
            'renderOptions': {'renderType': 'row-merge'},
            'width': '50%',
        },
        {
            'title': 'row-merge示例2',
            'dataIndex': 'row-merge示例2',
            'renderOptions': {'renderType': 'row-merge'},
            'width': '50%',
        },
    ],
    data=[
        {
            'row-merge示例1': {'content': '示例1-1', 'rowSpan': 1},
            'row-merge示例2': {'content': '示例2-1', 'rowSpan': 2},
        },
        {
            'row-merge示例1': {'content': '示例1-2', 'rowSpan': 2},
            'row-merge示例2': {'rowSpan': 0},
        },
        {
            'row-merge示例1': {'rowSpan': 0},
            'row-merge示例2': {'content': '示例2-2', 'rowSpan': 1},
        },
    ],
    bordered=True,
    style={'width': 300},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdTable(
    locale="en-us",
    columns=[
        {
            'title': 'row-merge Example 1',
            'dataIndex': 'row-merge Example 1',
            'renderOptions': {'renderType': 'row-merge'},
            'width': '50%',
        },
        {
            'title': 'row-merge Example 2',
            'dataIndex': 'row-merge Example 2',
            'renderOptions': {'renderType': 'row-merge'},
            'width': '50%',
        },
    ],
    data=[
        {
            'row-merge Example 1': {'content': 'Example 1-1', 'rowSpan': 1},
            'row-merge Example 2': {'content': 'Example 2-1', 'rowSpan': 2},
        },
        {
            'row-merge Example 1': {'content': 'Example 1-2', 'rowSpan': 2},
            'row-merge Example 2': {'rowSpan': 0},
        },
        {
            'row-merge Example 1': {'rowSpan': 0},
            'row-merge Example 2': {'content': 'Example 2-2', 'rowSpan': 1},
        },
    ],
    bordered=True,
    style={'width': 300},
)
"""
            }
        ]
