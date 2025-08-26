import json

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output, State

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = [
            fac.AntdTable(
                id="table-rerender-dropdown-demo",
                columns=[
                    {
                        "title": "dropdown示例1",
                        "dataIndex": "dropdown示例1",
                        "renderOptions": {"renderType": "dropdown"},
                    },
                    {
                        "title": "dropdown示例2",
                        "dataIndex": "dropdown示例2",
                        "renderOptions": {
                            "renderType": "dropdown",
                            "dropdownProps": {"title": "更多"},
                        },
                    },
                ],
                data=[
                    {
                        "dropdown示例1": [
                            {
                                "title": f"示例1-{i}-{j}",
                                "custom": "balabalabalabala",
                            }
                            for j in range(1, 6)
                        ],
                        "dropdown示例2": [
                            {
                                "title": f"示例2-{i}-{j}",
                                "custom": "balabalabalabala",
                            }
                            for j in range(1, 6)
                        ],
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={"width": 200},
            ),
            html.Pre(id="table-rerender-dropdown-demo-output"),
        ]

    elif current_locale == "en-us":
        demo_contents = [
            fac.AntdTable(
                id="table-rerender-dropdown-demo",
                locale="en-us",
                columns=[
                    {
                        "title": "Dropdown Example 1",
                        "dataIndex": "Dropdown Example 1",
                        "renderOptions": {"renderType": "dropdown"},
                    },
                    {
                        "title": "Dropdown Example 2",
                        "dataIndex": "Dropdown Example 2",
                        "renderOptions": {
                            "renderType": "dropdown",
                            "dropdownProps": {"title": "More"},
                        },
                    },
                ],
                data=[
                    {
                        "Dropdown Example 1": [
                            {
                                "title": f"Example1-{i}-{j}",
                                "custom": "balabalabalabala",
                            }
                            for j in range(1, 6)
                        ],
                        "Dropdown Example 2": [
                            {
                                "title": f"Example2-{i}-{j}",
                                "custom": "balabalabalabala",
                            }
                            for j in range(1, 6)
                        ],
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={"width": 200},
            ),
            html.Pre(id="table-rerender-dropdown-demo-output"),
        ]

    return demo_contents


@app.callback(
    Output("table-rerender-dropdown-demo-output", "children"),
    Input("table-rerender-dropdown-demo", "nClicksDropdownItem"),
    [
        State("table-rerender-dropdown-demo", "recentlyClickedDropdownItemTitle"),
        State(
            "table-rerender-dropdown-demo",
            "recentlyDropdownItemClickedDataIndex",
        ),
        State("table-rerender-dropdown-demo", "recentlyDropdownItemClickedRow"),
    ],
    prevent_initial_call=True,
)
def table_rerender_dropdown_demo(
    nClicksDropdownItem,
    recentlyClickedDropdownItemTitle,
    recentlyDropdownItemClickedDataIndex,
    recentlyDropdownItemClickedRow,
):
    return json.dumps(
        dict(
            nClicksDropdownItem=nClicksDropdownItem,
            recentlyClickedDropdownItemTitle=recentlyClickedDropdownItemTitle,
            recentlyDropdownItemClickedDataIndex=recentlyDropdownItemClickedDataIndex,
            recentlyDropdownItemClickedRow=recentlyDropdownItemClickedRow,
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
        id='table-rerender-dropdown-demo',
        columns=[
            {
                'title': 'dropdown示例1',
                'dataIndex': 'dropdown示例1',
                'renderOptions': {'renderType': 'dropdown'},
            },
            {
                'title': 'dropdown示例2',
                'dataIndex': 'dropdown示例2',
                'renderOptions': {
                    'renderType': 'dropdown',
                    'dropdownProps': {'title': '更多'},
                },
            },
        ],
        data=[
            {
                'dropdown示例1': [
                    {
                        'title': f'示例1-{i}-{j}',
                        'custom': 'balabalabalabala',
                    }
                    for j in range(1, 6)
                ],
                'dropdown示例2': [
                    {
                        'title': f'示例2-{i}-{j}',
                        'custom': 'balabalabalabala',
                    }
                    for j in range(1, 6)
                ],
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-dropdown-demo-output'),
]

...

@app.callback(
    Output('table-rerender-dropdown-demo-output', 'children'),
    Input('table-rerender-dropdown-demo', 'nClicksDropdownItem'),
    [
        State(
            'table-rerender-dropdown-demo', 'recentlyClickedDropdownItemTitle'
        ),
        State(
            'table-rerender-dropdown-demo',
            'recentlyDropdownItemClickedDataIndex',
        ),
        State('table-rerender-dropdown-demo', 'recentlyDropdownItemClickedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_dropdown_demo(
    nClicksDropdownItem,
    recentlyClickedDropdownItemTitle,
    recentlyDropdownItemClickedDataIndex,
    recentlyDropdownItemClickedRow,
):
    return json.dumps(
        dict(
            nClicksDropdownItem=nClicksDropdownItem,
            recentlyClickedDropdownItemTitle=recentlyClickedDropdownItemTitle,
            recentlyDropdownItemClickedDataIndex=recentlyDropdownItemClickedDataIndex,
            recentlyDropdownItemClickedRow=recentlyDropdownItemClickedRow,
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
        id='table-rerender-dropdown-demo',
        locale='en-us',
        columns=[
            {
                'title': 'Dropdown Example 1',
                'dataIndex': 'Dropdown Example 1',
                'renderOptions': {'renderType': 'dropdown'},
            },
            {
                'title': 'Dropdown Example 2',
                'dataIndex': 'Dropdown Example 2',
                'renderOptions': {
                    'renderType': 'dropdown',
                    'dropdownProps': {'title': 'More'},
                },
            },
        ],
        data=[
            {
                'Dropdown Example 1': [
                    {
                        'title': f'Example1-{i}-{j}',
                        'custom': 'balabalabalabala',
                    }
                    for j in range(1, 6)
                ],
                'Dropdown Example 2': [
                    {
                        'title': f'Example2-{i}-{j}',
                        'custom': 'balabalabalabala',
                    }
                    for j in range(1, 6)
                ],
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-dropdown-demo-output'),
]

...

@app.callback(
    Output('table-rerender-dropdown-demo-output', 'children'),
    Input('table-rerender-dropdown-demo', 'nClicksDropdownItem'),
    [
        State('table-rerender-dropdown-demo', 'recentlyClickedDropdownItemTitle'),
        State('table-rerender-dropdown-demo', 'recentlyDropdownItemClickedDataIndex'),
        State('table-rerender-dropdown-demo', 'recentlyDropdownItemClickedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_dropdown_demo(
    nClicksDropdownItem,
    recentlyClickedDropdownItemTitle,
    recentlyDropdownItemClickedDataIndex,
    recentlyDropdownItemClickedRow,
):
    return json.dumps(
        dict(
            nClicksDropdownItem=nClicksDropdownItem,
            recentlyClickedDropdownItemTitle=recentlyClickedDropdownItemTitle,
            recentlyDropdownItemClickedDataIndex=recentlyDropdownItemClickedDataIndex,
            recentlyDropdownItemClickedRow=recentlyDropdownItemClickedRow,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
