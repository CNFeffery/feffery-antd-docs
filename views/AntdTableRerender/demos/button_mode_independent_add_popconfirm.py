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
                    "dataIndex": "按钮示例",
                    "title": "按钮示例",
                    "renderOptions": {"renderType": "button"},
                },
            ],
            data=[
                {
                    "按钮示例": [
                        {
                            "content": "带气泡确认",
                            "popConfirmProps": {
                                "title": "气泡确认标题",
                                "okText": "确认",
                                "cancelText": "取消",
                            },
                        },
                        {
                            "content": "不带气泡确认",
                        },
                    ]
                }
            ],
            bordered=True,
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "dataIndex": "Button Example",
                    "title": "Button Example",
                    "renderOptions": {"renderType": "button"},
                },
            ],
            data=[
                {
                    "Button Example": [
                        {
                            "content": "With PopConfirm",
                            "popConfirmProps": {
                                "title": "PopConfirm Title",
                                "okText": "Confirm",
                                "cancelText": "Cancel",
                            },
                        },
                        {
                            "content": "Without PopConfirm",
                        },
                    ]
                }
            ],
            bordered=True,
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
            'dataIndex': '按钮示例',
            'title': '按钮示例',
            'renderOptions': {'renderType': 'button'},
        },
    ],
    data=[
        {
            '按钮示例': [
                {
                    'content': '带气泡确认',
                    'popConfirmProps': {
                        'title': '气泡确认标题',
                        'okText': '确认',
                        'cancelText': '取消',
                    },
                },
                {
                    'content': '不带气泡确认',
                },
            ]
        }
    ],
    bordered=True,
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
            'dataIndex': 'Button Example',
            'title': 'Button Example',
            'renderOptions': {'renderType': 'button'},
        },
    ],
    data=[
        {
            'Button Example': [
                {
                    'content': 'With PopConfirm',
                    'popConfirmProps': {
                        'title': 'PopConfirm Title',
                        'okText': 'Confirm',
                        'cancelText': 'Cancel',
                    },
                },
                {
                    'content': 'Without PopConfirm',
                },
            ]
        }
    ],
    bordered=True,
)
"""
            }
        ]
