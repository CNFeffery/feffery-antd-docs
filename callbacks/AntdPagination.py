import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('pagination-demo-output', 'children'),
    [Input('pagination-demo', 'current'),
     Input('pagination-demo', 'pageSize')]
)
def pagination_callback_demo(current, pageSize):
    import time;time.sleep(1)
    return [
        fac.AntdText(f'内容项{i}')
        for i in range((current - 1) * pageSize, current * pageSize)
    ]
