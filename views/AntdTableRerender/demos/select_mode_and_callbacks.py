import json

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = [
            fac.AntdTable(
                id='table-rerender-select-demo',
                columns=[
                    {
                        'title': 'select示例1',
                        'dataIndex': 'select示例1',
                        'renderOptions': {'renderType': 'select'},
                        'width': 'calc(100% / 3)',
                    },
                    {
                        'title': 'select示例2',
                        'dataIndex': 'select示例2',
                        'renderOptions': {'renderType': 'select'},
                        'width': 'calc(100% / 3)',
                    },
                    {
                        'title': 'select示例3',
                        'dataIndex': 'select示例3',
                        'renderOptions': {'renderType': 'select'},
                        'width': 'calc(100% / 3)',
                    },
                ],
                data=[
                    {
                        'select示例1': {
                            'options': [
                                {'label': f'选项{j}', 'value': f'选项{j}'}
                                for j in range(5)
                            ],
                            'allowClear': True,
                            'placeholder': '请选择',
                        },
                        'select示例2': {
                            'options': [
                                {'label': f'选项{j}', 'value': f'选项{j}'}
                                for j in range(5)
                            ],
                            'mode': 'multiple',
                            'allowClear': True,
                            'placeholder': '请选择',
                        },
                        'select示例3': {
                            'options': [
                                {'label': f'选项{j}', 'value': f'选项{j}'}
                                for j in range(5)
                            ],
                            'mode': 'tags',
                            'allowClear': True,
                            'placeholder': '请选择',
                        },
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={'width': 600},
            ),
            html.Pre(id='table-rerender-select-demo-output'),
        ]

    elif current_locale == 'en-us':
        demo_contents = [
            fac.AntdTable(
                id='table-rerender-select-demo',
                locale='en-us',
                columns=[
                    {
                        'title': 'select Example 1',
                        'dataIndex': 'select Example 1',
                        'renderOptions': {'renderType': 'select'},
                        'width': 'calc(100% / 3)',
                    },
                    {
                        'title': 'select Example 2',
                        'dataIndex': 'select Example 2',
                        'renderOptions': {'renderType': 'select'},
                        'width': 'calc(100% / 3)',
                    },
                    {
                        'title': 'select Example 3',
                        'dataIndex': 'select Example 3',
                        'renderOptions': {'renderType': 'select'},
                        'width': 'calc(100% / 3)',
                    },
                ],
                data=[
                    {
                        'select Example 1': {
                            'options': [
                                {'label': f'Option {j}', 'value': f'Option {j}'}
                                for j in range(5)
                            ],
                            'allowClear': True,
                            'placeholder': 'Please select',
                        },
                        'select Example 2': {
                            'options': [
                                {'label': f'Option {j}', 'value': f'Option {j}'}
                                for j in range(5)
                            ],
                            'mode': 'multiple',
                            'allowClear': True,
                            'placeholder': 'Please select',
                        },
                        'select Example 3': {
                            'options': [
                                {'label': f'Option {j}', 'value': f'Option {j}'}
                                for j in range(5)
                            ],
                            'mode': 'tags',
                            'allowClear': True,
                            'placeholder': 'Please select',
                        },
                    }
                    for i in range(1, 4)
                ],
                bordered=True,
                style={'width': 600},
            ),
            html.Pre(id='table-rerender-select-demo-output'),
        ]

    return demo_contents


@app.callback(
    Output('table-rerender-select-demo-output', 'children'),
    [
        Input('table-rerender-select-demo', 'recentlySelectRow'),
        Input('table-rerender-select-demo', 'recentlySelectDataIndex'),
        Input('table-rerender-select-demo', 'recentlySelectValue'),
    ],
    prevent_initial_call=True,
)
def table_rerender_select_demo(
    recentlySelectRow, recentlySelectDataIndex, recentlySelectValue
):
    return json.dumps(
        dict(
            recentlySelectRow=recentlySelectRow,
            recentlySelectDataIndex=recentlySelectDataIndex,
            recentlySelectValue=recentlySelectValue,
        ),
        indent=4,
        ensure_ascii=False,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdTable(
        id='table-rerender-select-demo',
        columns=[
            {
                'title': 'select示例1',
                'dataIndex': 'select示例1',
                'renderOptions': {'renderType': 'select'},
                'width': 'calc(100% / 3)',
            },
            {
                'title': 'select示例2',
                'dataIndex': 'select示例2',
                'renderOptions': {'renderType': 'select'},
                'width': 'calc(100% / 3)',
            },
            {
                'title': 'select示例3',
                'dataIndex': 'select示例3',
                'renderOptions': {'renderType': 'select'},
                'width': 'calc(100% / 3)',
            },
        ],
        data=[
            {
                'select示例1': {
                    'options': [
                        {'label': f'选项{j}', 'value': f'选项{j}'}
                        for j in range(5)
                    ],
                    'allowClear': True,
                    'placeholder': '请选择',
                },
                'select示例2': {
                    'options': [
                        {'label': f'选项{j}', 'value': f'选项{j}'}
                        for j in range(5)
                    ],
                    'mode': 'multiple',
                    'allowClear': True,
                    'placeholder': '请选择',
                },
                'select示例3': {
                    'options': [
                        {'label': f'选项{j}', 'value': f'选项{j}'}
                        for j in range(5)
                    ],
                    'mode': 'tags',
                    'allowClear': True,
                    'placeholder': '请选择',
                },
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 600},
    ),
    html.Pre(id='table-rerender-select-demo-output'),
]

...

@app.callback(
    Output('table-rerender-select-demo-output', 'children'),
    [
        Input('table-rerender-select-demo', 'recentlySelectRow'),
        Input('table-rerender-select-demo', 'recentlySelectDataIndex'),
        Input('table-rerender-select-demo', 'recentlySelectValue'),
    ],
    prevent_initial_call=True,
)
def table_rerender_select_demo(
    recentlySelectRow, recentlySelectDataIndex, recentlySelectValue
):
    return json.dumps(
        dict(
            recentlySelectRow=recentlySelectRow,
            recentlySelectDataIndex=recentlySelectDataIndex,
            recentlySelectValue=recentlySelectValue,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdTable(
        id='table-rerender-select-demo',
        locale="en-us",
        columns=[
            {
                'title': 'select Example 1',
                'dataIndex': 'select Example 1',
                'renderOptions': {'renderType': 'select'},
                'width': 'calc(100% / 3)',
            },
            {
                'title': 'select Example 2',
                'dataIndex': 'select Example 2',
                'renderOptions': {'renderType': 'select'},
                'width': 'calc(100% / 3)',
            },
            {
                'title': 'select Example 3',
                'dataIndex': 'select Example 3',
                'renderOptions': {'renderType': 'select'},
                'width': 'calc(100% / 3)',
            },
        ],
        data=[
            {
                'select Example 1': {
                    'options': [
                        {'label': f'Option {j}', 'value': f'Option {j}'}
                        for j in range(5)
                    ],
                    'allowClear': True,
                    'placeholder': 'Please select',
                },
                'select Example 2': {
                    'options': [
                        {'label': f'Option {j}', 'value': f'Option {j}'}
                        for j in range(5)
                    ],
                    'mode': 'multiple',
                    'allowClear': True,
                    'placeholder': 'Please select',
                },
                'select Example 3': {
                    'options': [
                        {'label': f'Option {j}', 'value': f'Option {j}'}
                        for j in range(5)
                    ],
                    'mode': 'tags',
                    'allowClear': True,
                    'placeholder': 'Please select',
                },
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 600},
    ),
    html.Pre(id='table-rerender-select-demo-output'),
]

...

@app.callback(
    Output('table-rerender-select-demo-output', 'children'),
    [
        Input('table-rerender-select-demo', 'recentlySelectRow'),
        Input('table-rerender-select-demo', 'recentlySelectDataIndex'),
        Input('table-rerender-select-demo', 'recentlySelectValue'),
    ],
    prevent_initial_call=True,
)
def table_rerender_select_demo(
    recentlySelectRow, recentlySelectDataIndex, recentlySelectValue
):
    return json.dumps(
        dict(
            recentlySelectRow=recentlySelectRow,
            recentlySelectDataIndex=recentlySelectDataIndex,
            recentlySelectValue=recentlySelectValue,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
