import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app
from config import Config


@app.callback(
    Output('icon-demo', 'children'),
    Input('icon-category', 'value')
)
def icon_demo_render_callback(value):
    return [
        fac.AntdCol(
            fac.AntdSpace(
                [
                    fuc.FefferyLazyLoad(
                        fac.AntdIcon(
                            icon=icon,
                            style={
                                'fontSize': '28px'
                            }
                        ),
                        height=44
                    ),
                    fac.AntdText(
                        icon,
                        copyable=True,
                        style={
                            'borderBottom': '1px dashed #e1dfdd'
                        }
                    )
                ],
                direction='vertical',
                size=0,
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                    'marginBottom': '5px'
                }
            ),
            span=8
        )
        for icon in Config.icon_map_dict[value]
    ]


@app.callback(
    Output('icon-click-demo-output', 'children'),
    Input('icon-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def icon_click_demo(nClicks):

    return f'nClicks: {nClicks}'


@app.callback(
    Output('icon-debounce-click-demo-output', 'children'),
    Input('icon-debounce-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def icon_debounce_click_demo(nClicks):

    return f'nClicks: {nClicks}'
