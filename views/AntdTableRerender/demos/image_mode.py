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
                    "title": "交互式图片",
                    "dataIndex": "交互式图片",
                    "renderOptions": {"renderType": "image"},
                },
                {
                    "title": "静态图片",
                    "dataIndex": "静态图片",
                    "renderOptions": {"renderType": "image"},
                },
            ],
            data=[
                {
                    "交互式图片": {
                        "src": "/assets/imgs/fac-logo.svg",
                        "height": "75px",
                    },
                    "静态图片": {
                        "src": "/assets/imgs/fac-logo.svg",
                        "height": "75px",
                        "preview": False,
                    },
                }
                for i in range(5)
            ],
            bordered=True,
            style={"width": "300px"},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "title": "Interactive Image",
                    "dataIndex": "Interactive Image",
                    "renderOptions": {"renderType": "image"},
                },
                {
                    "title": "Static Image",
                    "dataIndex": "Static Image",
                    "renderOptions": {"renderType": "image"},
                },
            ],
            data=[
                {
                    "Interactive Image": {
                        "src": "/assets/imgs/fac-logo.svg",
                        "height": "75px",
                    },
                    "Static Image": {
                        "src": "/assets/imgs/fac-logo.svg",
                        "height": "75px",
                        "preview": False,
                    },
                }
                for i in range(5)
            ],
            bordered=True,
            style={"width": "300px"},
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
            'title': '交互式图片',
            'dataIndex': '交互式图片',
            'renderOptions': {'renderType': 'image'},
        },
        {
            'title': '静态图片',
            'dataIndex': '静态图片',
            'renderOptions': {'renderType': 'image'},
        },
    ],
    data=[
        {
            '交互式图片': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px',
            },
            '静态图片': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px',
                'preview': False,
            },
        }
        for i in range(5)
    ],
    bordered=True,
    style={'width': '300px'},
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
            'title': 'Interactive Image',
            'dataIndex': 'Interactive Image',
            'renderOptions': {'renderType': 'image'},
        },
        {
            'title': 'Static Image',
            'dataIndex': 'Static Image',
            'renderOptions': {'renderType': 'image'},
        },
    ],
    data=[
        {
            'Interactive Image': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px',
            },
            'Static Image': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px',
                'preview': False,
            },
        }
        for i in range(5)
    ],
    bordered=True,
    style={'width': '300px'},
)
"""
            }
        ]
