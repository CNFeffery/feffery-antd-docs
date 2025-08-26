from datetime import datetime

import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSwitch(id="table-loading", checked=False),
                fac.AntdTable(
                    id="table-loading-demo",
                    columns=[
                        {"title": "int型示例", "dataIndex": "int型示例"},
                        {"title": "float型示例", "dataIndex": "float型示例"},
                        {"title": "str型示例", "dataIndex": "str型示例"},
                        {"title": "日期时间示例", "dataIndex": "日期时间示例"},
                    ],
                    data=[
                        {
                            "int型示例": 123,
                            "float型示例": 1.23,
                            "str型示例": "示例字符",
                            "日期时间示例": datetime.now(),
                        }
                    ]
                    * 3,
                ),
            ],
            direction="vertical",
            style={"width": "100%"},
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSwitch(id="table-loading", checked=False),
                fac.AntdTable(
                    id="table-loading-demo",
                    columns=[
                        {"title": "int Example", "dataIndex": "int Example"},
                        {"title": "float Example", "dataIndex": "float Example"},
                        {"title": "str Example", "dataIndex": "str Example"},
                        {"title": "Datetime Example", "dataIndex": "Datetime Example"},
                    ],
                    data=[
                        {
                            "int Example": 123,
                            "float Example": 1.23,
                            "str Example": "Example string",
                            "Datetime Example": datetime.now(),
                        }
                    ]
                    * 3,
                    locale="en-us",
                ),
            ],
            direction="vertical",
            style={"width": "100%"},
        )

    return demo_contents


@app.callback(
    Output("table-loading-demo", "loading"),
    Input("table-loading", "checked"),
    prevent_initial_call=True,
)
def table_loading(checked):
    return checked


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdSwitch(id='table-loading', checked=False),
        fac.AntdTable(
            id='table-loading-demo',
            columns=[
                {'title': 'int型示例', 'dataIndex': 'int型示例'},
                {'title': 'float型示例', 'dataIndex': 'float型示例'},
                {'title': 'str型示例', 'dataIndex': 'str型示例'},
                {'title': '日期时间示例', 'dataIndex': '日期时间示例'},
            ],
            data=[
                {
                    'int型示例': 123,
                    'float型示例': 1.23,
                    'str型示例': '示例字符',
                    '日期时间示例': datetime.now(),
                }
            ]
            * 3,
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('table-loading-demo', 'loading'),
    Input('table-loading', 'checked'),
    prevent_initial_call=True,
)
def table_loading(checked):
    return checked
"""
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdSwitch(id='table-loading', checked=False),
        fac.AntdTable(
            id='table-loading-demo',
            columns=[
                {'title': 'int Example', 'dataIndex': 'int Example'},
                {'title': 'float Example', 'dataIndex': 'float Example'},
                {'title': 'str Example', 'dataIndex': 'str Example'},
                {'title': 'Datetime Example', 'dataIndex': 'Datetime Example'},
            ],
            data=[
                {
                    'int Example': 123,
                    'float Example': 1.23,
                    'str Example': 'Example string',
                    'Datetime Example': datetime.now(),
                }
            ]
            * 3,
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('table-loading-demo', 'loading'),
    Input('table-loading', 'checked'),
    prevent_initial_call=True,
)
def table_loading(checked):
    return checked
"""
            }
        ]
