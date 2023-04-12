import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    Output('mentions-demo-output', 'children'),
    [Input('mentions-demo', 'value'),
     Input('mentions-demo', 'selectedOptions')]
)
def mentions_demo(value, selectedOptions):

    return [
        fac.AntdText(
            f'value: {value}'
        ),
        fac.AntdText(
            f'selectedOptions: {selectedOptions}'
        )
    ]
