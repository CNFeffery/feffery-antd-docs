import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdTable(
            size='small',
            columns=[
                {
                    'title': '角标模式',
                    'dataIndex': '角标模式',
                    'renderOptions': {'renderType': 'corner-mark'},
                }
            ],
            data=[
                {
                    'key': i,
                    '角标模式': {
                        'content': '角标模式',
                        'color': ['red', 'blue', 'green'][i],
                        'offsetX': -7.5,
                        'offsetY': -8.5,
                        'placement': 'top-left',
                        'hide': [False, True, False][i],
                    },
                }
                for i in range(3)
            ],
            bordered=True,
            style={'width': '200px'},
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdTable(
            locale='en-us',
            size='small',
            columns=[
                {
                    'title': 'Corner Mark Mode',
                    'dataIndex': 'Corner Mark Mode',
                    'renderOptions': {'renderType': 'corner-mark'},
                }
            ],
            data=[
                {
                    'key': i,
                    'Corner Mark Mode': {
                        'content': 'Corner Mark',
                        'color': ['red', 'blue', 'green'][i],
                        'offsetX': -7.5,
                        'offsetY': -8.5,
                        'placement': 'top-left',
                        'hide': [False, True, False][i],
                    },
                }
                for i in range(3)
            ],
            bordered=True,
            style={'width': '200px'},
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
    size='small',
    columns=[
        {
            'title': '角标模式',
            'dataIndex': '角标模式',
            'renderOptions': {'renderType': 'corner-mark'},
        }
    ],
    data=[
        {
            'key': i,
            '角标模式': {
                'content': '角标模式',
                'color': ['red', 'blue', 'green'][i],
                'offsetX': -7.5,
                'offsetY': -8.5,
                'placement': 'top-left',
                'hide': [False, True, False][i],
            },
        }
        for i in range(3)
    ],
    bordered=True,
    style={'width': '200px'},
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
    size='small',
    columns=[
        {
            'title': 'Corner Mark Mode',
            'dataIndex': 'Corner Mark Mode',
            'renderOptions': {'renderType': 'corner-mark'},
        }
    ],
    data=[
        {
            'key': i,
            'Corner Mark Mode': {
                'content': 'Corner Mark',
                'color': ['red', 'blue', 'green'][i],
                'offsetX': -7.5,
                'offsetY': -8.5,
                'placement': 'top-left',
                'hide': [False, True, False][i],
            },
        }
        for i in range(3)
    ],
    bordered=True,
    style={'width': '200px'},
)
"""
            }
        ]
