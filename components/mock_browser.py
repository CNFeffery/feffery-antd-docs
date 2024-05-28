from dash import html
import feffery_antd_components as fac


def render():
    """渲染演示用示意浏览器头"""

    return fac.AntdRow(
        [
            fac.AntdCol(
                fac.AntdSpace(
                    [
                        html.Div(
                            style={
                                'width': 12,
                                'height': 12,
                                'borderRadius': '50%',
                                'background': color,
                            }
                        )
                        for color in ['#ff4444', '#99bb33', '#ffbb55']
                    ]
                ),
                flex='none',
                style={'paddingRight': '10px'},
            ),
            fac.AntdCol(
                html.Div(style={'height': 20, 'background': 'white'}),
                flex='auto',
            ),
        ],
        align='middle',
        style={
            'background': '#ededed',
            'padding': '6px 12px',
            'borderRadius': '8px 8px 0 0',
        },
    )
