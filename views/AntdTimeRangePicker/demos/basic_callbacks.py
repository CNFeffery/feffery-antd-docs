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
                    fac.AntdTimeRangePicker(
                        id='time-range-picker-demo',
                        defaultValue=['12:00:00', '13:00:00'],
                    ),
                    fac.AntdText(id='time-range-picker-demo-output'),
                ],
                align='center',
            ),
            fac.AntdSpace(
                [
                    fac.AntdTimeRangePicker(
                        id='time-range-picker-format-demo',
                        defaultValue=['12时00分00秒', '13时00分00秒'],
                        format='HH时mm分ss秒',
                    ),
                    fac.AntdText(id='time-range-picker-format-demo-output'),
                ],
                align='center',
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('time-range-picker-demo-output', 'children'),
    Input('time-range-picker-demo', 'value'),
)
def time_range_picker_demo(value):
    return f'value: {value}'


@app.callback(
    Output('time-range-picker-format-demo-output', 'children'),
    Input('time-range-picker-format-demo', 'value'),
)
def time_range_picker_format_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdTimeRangePicker(
                    id='time-range-picker-demo',
                    defaultValue=['12:00:00', '13:00:00'],
                ),
                fac.AntdText(id='time-range-picker-demo-output'),
            ],
            align='center',
        ),
        fac.AntdSpace(
            [
                fac.AntdTimeRangePicker(
                    id='time-range-picker-format-demo',
                    defaultValue=['12时00分00秒', '13时00分00秒'],
                    format='HH时mm分ss秒',
                ),
                fac.AntdText(id='time-range-picker-format-demo-output'),
            ],
            align='center',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('time-range-picker-demo-output', 'children'),
    Input('time-range-picker-demo', 'value'),
)
def time_range_picker_demo(value):
    return f'value: {value}'


@app.callback(
    Output('time-range-picker-format-demo-output', 'children'),
    Input('time-range-picker-format-demo', 'value'),
)
def time_range_picker_format_demo(value):
    return f'value: {value}'
"""
    }
]
