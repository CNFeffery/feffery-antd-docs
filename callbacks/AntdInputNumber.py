from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app


@app.callback(
    Output('input-number-demo-output', 'children'),
    [Input('input-number-demo1', 'nSubmit'),
     Input('input-number-demo2', 'nSubmit')],
    [State('input-number-demo1', 'value'),
     State('input-number-demo2', 'value')],
    prevent_initial_call=True
)
def input_number_callback(nSubmit1, nSubmit2, value1, value2):
    return [
        html.Div(
            [
                fac.AntdText('常规模式value：', strong=True),
                fac.AntdText(str(value1))
            ]
        ),
        html.Div(
            [
                fac.AntdText('常规模式value类型：', strong=True),
                fac.AntdText(str(type(value1)))
            ]
        ),
        fac.AntdDivider(),
        html.Div(
            [
                fac.AntdText('高精度模式value：', strong=True),
                fac.AntdText(str(value2))
            ]
        ),
        html.Div(
            [
                fac.AntdText('高精度模式value类型：', strong=True),
                fac.AntdText(str(type(value2)))
            ]
        )
    ]
