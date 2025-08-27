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
                fac.AntdDivider(
                    '设置visibilityHeight', innerTextOrientation='left'
                ),
                fac.AntdSlider(
                    id='back-top-visibility-height-slider-demo',
                    value=200,
                    min=50,
                    max=1500,
                    step=1,
                ),
                fac.AntdBackTop(
                    id='back-top-visibility-height-demo',
                    containerId='back-top-container-visibility-height-demo',
                ),
                fac.AntdTitle(
                    id='back-top-visibility-height-title-demo', level=4
                ),
            ]
            + [
                fac.AntdSpace(
                    [
                        f'已滚动{(i - 4) * (22.5 + 8) if i > 4 else 0}px'
                        for i in range(200)
                    ],
                    direction='vertical',
                )
            ],
            id='back-top-container-visibility-height-demo',
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
        Output('back-top-visibility-height-demo', 'visibilityHeight'),
        Output('back-top-visibility-height-title-demo', 'children'),
    ],
    Input('back-top-visibility-height-slider-demo', 'value'),
)
def update_duration(value):
    return value, f'向下滚动{value}px出现按钮'


code_string = [
    {
        'code': """
html.Div(
    [
        fac.AntdDivider(
            '设置visibilityHeight', innerTextOrientation='left'
        ),
        fac.AntdSlider(
            id='back-top-visibility-height-slider-demo',
            value=200,
            min=50,
            max=1500,
            step=1,
        ),
        fac.AntdBackTop(
            id='back-top-visibility-height-demo',
            containerId='back-top-container-visibility-height-demo',
        ),
        fac.AntdTitle(
            id='back-top-visibility-height-title-demo', level=4
        ),
    ]
    + [
        fac.AntdSpace(
            [
                f'已滚动{(i - 4)*(22.5+8) if i > 4 else 0}px'
                for i in range(200)
            ],
            direction='vertical',
        )
    ],
    id='back-top-container-visibility-height-demo',
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
        Output('back-top-visibility-height-demo', 'visibilityHeight'),
        Output('back-top-visibility-height-title-demo', 'children'),
    ],
    Input('back-top-visibility-height-slider-demo', 'value'),
)
def update_duration(value):
    return value, f'向下滚动{value}px出现按钮'
"""
    }
]
