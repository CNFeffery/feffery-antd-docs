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
                    'title': 'mini-progress示例1',
                    'dataIndex': 'mini-progress示例1',
                    'renderOptions': {'renderType': 'mini-progress'},
                    'width': '50%',
                },
                {
                    'title': 'mini-progress示例2',
                    'dataIndex': 'mini-progress示例2',
                    'renderOptions': {
                        'renderType': 'mini-progress',
                        'progressOneHundredPercentColor': '#f08c00',
                    },
                    'width': '50%',
                },
            ],
            data=[
                {'mini-progress示例1': x, 'mini-progress示例2': x}
                for x in [0, 0.66, 1]
            ],
            bordered=True,
            style={'width': 300},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdTable(
            locale='en-us',
            columns=[
                {
                    'title': 'mini-progress Example 1',
                    'dataIndex': 'mini-progress Example 1',
                    'renderOptions': {'renderType': 'mini-progress'},
                    'width': '50%',
                },
                {
                    'title': 'mini-progress Example 2',
                    'dataIndex': 'mini-progress Example 2',
                    'renderOptions': {
                        'renderType': 'mini-progress',
                        'progressOneHundredPercentColor': '#f08c00',
                    },
                    'width': '50%',
                },
            ],
            data=[
                {'mini-progress Example 1': x, 'mini-progress Example 2': x}
                for x in [0, 0.66, 1]
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
            'title': 'mini-progress示例1',
            'dataIndex': 'mini-progress示例1',
            'renderOptions': {'renderType': 'mini-progress'},
            'width': '50%',
        },
        {
            'title': 'mini-progress示例2',
            'dataIndex': 'mini-progress示例2',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressOneHundredPercentColor': '#f08c00',
            },
            'width': '50%',
        },
    ],
    data=[
        {'mini-progress示例1': x, 'mini-progress示例2': x}
        for x in [0, 0.66, 1]
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
            'title': 'mini-progress Example 1',
            'dataIndex': 'mini-progress Example 1',
            'renderOptions': {'renderType': 'mini-progress'},
            'width': '50%',
        },
        {
            'title': 'mini-progress Example 2',
            'dataIndex': 'mini-progress Example 2',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressOneHundredPercentColor': '#f08c00',
            },
            'width': '50%',
        },
    ],
    data=[
        {'mini-progress Example 1': x, 'mini-progress Example 2': x}
        for x in [0, 0.66, 1]
    ],
    bordered=True,
    style={'width': 300},
)
"""
            }
        ]
