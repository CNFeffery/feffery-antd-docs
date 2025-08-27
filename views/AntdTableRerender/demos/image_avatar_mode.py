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
                    "title": "image-avatar示例1",
                    "dataIndex": "image-avatar示例1",
                    "renderOptions": {"renderType": "image-avatar"},
                    "width": "50%",
                },
                {
                    "title": "image-avatar示例2",
                    "dataIndex": "image-avatar示例2",
                    "renderOptions": {"renderType": "image-avatar"},
                    "width": "50%",
                },
            ],
            data=[
                {
                    "image-avatar示例1": {
                        "src": "assets/imgs/components/AntdAvatar/avatar-demo.jpg"
                    },
                    "image-avatar示例2": {
                        "src": "assets/imgs/components/AntdAvatar/avatar-demo.jpg",
                        "shape": "square",
                    },
                }
            ]
            * 3,
            bordered=True,
            style={"width": 300},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "title": "image-avatar Example 1",
                    "dataIndex": "image-avatar Example 1",
                    "renderOptions": {"renderType": "image-avatar"},
                    "width": "50%",
                },
                {
                    "title": "image-avatar Example 2",
                    "dataIndex": "image-avatar Example 2",
                    "renderOptions": {"renderType": "image-avatar"},
                    "width": "50%",
                },
            ],
            data=[
                {
                    "image-avatar Example 1": {
                        "src": "assets/imgs/components/AntdAvatar/avatar-demo.jpg"
                    },
                    "image-avatar Example 2": {
                        "src": "assets/imgs/components/AntdAvatar/avatar-demo.jpg",
                        "shape": "square",
                    },
                }
            ]
            * 3,
            bordered=True,
            style={"width": 300},
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
            'title': 'image-avatar示例1',
            'dataIndex': 'image-avatar示例1',
            'renderOptions': {'renderType': 'image-avatar'},
            'width': '50%',
        },
        {
            'title': 'image-avatar示例2',
            'dataIndex': 'image-avatar示例2',
            'renderOptions': {'renderType': 'image-avatar'},
            'width': '50%',
        },
    ],
    data=[
        {
            'image-avatar示例1': {
                'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg'
            },
            'image-avatar示例2': {
                'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                'shape': 'square',
            },
        }
    ]
    * 3,
    bordered=True,
    style={'width': 300},
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
            'title': 'image-avatar Example 1',
            'dataIndex': 'image-avatar Example 1',
            'renderOptions': {'renderType': 'image-avatar'},
            'width': '50%',
        },
        {
            'title': 'image-avatar Example 2',
            'dataIndex': 'image-avatar Example 2',
            'renderOptions': {'renderType': 'image-avatar'},
            'width': '50%',
        },
    ],
    data=[
        {
            'image-avatar Example 1': {
                'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg'
            },
            'image-avatar Example 2': {
                'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                'shape': 'square',
            },
        }
    ]
    * 3,
    bordered=True,
    style={'width': 300},
)
"""
            }
        ]
