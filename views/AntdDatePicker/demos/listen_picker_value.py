import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDatePicker(
                    id="date-picker-listen-picker-value-demo",
                    style={"width": 175},
                ),
                fac.AntdText(id="date-picker-listen-picker-value-demo-output"),
            ]
        )
    else:
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDatePicker(
                    id="date-picker-listen-picker-value-demo",
                    style={"width": 175},
                    locale="en-us",
                ),
                fac.AntdText(id="date-picker-listen-picker-value-demo-output"),
            ]
        )

    return demo_contents


@app.callback(
    Output("date-picker-listen-picker-value-demo-output", "children"),
    Input("date-picker-listen-picker-value-demo", "pickerValue"),
)
def show_picker_value(pickerValue):
    return f"pickerValue: {pickerValue}"


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
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
    else:
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdDatePicker(
            id='date-picker-listen-picker-value-demo',
            style={'width': 175},
            locale='en-us',
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
