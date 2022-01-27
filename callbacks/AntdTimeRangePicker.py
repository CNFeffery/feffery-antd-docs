import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('time-range-picker-demo-output', 'children'),
    Input('time-range-picker-demo', 'value'),
    prevent_initial_call=True
)
def time_range_picker_demo_callback(value):
    return [
        fac.AntdText('value: ', strong=True),
        fac.AntdText(f'{value[0]} ~ {value[1]}')
    ]
