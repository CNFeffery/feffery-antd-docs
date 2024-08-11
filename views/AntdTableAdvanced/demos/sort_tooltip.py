import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
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
                    {
                        'title': 'int型示例',
                        'dataIndex': 'int型示例',
                        'width': '25%',
                    },
                    {
                        'title': 'float型示例',
                        'dataIndex': 'float型示例',
                        'width': '25%',
                    },
                    {
                        'title': 'str型示例',
                        'dataIndex': 'str型示例',
                        'width': '25%',
                    },
                    {
                        'title': '日期时间示例',
                        'dataIndex': '日期时间示例',
                        'width': '25%',
                    },
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
                    'sortDataIndexes': [
                        'int型示例',
                        'float型示例',
                        'str型示例',
                        '日期时间示例',
                    ]
                },
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


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


code_string = [
    {
        'code': '''
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
                {
                    'title': 'int型示例',
                    'dataIndex': 'int型示例',
                    'width': '25%',
                },
                {
                    'title': 'float型示例',
                    'dataIndex': 'float型示例',
                    'width': '25%',
                },
                {
                    'title': 'str型示例',
                    'dataIndex': 'str型示例',
                    'width': '25%',
                },
                {
                    'title': '日期时间示例',
                    'dataIndex': '日期时间示例',
                    'width': '25%',
                },
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
                'sortDataIndexes': [
                    'int型示例',
                    'float型示例',
                    'str型示例',
                    '日期时间示例',
                ]
            },
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
        
...

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
