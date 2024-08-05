import feffery_antd_components as fac
from dash.dependencies import Component
from dash import html
from server import app
from dash.dependencies import Input, Output


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        html.Div(
            [
                fac.AntdDivider('设置duration', innerTextOrientation='left'),
                fac.AntdSlider(
                    id='back-top-duration-slider-demo',
                    value=1,
                    min=0.1,
                    max=5,
                    step=0.1,
                ),
                fac.AntdBackTop(
                    id='back-top-duration-demo',
                    containerId='back-top-container-duration-demo',
                    duration=3,
                ),
                fac.AntdTitle(id='back-top-duration-title-demo', level=4),
            ]
            + [html.Div([i if i % 2 == 0 else html.Br() for i in range(200)])],
            id='back-top-container-duration-demo',
            style={
                'maxHeight': '500px',
                'overflowY': 'auto',
                'position': 'relative',
                'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                'border': '1px solid #f0f0f0',
                'padding': '20px',
            },
        )
    ]

    return demo_contents


@app.callback(
    [
        Output('back-top-duration-demo', 'duration'),
        Output('back-top-duration-title-demo', 'children'),
    ],
    Input('back-top-duration-slider-demo', 'value'),
)
def update_duration(value):
    return value, f'向下滚动一段距离，点击按钮后{value}秒内滚动回顶部'


code_string = [
    {
        'code': """
html.Div(
    [
        fac.AntdDivider('设置duration', innerTextOrientation='left'),
        fac.AntdSlider(
            id='back-top-duration-slider-demo',
            value=1,
            min=0.1,
            max=5,
            step=0.1,
        ),
        fac.AntdBackTop(
            id='back-top-duration-demo',
            containerId='back-top-container-duration-demo',
            duration=3,
        ),
        fac.AntdTitle(id='back-top-duration-title-demo', level=4),
    ]
    + [html.Div([i if i % 2 == 0 else html.Br() for i in range(200)])],
    id='back-top-container-duration-demo',
    style={
        'maxHeight': '500px',
        'overflowY': 'auto',
        'position': 'relative',
        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
        'border': '1px solid #f0f0f0',
        'padding': '20px',
    },
)


@app.callback(
    [
        Output('back-top-duration-demo', 'duration'),
        Output('back-top-duration-title-demo', 'children'),
    ],
    Input('back-top-duration-slider-demo', 'value'),
)
def update_duration(value):
    return value, f'向下滚动一段距离，点击按钮后{value}秒内滚动回顶部'
"""
    }
]
