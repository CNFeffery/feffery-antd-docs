from i18n import get_current_locale
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
                        defaultValue=(
                            '06h00m00s'
                            if get_current_locale() == 'en-us'
                            else '06时00分00秒'
                        ),
                        format=(
                            'HH[h]mm[m]ss[s]'
                            if get_current_locale() == 'en-us'
                            else 'HH时mm分ss秒'
                        ),
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


def code_string():
    codes = [
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

    if get_current_locale() == 'en-us':
        for item in codes:
            item['code'] = item['code'].replace(
                'HH时mm分ss秒', 'HH[h]mm[m]ss[s]'
            )
            item['code'] = item['code'].replace('06时00分00秒', '06h00m00s')
    return codes
