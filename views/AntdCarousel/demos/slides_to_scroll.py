from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCarousel(
        [
            html.Div(
                fac.AntdCenter(
                    i,
                    style={
                        'color': 'white',
                        'fontSize': 36,
                        'backgroundColor': '#364d79',
                        'height': '100%',
                    },
                ),
                style={'height': 160, 'padding': '0 5px'},
            )
            for i in range(1, 10)
        ],
        slidesToShow=3,
        slidesToScroll=3,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdCarousel(
    [
        html.Div(
            fac.AntdCenter(
                i,
                style={
                    'color': 'white',
                    'fontSize': 36,
                    'backgroundColor': '#364d79',
                    'height': '100%',
                },
            ),
            style={'height': 160, 'padding': '0 5px'},
        )
        for i in range(1, 10)
    ],
    slidesToShow=3,
    slidesToScroll=3,
)
"""
    }
]
