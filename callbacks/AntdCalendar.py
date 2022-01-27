import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('calendar-demo-output', 'children'),
    Input('calendar-demo', 'value')
)
def calendar_demo_callback(value):
    return [
        fac.AntdText('value: ', strong=True),
        fac.AntdText(value)
    ]
