import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdTable(
            columns=[
                {
                    "title": "link示例1",
                    "dataIndex": "link示例1",
                    "renderOptions": {"renderType": "link"},
                    "width": "50%",
                },
                {
                    "title": "link示例2",
                    "dataIndex": "link示例2",
                    "renderOptions": {
                        "renderType": "link",
                        "renderLinkText": "示例链接",
                    },
                    "width": "50%",
                },
            ],
            data=[
                {
                    "link示例1": {"content": f"{content}仓库", "href": href},
                    "link示例2": {"href": "/AntdTable-rerender"},
                }
                for href, content in zip(
                    [
                        "https://github.com/CNFeffery/feffery-antd-components",
                        "https://github.com/CNFeffery/feffery-utils-components",
                        "https://github.com/CNFeffery/feffery-antd-charts",
                        "https://github.com/CNFeffery/feffery-markdown-components",
                        "https://github.com/CNFeffery/feffery-leaflet-components",
                    ],
                    ["fac", "fuc", "fact", "fmc", "flc"],
                )
            ],
            bordered=True,
            style={"width": 400},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "title": "link Example 1",
                    "dataIndex": "link Example 1",
                    "renderOptions": {"renderType": "link"},
                    "width": "50%",
                },
                {
                    "title": "link Example 2",
                    "dataIndex": "link Example 2",
                    "renderOptions": {
                        "renderType": "link",
                        "renderLinkText": "Example Link",
                    },
                    "width": "50%",
                },
            ],
            data=[
                {
                    "link Example 1": {"content": f"{content} repo", "href": href},
                    "link Example 2": {"href": "/AntdTable-rerender"},
                }
                for href, content in zip(
                    [
                        "https://github.com/CNFeffery/feffery-antd-components",
                        "https://github.com/CNFeffery/feffery-utils-components",
                        "https://github.com/CNFeffery/feffery-antd-charts",
                        "https://github.com/CNFeffery/feffery-markdown-components",
                        "https://github.com/CNFeffery/feffery-leaflet-components",
                    ],
                    ["fac", "fuc", "fact", "fmc", "flc"],
                )
            ],
            bordered=True,
            style={"width": 400},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {
            'title': 'link示例1',
            'dataIndex': 'link示例1',
            'renderOptions': {'renderType': 'link'},
            'width': '50%',
        },
        {
            'title': 'link示例2',
            'dataIndex': 'link示例2',
            'renderOptions': {
                'renderType': 'link',
                'renderLinkText': '示例链接',
            },
            'width': '50%',
        },
    ],
    data=[
        {
            'link示例1': {'content': f'{content}仓库', 'href': href},
            'link示例2': {'href': '/AntdTable-rerender'},
        }
        for href, content in zip(
            [
                'https://github.com/CNFeffery/feffery-antd-components',
                'https://github.com/CNFeffery/feffery-utils-components',
                'https://github.com/CNFeffery/feffery-antd-charts',
                'https://github.com/CNFeffery/feffery-markdown-components',
                'https://github.com/CNFeffery/feffery-leaflet-components',
            ],
            ['fac', 'fuc', 'fact', 'fmc', 'flc'],
        )
    ],
    bordered=True,
    style={'width': 400},
)
"""
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdTable(
    locale='en-us',
    columns=[
        {
            'title': 'link Example 1',
            'dataIndex': 'link Example 1',
            'renderOptions': {'renderType': 'link'},
            'width': '50%',
        },
        {
            'title': 'link Example 2',
            'dataIndex': 'link Example 2',
            'renderOptions': {
                'renderType': 'link',
                'renderLinkText': 'Example Link',
            },
            'width': '50%',
        },
    ],
    data=[
        {
            'link Example 1': {'content': f'{content} repo', 'href': href},
            'link Example 2': {'href': '/AntdTable-rerender'},
        }
        for href, content in zip(
            [
                'https://github.com/CNFeffery/feffery-antd-components',
                'https://github.com/CNFeffery/feffery-utils-components',
                'https://github.com/CNFeffery/feffery-antd-charts',
                'https://github.com/CNFeffery/feffery-markdown-components',
                'https://github.com/CNFeffery/feffery-leaflet-components',
            ],
            ['fac', 'fuc', 'fact', 'fmc', 'flc'],
        )
    ],
    bordered=True,
    style={'width': 400},
)
"""
            }
        ]
