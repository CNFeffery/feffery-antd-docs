from datetime import datetime, timedelta

import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        demo_contents = fac.AntdDatePicker(id="date-picker-dynamic-forbidden-demo")
    else:
        demo_contents = fac.AntdDatePicker(
            id="date-picker-dynamic-forbidden-demo", locale="en-us"
        )

    return demo_contents


@app.callback(
    Output("date-picker-dynamic-forbidden-demo", "disabledDatesStrategy"),
    Input("date-picker-dynamic-forbidden-demo", "id"),
)
def date_picker_dynamic_forbidden_demo(_):
    return [
        {
            "mode": "lt",
            "target": "specific-date",
            "value": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "mode": "gt",
            "target": "specific-date",
            "value": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
        },
    ]


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    return [
        {
            "code": """
from datetime import datetime, timedelta

...

fac.AntdDatePicker(id='date-picker-dynamic-forbidden-demo')

...

@app.callback(
    Output('date-picker-dynamic-forbidden-demo', 'disabledDatesStrategy'),
    Input('date-picker-dynamic-forbidden-demo', 'id'),
)
def date_picker_dynamic_forbidden_demo(_):

    return [
        {
            'mode': 'lt',
            'target': 'specific-date',
            'value': datetime.now().strftime('%Y-%m-%d'),
        },
        {
            'mode': 'gt',
            'target': 'specific-date',
            'value': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
        },
    ]
"""
        }
    ]
