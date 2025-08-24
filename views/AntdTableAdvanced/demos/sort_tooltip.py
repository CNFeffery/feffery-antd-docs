import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        label = {
            "int": "int型示例",
            "float": "float型示例",
            "str": "str型示例",
            "dt": "日期时间示例",
        }
        sample_str = lambda i: f"示例字符{i}"
    else:  # en-us fallback
        label = {
            "int": "Integer Example",
            "float": "Float Example",
            "str": "String Example",
            "dt": "Datetime Example",
        }
        sample_str = lambda i: f"Sample Text {i}"

    columns = [
        {"title": label["int"], "dataIndex": label["int"], "width": "25%"},
        {"title": label["float"], "dataIndex": label["float"], "width": "25%"},
        {"title": label["str"], "dataIndex": label["str"], "width": "25%"},
        {"title": label["dt"], "dataIndex": label["dt"], "width": "25%"},
    ]

    data = [
        {
            label["int"]: i,
            label["float"]: round(i * 0.1, 1),
            label["str"]: sample_str(i),
            label["dt"]: f"2099-01-0{i}",
        }
        for i in [4, 2, 1, 5, 3]
    ]

    demo_contents = fac.AntdSpace(
        [
            fac.AntdFormItem(
                fac.AntdSwitch(
                    id="table-sort-tooltip-demo-show-sorter-tooltip",
                    checked=True,
                ),
                label="showSorterTooltip",
                layout="horizontal",
                style={"margin": 0},
            ),
            fac.AntdFormItem(
                fac.AntdRadioGroup(
                    id="table-sort-tooltip-demo-show-sorter-tooltip-target",
                    options=["full-header", "sorter-icon"],
                    value="full-header",
                ),
                label="showSorterTooltipTarget",
                layout="horizontal",
                style={"margin": 0},
            ),
            fac.AntdTable(
                id="table-sort-tooltip-demo",
                columns=columns,
                data=data,
                sortOptions={
                    "sortDataIndexes": [
                        label["int"],
                        label["float"],
                        label["str"],
                        label["dt"],
                    ]
                },
            ),
        ],
        direction="vertical",
        style={"width": "100%"},
    )

    return demo_contents


app.clientside_callback(
    """(showSorterTooltip, showSorterTooltipTarget) => [showSorterTooltip, showSorterTooltipTarget]""",
    [
        Output("table-sort-tooltip-demo", "showSorterTooltip"),
        Output("table-sort-tooltip-demo", "showSorterTooltipTarget"),
    ],
    [
        Input("table-sort-tooltip-demo-show-sorter-tooltip", "checked"),
        Input("table-sort-tooltip-demo-show-sorter-tooltip-target", "value"),
    ],
)


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    from i18n import get_current_locale

    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": '''
fac.AntdSpace(
    [
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='table-sort-tooltip-demo-show-sorter-tooltip',
                checked=True,
            ),
            label='showSorterTooltip',
            layout='horizontal',
            style={'margin': 0},
        ),
        fac.AntdFormItem(
            fac.AntdRadioGroup(
                id='table-sort-tooltip-demo-show-sorter-tooltip-target',
                options=['full-header', 'sorter-icon'],
                value='full-header',
            ),
            label='showSorterTooltipTarget',
            layout='horizontal',
            style={'margin': 0},
        ),
        fac.AntdTable(
            id='table-sort-tooltip-demo',
            columns=[
                {'title': 'int型示例', 'dataIndex': 'int型示例', 'width': '25%'},
                {'title': 'float型示例', 'dataIndex': 'float型示例', 'width': '25%'},
                {'title': 'str型示例', 'dataIndex': 'str型示例', 'width': '25%'},
                {'title': '日期时间示例', 'dataIndex': '日期时间示例', 'width': '25%'},
            ],
            data=[
                {
                    'int型示例': i,
                    'float型示例': round(i * 0.1, 1),
                    'str型示例': f'示例字符{i}',
                    '日期时间示例': f'2099-01-0{i}',
                }
                for i in [4, 2, 1, 5, 3]
            ],
            sortOptions={
                'sortDataIndexes': ['int型示例', 'float型示例', 'str型示例', '日期时间示例']
            },
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

app.clientside_callback(
    """(showSorterTooltip, showSorterTooltipTarget) => [showSorterTooltip, showSorterTooltipTarget]""",
    [
        Output('table-sort-tooltip-demo', 'showSorterTooltip'),
        Output('table-sort-tooltip-demo', 'showSorterTooltipTarget'),
    ],
    [
        Input('table-sort-tooltip-demo-show-sorter-tooltip', 'checked'),
        Input('table-sort-tooltip-demo-show-sorter-tooltip-target', 'value'),
    ],
)
'''
            }
        ]
    else:  # en-us
        return [
            {
                "code": '''
fac.AntdSpace(
    [
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='table-sort-tooltip-demo-show-sorter-tooltip',
                checked=True,
            ),
            label='showSorterTooltip',
            layout='horizontal',
            style={'margin': 0},
        ),
        fac.AntdFormItem(
            fac.AntdRadioGroup(
                id='table-sort-tooltip-demo-show-sorter-tooltip-target',
                options=['full-header', 'sorter-icon'],
                value='full-header',
            ),
            label='showSorterTooltipTarget',
            layout='horizontal',
            style={'margin': 0},
        ),
        fac.AntdTable(
            id='table-sort-tooltip-demo',
            columns=[
                {'title': 'Integer Example', 'dataIndex': 'Integer Example', 'width': '25%'},
                {'title': 'Float Example', 'dataIndex': 'Float Example', 'width': '25%'},
                {'title': 'String Example', 'dataIndex': 'String Example', 'width': '25%'},
                {'title': 'Datetime Example', 'dataIndex': 'Datetime Example', 'width': '25%'},
            ],
            data=[
                {
                    'Integer Example': i,
                    'Float Example': round(i * 0.1, 1),
                    'String Example': f'Sample Text {i}',
                    'Datetime Example': f'2099-01-0{i}',
                }
                for i in [4, 2, 1, 5, 3]
            ],
            sortOptions={
                'sortDataIndexes': ['Integer Example', 'Float Example', 'String Example', 'Datetime Example']
            },
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

app.clientside_callback(
    """(showSorterTooltip, showSorterTooltipTarget) => [showSorterTooltip, showSorterTooltipTarget]""",
    [
        Output('table-sort-tooltip-demo', 'showSorterTooltip'),
        Output('table-sort-tooltip-demo', 'showSorterTooltipTarget'),
    ],
    [
        Input('table-sort-tooltip-demo-show-sorter-tooltip', 'checked'),
        Input('table-sort-tooltip-demo-show-sorter-tooltip-target', 'value'),
    ],
)
'''
            }
        ]
