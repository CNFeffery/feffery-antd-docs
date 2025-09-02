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
                    'title': 'tags示例1',
                    'dataIndex': 'tags示例1',
                    'renderOptions': {'renderType': 'tags'},
                },
                {
                    'title': 'tags示例2',
                    'dataIndex': 'tags示例2',
                    'renderOptions': {'renderType': 'tags'},
                },
            ],
            data=[
                {
                    'tags示例1': {'tag': f'标签{i}', 'color': 'cyan'},
                    'tags示例2': [
                        {'tag': f'标签{i}-{j}', 'color': color}
                        for j, color in zip(
                            range(1, 4), ['volcano', 'blue', 'geekblue']
                        )
                    ],
                }
                for i in range(1, 4)
            ],
            bordered=True,
            style={'width': 400},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdTable(
            locale='en-us',
            columns=[
                {
                    'title': 'Tags Example 1',
                    'dataIndex': 'Tags Example 1',
                    'renderOptions': {'renderType': 'tags'},
                },
                {
                    'title': 'Tags Example 2',
                    'dataIndex': 'Tags Example 2',
                    'renderOptions': {'renderType': 'tags'},
                },
            ],
            data=[
                {
                    'Tags Example 1': {'tag': f'Tag {i}', 'color': 'cyan'},
                    'Tags Example 2': [
                        {'tag': f'Tag {i}-{j}', 'color': color}
                        for j, color in zip(
                            range(1, 4), ['volcano', 'blue', 'geekblue']
                        )
                    ],
                }
                for i in range(1, 4)
            ],
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
            'title': 'tags示例1',
            'dataIndex': 'tags示例1',
            'renderOptions': {'renderType': 'tags'},
        },
        {
            'title': 'tags示例2',
            'dataIndex': 'tags示例2',
            'renderOptions': {'renderType': 'tags'},
        },
    ],
    data=[
        {
            'tags示例1': {'tag': f'标签{i}', 'color': 'cyan'},
            'tags示例2': [
                {'tag': f'标签{i}-{j}', 'color': color}
                for j, color in zip(
                    range(1, 4), ['volcano', 'blue', 'geekblue']
                )
            ],
        }
        for i in range(1, 4)
    ],
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
    locale="en-us",
    columns=[
        {
            'title': 'Tags Example 1',
            'dataIndex': 'Tags Example 1',
            'renderOptions': {'renderType': 'tags'},
        },
        {
            'title': 'Tags Example 2',
            'dataIndex': 'Tags Example 2',
            'renderOptions': {'renderType': 'tags'},
        },
    ],
    data=[
        {
            'Tags Example 1': {'tag': f'Tag {i}', 'color': 'cyan'},
            'Tags Example 2': [
                {'tag': f'Tag {i}-{j}', 'color': color}
                for j, color in zip(
                    range(1, 4), ['volcano', 'blue', 'geekblue']
                )
            ],
        }
        for i in range(1, 4)
    ],
    bordered=True,
    style={'width': 400},
)
"""
            }
        ]
