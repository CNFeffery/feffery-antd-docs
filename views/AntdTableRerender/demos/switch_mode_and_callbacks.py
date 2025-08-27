import json

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = [
            fac.AntdTable(
                id="table-rerender-switch-demo",
                columns=[
                    {
                        "title": "switch示例",
                        "dataIndex": "switch示例",
                        "renderOptions": {"renderType": "switch"},
                    }
                ],
                data=[
                    {
                        "switch示例": {
                            "checked": i % 2 == 0,
                            "checkedChildren": "开",
                            "unCheckedChildren": "关",
                            "custom": "balabalabalabala",
                        }
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={"width": 200},
            ),
            html.Pre(id="table-rerender-switch-demo-output"),
        ]

    elif current_locale == "en-us":
        demo_contents = [
            fac.AntdTable(
                id="table-rerender-switch-demo",
                locale="en-us",
                columns=[
                    {
                        "title": "Switch Example",
                        "dataIndex": "Switch Example",
                        "renderOptions": {"renderType": "switch"},
                    }
                ],
                data=[
                    {
                        "Switch Example": {
                            "checked": i % 2 == 0,
                            "checkedChildren": "On",
                            "unCheckedChildren": "Off",
                            "custom": "balabalabalabala",
                        }
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={"width": 200},
            ),
            html.Pre(id="table-rerender-switch-demo-output"),
        ]

    return demo_contents


@app.callback(
    Output("table-rerender-switch-demo-output", "children"),
    [
        Input("table-rerender-switch-demo", "recentlySwitchDataIndex"),
        Input("table-rerender-switch-demo", "recentlySwitchStatus"),
        Input("table-rerender-switch-demo", "recentlySwitchRow"),
    ],
    prevent_initial_call=True,
)
def table_rerender_switch_demo(
    recentlySwitchDataIndex, recentlySwitchStatus, recentlySwitchRow
):
    return json.dumps(
        dict(
            recentlySwitchDataIndex=recentlySwitchDataIndex,
            recentlySwitchStatus=recentlySwitchStatus,
            recentlySwitchRow=recentlySwitchRow,
        ),
        indent=4,
        ensure_ascii=False,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
[
    fac.AntdTable(
        id='table-rerender-switch-demo',
        columns=[
            {
                'title': 'switch示例',
                'dataIndex': 'switch示例',
                'renderOptions': {'renderType': 'switch'},
            }
        ],
        data=[
            {
                'switch示例': {
                    'checked': i % 2 == 0,
                    'checkedChildren': '开',
                    'unCheckedChildren': '关',
                    'custom': 'balabalabalabala',
                }
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-switch-demo-output'),
]

...

@app.callback(
    Output('table-rerender-switch-demo-output', 'children'),
    [
        Input('table-rerender-switch-demo', 'recentlySwitchDataIndex'),
        Input('table-rerender-switch-demo', 'recentlySwitchStatus'),
        Input('table-rerender-switch-demo', 'recentlySwitchRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_switch_demo(
    recentlySwitchDataIndex, recentlySwitchStatus, recentlySwitchRow
):
    return json.dumps(
        dict(
            recentlySwitchDataIndex=recentlySwitchDataIndex,
            recentlySwitchStatus=recentlySwitchStatus,
            recentlySwitchRow=recentlySwitchRow,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": """
[
    fac.AntdTable(
        id='table-rerender-switch-demo',
        locale="en-us",
        columns=[
            {
                'title': 'Switch Example',
                'dataIndex': 'Switch Example',
                'renderOptions': {'renderType': 'switch'},
            }
        ],
        data=[
            {
                'Switch Example': {
                    'checked': i % 2 == 0,
                    'checkedChildren': 'On',
                    'unCheckedChildren': 'Off',
                    'custom': 'balabalabalabala',
                }
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-switch-demo-output'),
]

...

@app.callback(
    Output('table-rerender-switch-demo-output', 'children'),
    [
        Input('table-rerender-switch-demo', 'recentlySwitchDataIndex'),
        Input('table-rerender-switch-demo', 'recentlySwitchStatus'),
        Input('table-rerender-switch-demo', 'recentlySwitchRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_switch_demo(
    recentlySwitchDataIndex, recentlySwitchStatus, recentlySwitchRow
):
    return json.dumps(
        dict(
            recentlySwitchDataIndex=recentlySwitchDataIndex,
            recentlySwitchStatus=recentlySwitchStatus,
            recentlySwitchRow=recentlySwitchRow,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
