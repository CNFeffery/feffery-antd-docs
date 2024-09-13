import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDatePicker(
                id='date-picker-listen-picker-value-demo',
                style={'width': 175},
            ),
            fac.AntdText(id='date-picker-listen-picker-value-demo-output'),
        ]
    )

    return demo_contents


@app.callback(
    Output('date-picker-listen-picker-value-demo-output', 'children'),
    Input('date-picker-listen-picker-value-demo', 'pickerValue'),
)
def show_picker_value(pickerValue):
    return f'pickerValue: {pickerValue}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDatePicker(
            id='date-picker-listen-picker-value-demo',
            style={'width': 175},
        ),
        fac.AntdText(id='date-picker-listen-picker-value-demo-output'),
    ]
)

...

@app.callback(
    Output('date-picker-listen-picker-value-demo-output', 'children'),
    Input('date-picker-listen-picker-value-demo', 'pickerValue'),
)
def show_picker_value(pickerValue):
    return f'pickerValue: {pickerValue}'
"""
    }
]
