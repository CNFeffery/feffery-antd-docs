import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdDateRangePicker(
                        id='date-range-picker-demo1',
                        style={'width': 300},
                    ),
                    fac.AntdText(id='date-range-picker-demo1-output'),
                ],
                align='center',
            ),
            fac.AntdSpace(
                [
                    fac.AntdDateRangePicker(
                        id='date-range-picker-demo2',
                        placeholder=['开始日期时间', '结束日期时间'],
                        style={'width': 350},
                        showTime=True,
                        needConfirm=True,
                    ),
                    fac.AntdText(id='date-range-picker-demo2-output'),
                ],
                align='center',
            ),
            fac.AntdSpace(
                [
                    fac.AntdDateRangePicker(
                        id='date-range-picker-demo3',
                        placeholder=['配合自定义format', ''],
                        format='YYYY年MM月DD日',
                        style={'width': 300},
                    ),
                    fac.AntdText(id='date-range-picker-demo3-output'),
                ],
                align='center',
            ),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('date-range-picker-demo1-output', 'children'),
    Input('date-range-picker-demo1', 'value'),
)
def date_range_picker_demo1(value):
    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo2-output', 'children'),
    Input('date-range-picker-demo2', 'value'),
)
def date_range_picker_demo2(value):
    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo3-output', 'children'),
    Input('date-range-picker-demo3', 'value'),
)
def date_range_picker_demo3(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdDateRangePicker(
                    id='date-range-picker-demo1',
                    style={'width': 300},
                ),
                fac.AntdText(id='date-range-picker-demo1-output'),
            ],
            align='center',
        ),
        fac.AntdSpace(
            [
                fac.AntdDateRangePicker(
                    id='date-range-picker-demo2',
                    placeholder=['开始日期时间', '结束日期时间'],
                    style={'width': 350},
                    showTime=True,
                    needConfirm=True,
                ),
                fac.AntdText(id='date-range-picker-demo2-output'),
            ],
            align='center',
        ),
        fac.AntdSpace(
            [
                fac.AntdDateRangePicker(
                    id='date-range-picker-demo3',
                    placeholder=['配合自定义format', ''],
                    format='YYYY年MM月DD日',
                    style={'width': 300},
                ),
                fac.AntdText(id='date-range-picker-demo3-output'),
            ],
            align='center',
        ),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('date-range-picker-demo1-output', 'children'),
    Input('date-range-picker-demo1', 'value'),
)
def date_range_picker_demo1(value):
    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo2-output', 'children'),
    Input('date-range-picker-demo2', 'value'),
)
def date_range_picker_demo2(value):
    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo3-output', 'children'),
    Input('date-range-picker-demo3', 'value'),
)
def date_range_picker_demo3(value):
    return f'value: {value}'
"""
    }
]
