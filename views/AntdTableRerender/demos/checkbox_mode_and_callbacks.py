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
                id="table-rerender-checkbox-demo",
                columns=[
                    {
                        "title": "checkbox示例",
                        "dataIndex": "checkbox示例",
                        "renderOptions": {"renderType": "checkbox"},
                    }
                ],
                data=[
                    {
                        "checkbox示例": {
                            "checked": i % 2 == 0,
                            "label": f"选项{i}",
                            "custom": "balabalabalabala",
                        }
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={"width": 200},
            ),
            html.Pre(id="table-rerender-checkbox-demo-output"),
        ]

    elif current_locale == "en-us":
        demo_contents = [
            fac.AntdTable(
                id="table-rerender-checkbox-demo",
                locale="en-us",
                columns=[
                    {
                        "title": "Checkbox Example",
                        "dataIndex": "Checkbox Example",
                        "renderOptions": {"renderType": "checkbox"},
                    }
                ],
                data=[
                    {
                        "Checkbox Example": {
                            "checked": i % 2 == 0,
                            "label": f"Option {i}",
                            "custom": "balabalabalabala",
                        }
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={"width": 200},
            ),
            html.Pre(id="table-rerender-checkbox-demo-output"),
        ]

    return demo_contents


@app.callback(
    Output("table-rerender-checkbox-demo-output", "children"),
    [
        Input("table-rerender-checkbox-demo", "recentlyCheckedLabel"),
        Input("table-rerender-checkbox-demo", "recentlyCheckedDataIndex"),
        Input("table-rerender-checkbox-demo", "recentlyCheckedStatus"),
        Input("table-rerender-checkbox-demo", "recentlyCheckedRow"),
    ],
    prevent_initial_call=True,
)
def table_rerender_checkbox_demo(
    recentlyCheckedLabel,
    recentlyCheckedDataIndex,
    recentlyCheckedStatus,
    recentlyCheckedRow,
):
    return json.dumps(
        dict(
            recentlyCheckedLabel=recentlyCheckedLabel,
            recentlyCheckedDataIndex=recentlyCheckedDataIndex,
            recentlyCheckedStatus=recentlyCheckedStatus,
            recentlyCheckedRow=recentlyCheckedRow,
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
        id='table-rerender-checkbox-demo',
        columns=[
            {
                'title': 'checkbox示例',
                'dataIndex': 'checkbox示例',
                'renderOptions': {'renderType': 'checkbox'},
            }
        ],
        data=[
            {
                'checkbox示例': {
                    'checked': i % 2 == 0,
                    'label': f'选项{i}',
                    'custom': 'balabalabalabala',
                }
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-checkbox-demo-output'),
]

...

@app.callback(
    Output('table-rerender-checkbox-demo-output', 'children'),
    [
        Input('table-rerender-checkbox-demo', 'recentlyCheckedLabel'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedDataIndex'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedStatus'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_checkbox_demo(
    recentlyCheckedLabel,
    recentlyCheckedDataIndex,
    recentlyCheckedStatus,
    recentlyCheckedRow,
):
    return json.dumps(
        dict(
            recentlyCheckedLabel=recentlyCheckedLabel,
            recentlyCheckedDataIndex=recentlyCheckedDataIndex,
            recentlyCheckedStatus=recentlyCheckedStatus,
            recentlyCheckedRow=recentlyCheckedRow,
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
        id='table-rerender-checkbox-demo',
        locale='en-us',
        columns=[
            {
                'title': 'Checkbox Example',
                'dataIndex': 'Checkbox Example',
                'renderOptions': {'renderType': 'checkbox'},
            }
        ],
        data=[
            {
                'Checkbox Example': {
                    'checked': i % 2 == 0,
                    'label': f'Option {i}',
                    'custom': 'balabalabalabala',
                }
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-checkbox-demo-output'),
]

...

@app.callback(
    Output('table-rerender-checkbox-demo-output', 'children'),
    [
        Input('table-rerender-checkbox-demo', 'recentlyCheckedLabel'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedDataIndex'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedStatus'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_checkbox_demo(
    recentlyCheckedLabel,
    recentlyCheckedDataIndex,
    recentlyCheckedStatus,
    recentlyCheckedRow,
):
    return json.dumps(
        dict(
            recentlyCheckedLabel=recentlyCheckedLabel,
            recentlyCheckedDataIndex=recentlyCheckedDataIndex,
            recentlyCheckedStatus=recentlyCheckedStatus,
            recentlyCheckedRow=recentlyCheckedRow,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
