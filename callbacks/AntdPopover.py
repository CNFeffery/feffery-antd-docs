import feffery_antd_components as fac
from dash.dependencies import Input, Output

from server import app


@app.callback(
    [Output('popover-color-demo', 'color'),
     Output('popover-color-demo', 'content')],
    Input('popover-color-demo-input', 'color')
)
def popover_color_demo(color):

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
