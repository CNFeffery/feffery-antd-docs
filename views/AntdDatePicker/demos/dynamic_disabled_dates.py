import feffery_antd_components as fac
from datetime import datetime, timedelta
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDatePicker(id='date-picker-dynamic-forbidden-demo')

    return demo_contents


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


code_string = [
    {
        'code': """
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
