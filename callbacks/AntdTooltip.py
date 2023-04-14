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


app.clientside_callback(
    '''(open, permanent) => {
        return [
            open,
            permanent,
            `open=${open} permanent=${permanent}`
        ];
    }''',
    [Output('tooltip-open-demo', 'open'),
     Output('tooltip-open-demo', 'permanent'),
     Output('tooltip-open-demo', 'title')],
    [Input('tooltip-open-demo-open', 'checked'),
     Input('tooltip-open-demo-permanent', 'checked')]
)
