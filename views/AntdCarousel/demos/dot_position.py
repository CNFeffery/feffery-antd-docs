import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdRadioGroup(
                id='carousel-dot-position',
                options=['bottom', 'top', 'left', 'right'],
                value='bottom',
            ),
            fac.AntdCarousel(
                [
                    fac.AntdCenter(
                        i,
                        style={
                            'color': 'white',
                            'fontSize': 36,
                            'height': 160,
                            'backgroundColor': '#364d79',
                        },
                    )
                    for i in range(1, 6)
                ],
                id='carousel-dot-position-demo',
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


app.clientside_callback(
    """(value) => value""",
    Output('carousel-dot-position-demo', 'dotPosition'),
    Input('carousel-dot-position', 'value'),
)

code_string = [
    {
        'code': '''
fac.AntdSpace(
    [
        fac.AntdRadioGroup(
            id='carousel-dot-position',
            options=['bottom', 'top', 'left', 'right'],
            value='bottom',
        ),
        fac.AntdCarousel(
            [
                fac.AntdCenter(
                    i,
                    style={
                        'color': 'white',
                        'fontSize': 36,
                        'height': 160,
                        'backgroundColor': '#364d79',
                    },
                )
                for i in range(1, 6)
            ],
            id='carousel-dot-position-demo',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

app.clientside_callback(
    """(value) => value""",
    Output('carousel-dot-position-demo', 'dotPosition'),
    Input('carousel-dot-position', 'value'),
)
'''
    }
]
