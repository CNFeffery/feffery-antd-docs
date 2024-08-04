import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdText('justify:'),
            fac.AntdRadioGroup(
                id='row-align-demo-justify',
                options=[
                    'start',
                    'end',
                    'center',
                    'space-between',
                    'space-around',
                ],
                value='start',
            ),
            fac.AntdText('align:'),
            fac.AntdRadioGroup(
                id='row-align-demo-align',
                options=['top', 'middle', 'bottom'],
                value='top',
            ),
            fac.AntdRow(
                [
                    fac.AntdCol(
                        fac.AntdButton('子元素', type='primary'),
                        flex='none',
                        style={'height': 'fit-content'},
                    )
                ]
                * 4,
                id='row-align-demo',
                gutter=10,
                style={
                    'width': '100%',
                    'height': 200,
                    'borderRadius': 6,
                    'border': '1px solid #40a9ff',
                },
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('row-align-demo', 'justify'),
    Input('row-align-demo-justify', 'value'),
)
def update_demo_justify(value):
    return value


@app.callback(
    Output('row-align-demo', 'align'),
    Input('row-align-demo-align', 'value'),
)
def update_demo_align(value):
    return value


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdText('justify:'),
        fac.AntdRadioGroup(
            id='row-align-demo-justify',
            options=[
                'start',
                'end',
                'center',
                'space-between',
                'space-around',
            ],
            value='start',
        ),
        fac.AntdText('align:'),
        fac.AntdRadioGroup(
            id='row-align-demo-align',
            options=['top', 'middle', 'bottom'],
            value='top',
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdButton('子元素', type='primary'),
                    flex='none',
                    style={'height': 'fit-content'},
                )
            ]
            * 4,
            id='row-align-demo',
            gutter=10,
            style={
                'width': '100%',
                'height': 200,
                'borderRadius': 6,
                'border': '1px solid #40a9ff',
            },
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('row-align-demo', 'justify'),
    Input('row-align-demo-justify', 'value'),
)
def update_demo_justify(value):
    return value


@app.callback(
    Output('row-align-demo', 'align'),
    Input('row-align-demo-align', 'value'),
)
def update_demo_align(value):
    return value
"""
    }
]
