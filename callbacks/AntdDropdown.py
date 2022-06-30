import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'),
     Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText(', nClicks: ', strong=True),
        fac.AntdText(nClicks)
    ]
