from datetime import datetime

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
                    "title": "int型示例",
                    "dataIndex": "int型示例",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "float型示例",
                    "dataIndex": "float型示例",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "str型示例",
                    "dataIndex": "str型示例",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "日期时间示例",
                    "dataIndex": "日期时间示例",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "placeholder示例",
                    "dataIndex": "placeholder示例",
                    "editable": True,
                    "width": "20%",
                    "editOptions": {"placeholder": "请输入内容"},
                },
            ],
            data=[
                {
                    "int型示例": 123,
                    "float型示例": 1.23,
                    "str型示例": "示例字符",
                    "日期时间示例": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ]
            * 3,
            bordered=True,
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdTable(
            columns=[
                {
                    "title": "int Example",
                    "dataIndex": "int Example",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "float Example",
                    "dataIndex": "float Example",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "str Example",
                    "dataIndex": "str Example",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "Datetime Example",
                    "dataIndex": "Datetime Example",
                    "editable": True,
                    "width": "20%",
                },
                {
                    "title": "Placeholder Example",
                    "dataIndex": "Placeholder Example",
                    "editable": True,
                    "width": "20%",
                    "editOptions": {"placeholder": "Please enter content"},
                },
            ],
            data=[
                {
                    "int Example": 123,
                    "float Example": 1.23,
                    "str Example": "Example string",
                    "Datetime Example": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ]
            * 3,
            bordered=True,
            locale="en-us",
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
            'title': 'int型示例',
            'dataIndex': 'int型示例',
            'editable': True,
            'width': '20%',
        },
        {
            'title': 'float型示例',
            'dataIndex': 'float型示例',
            'editable': True,
            'width': '20%',
        },
        {
            'title': 'str型示例',
            'dataIndex': 'str型示例',
            'editable': True,
            'width': '20%',
        },
        {
            'title': '日期时间示例',
            'dataIndex': '日期时间示例',
            'editable': True,
            'width': '20%',
        },
        {
            'title': 'placeholder示例',
            'dataIndex': 'placeholder示例',
            'editable': True,
            'width': '20%',
            'editOptions': {'placeholder': '请输入内容'},
        },
    ],
    data=[
        {
            'int型示例': 123,
            'float型示例': 1.23,
            'str型示例': '示例字符',
            '日期时间示例': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
    ]
    * 3,
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
    columns=[
        {
            'title': 'int Example',
            'dataIndex': 'int Example',
            'editable': True,
            'width': '20%',
        },
        {
            'title': 'float Example',
            'dataIndex': 'float Example',
            'editable': True,
            'width': '20%',
        },
        {
            'title': 'str Example',
            'dataIndex': 'str Example',
            'editable': True,
            'width': '20%',
        },
        {
            'title': 'Datetime Example',
            'dataIndex': 'Datetime Example',
            'editable': True,
            'width': '20%',
        },
        {
            'title': 'Placeholder Example',
            'dataIndex': 'Placeholder Example',
            'editable': True,
            'width': '20%',
            'editOptions': {'placeholder': 'Please enter content'},
        },
    ],
    data=[
        {
            'int Example': 123,
            'float Example': 1.23,
            'str Example': 'Example string',
            'Datetime Example': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
    ]
    * 3,
    bordered=True,
)
"""
            }
        ]
