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
                    "title": "状态徽标示例",
                    "dataIndex": "状态徽标示例",
                    "renderOptions": {"renderType": "status-badge"},
                }
            ],
            data=[
                {
                    "key": i,
                    "状态徽标示例": {"status": status, "text": status + "状态示例"},
                }
                for i, status in enumerate(
                    ["success", "processing", "default", "error", "warning"]
                )
            ],
            style={"width": "250px"},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            locale="en-us",
            columns=[
                {
                    "title": "Status Badge Example",
                    "dataIndex": "Status Badge Example",
                    "renderOptions": {"renderType": "status-badge"},
                }
            ],
            data=[
                {
                    "key": i,
                    "Status Badge Example": {
                        "status": status,
                        "text": status.capitalize() + " status example",
                    },
                }
                for i, status in enumerate(
                    ["success", "processing", "default", "error", "warning"]
                )
            ],
            style={"width": "250px"},
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
            'title': '状态徽标示例',
            'dataIndex': '状态徽标示例',
            'renderOptions': {'renderType': 'status-badge'},
        }
    ],
    data=[
        {
            'key': i,
            '状态徽标示例': {'status': status, 'text': status + '状态示例'},
        }
        for i, status in enumerate(
            ['success', 'processing', 'default', 'error', 'warning']
        )
    ],
    style={'width': '250px'},
)
"""
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdTable(
    locale="en-us",
    columns=[
        {
            'title': 'Status Badge Example',
            'dataIndex': 'Status Badge Example',
            'renderOptions': {'renderType': 'status-badge'},
        }
    ],
    data=[
        {
            'key': i,
            'Status Badge Example': {
                'status': status,
                'text': status.capitalize() + ' status example',
            },
        }
        for i, status in enumerate(
            ['success', 'processing', 'default', 'error', 'warning']
        )
    ],
    style={'width': '250px'},
)
"""
            }
        ]
