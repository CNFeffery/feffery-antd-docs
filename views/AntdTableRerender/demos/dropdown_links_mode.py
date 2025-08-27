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
                    'title': 'dropdown-links示例1',
                    'dataIndex': 'dropdown-links示例1',
                    'renderOptions': {'renderType': 'dropdown-links'},
                    'width': '30%',
                },
                {
                    'title': 'dropdown-links示例2',
                    'dataIndex': 'dropdown-links示例2',
                    'renderOptions': {
                        'renderType': 'dropdown-links',
                        'dropdownProps': {'title': '更多'},
                    },
                    'width': '70%',
                },
            ],
            data=[
                {
                    'dropdown-links示例1': [
                        {
                            'title': f'image示例{i}.png',
                            'href': f'assets/imgs/image示例{i}.png',
                        }
                        for i in range(1, 8)
                    ],
                    'dropdown-links示例2': [
                        {
                            'title': f'image示例{i}.png',
                            'href': f'assets/imgs/image示例{i}.png',
                        }
                        for i in range(1, 8)
                    ],
                }
            ]
            * 3,
            bordered=True,
            style={'width': 400},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdTable(
            locale='en-us',
            columns=[
                {
                    'title': 'Dropdown Links Example 1',
                    'dataIndex': 'Dropdown Links Example 1',
                    'renderOptions': {'renderType': 'dropdown-links'},
                    'width': '30%',
                },
                {
                    'title': 'Dropdown Links Example 2',
                    'dataIndex': 'Dropdown Links Example 2',
                    'renderOptions': {
                        'renderType': 'dropdown-links',
                        'dropdownProps': {'title': 'More'},
                    },
                    'width': '70%',
                },
            ],
            data=[
                {
                    'Dropdown Links Example 1': [
                        {
                            'title': f'image-example-{i}.png',
                            'href': f'assets/imgs/image-example-{i}.png',
                        }
                        for i in range(1, 8)
                    ],
                    'Dropdown Links Example 2': [
                        {
                            'title': f'image-example-{i}.png',
                            'href': f'assets/imgs/image-example-{i}.png',
                        }
                        for i in range(1, 8)
                    ],
                }
            ]
            * 3,
            bordered=True,
            style={'width': 400},
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
            'title': 'dropdown-links示例1',
            'dataIndex': 'dropdown-links示例1',
            'renderOptions': {'renderType': 'dropdown-links'},
            'width': '30%',
        },
        {
            'title': 'dropdown-links示例2',
            'dataIndex': 'dropdown-links示例2',
            'renderOptions': {
                'renderType': 'dropdown-links',
                'dropdownProps': {'title': '更多'},
            },
            'width': '70%',
        },
    ],
    data=[
        {
            'dropdown-links示例1': [
                {
                    'title': f'image示例{i}.png',
                    'href': f'assets/imgs/image示例{i}.png',
                }
                for i in range(1, 8)
            ],
            'dropdown-links示例2': [
                {
                    'title': f'image示例{i}.png',
                    'href': f'assets/imgs/image示例{i}.png',
                }
                for i in range(1, 8)
            ],
        }
    ]
    * 3,
    bordered=True,
    style={'width': 400},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdTable(
    locale='en-us',
    columns=[
        {
            'title': 'Dropdown Links Example 1',
            'dataIndex': 'Dropdown Links Example 1',
            'renderOptions': {'renderType': 'dropdown-links'},
            'width': '30%',
        },
        {
            'title': 'Dropdown Links Example 2',
            'dataIndex': 'Dropdown Links Example 2',
            'renderOptions': {
                'renderType': 'dropdown-links',
                'dropdownProps': {'title': 'More'},
            },
            'width': '70%',
        },
    ],
    data=[
        {
            'Dropdown Links Example 1': [
                {
                    'title': f'image-example-{i}.png',
                    'href': f'assets/imgs/image-example-{i}.png',
                }
                for i in range(1, 8)
            ],
            'Dropdown Links Example 2': [
                {
                    'title': f'image-example-{i}.png',
                    'href': f'assets/imgs/image-example-{i}.png',
                }
                for i in range(1, 8)
            ],
        }
    ]
    * 3,
    bordered=True,
    style={'width': 400},
)
"""
            }
        ]
