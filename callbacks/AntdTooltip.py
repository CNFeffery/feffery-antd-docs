import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('tooltip-color-demo', 'color'),
     Output('tooltip-color-demo', 'title')],
    Input('tooltip-color-demo-input', 'color')
)
def tooltip_color_demo(color):

    return [
        color,
        fac.AntdParagraph(
            [
                '当前color: ',
                fac.AntdText(
                    color,
                    copyable=True
                )
            ]
        )
    ]
