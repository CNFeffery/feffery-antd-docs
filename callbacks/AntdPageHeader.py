import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('page-header-demo', 'children'),
    Input('page-header-demo', 'backClicks')
)
def page_header_demo_callback(backClicks):
    return [
        fac.AntdText('backClicks: ', strong=True),
        fac.AntdText(backClicks)
    ]
