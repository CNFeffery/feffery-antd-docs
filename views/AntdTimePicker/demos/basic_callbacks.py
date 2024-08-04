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
                    fac.AntdTimePicker(
                        id='time-picker-demo', defaultValue='06:00:00'
                    ),
                    fac.AntdText(id='time-picker-demo-output'),
                ],
                align='center',
            ),
            fac.AntdSpace(
                [
                    fac.AntdTimePicker(
                        id='time-picker-format-demo',
                        defaultValue='06时00分00秒',
                        format='HH时mm分ss秒',
                    ),
                    fac.AntdText(id='time-picker-format-demo-output'),
                ],
                align='center',
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('time-picker-demo-output', 'children'),
    Input('time-picker-demo', 'value'),
)
def time_picker_demo(value):
    return f'value: {value}'


@app.callback(
    Output('time-picker-format-demo-output', 'children'),
    Input('time-picker-format-demo', 'value'),
)
def time_picker_format_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdTimePicker(
                    id='time-picker-demo', defaultValue='06:00:00'
                ),
                fac.AntdText(id='time-picker-demo-output'),
            ],
            align='center',
        ),
        fac.AntdSpace(
            [
                fac.AntdTimePicker(
                    id='time-picker-format-demo',
                    defaultValue='06时00分00秒',
                    format='HH时mm分ss秒',
                ),
                fac.AntdText(id='time-picker-format-demo-output'),
            ],
            align='center',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('time-picker-demo-output', 'children'),
    Input('time-picker-demo', 'value'),
)
def time_picker_demo(value):
    return f'value: {value}'


@app.callback(
    Output('time-picker-format-demo-output', 'children'),
    Input('time-picker-format-demo', 'value'),
)
def time_picker_format_demo(value):
    return f'value: {value}'
"""
    }
]
