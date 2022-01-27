import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('time-picker-demo-output', 'children'),
    Input('time-picker-demo', 'value'),
    prevent_initial_call=True
)
def time_picker_demo_callback(value):
    return [
        fac.AntdText('value: ', strong=True),
        fac.AntdText(value)
    ]
