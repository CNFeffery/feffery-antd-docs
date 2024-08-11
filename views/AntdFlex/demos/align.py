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
                id='flex-align-demo-justify',
                options=[
                    'flex-start',
                    'center',
                    'flex-end',
                    'space-between',
                    'space-around',
                    'space-evenly',
                ],
                value='flex-start',
            ),
            fac.AntdText('align:'),
            fac.AntdRadioGroup(
                id='flex-align-demo-align',
                options=['flex-start', 'center', 'flex-end'],
                value='flex-start',
            ),
            fac.AntdFlex(
                [fac.AntdButton('子元素', type='primary')] * 4,
                id='flex-align-demo',
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
    Output('flex-align-demo', 'justify'),
    Input('flex-align-demo-justify', 'value'),
)
def update_demo_justify(value):
    return value


@app.callback(
    Output('flex-align-demo', 'align'),
    Input('flex-align-demo-align', 'value'),
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
            id='flex-align-demo-justify',
            options=[
                'flex-start',
                'center',
                'flex-end',
                'space-between',
                'space-around',
                'space-evenly',
            ],
            value='flex-start',
        ),
        fac.AntdText('align:'),
        fac.AntdRadioGroup(
            id='flex-align-demo-align',
            options=['flex-start', 'center', 'flex-end'],
            value='flex-start',
        ),
        fac.AntdFlex(
            [fac.AntdButton('子元素', type='primary')] * 4,
            id='flex-align-demo',
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
    Output('flex-align-demo', 'justify'),
    Input('flex-align-demo-justify', 'value'),
)
def update_demo_justify(value):
    return value


@app.callback(
    Output('flex-align-demo', 'align'),
    Input('flex-align-demo-align', 'value'),
)
def update_demo_align(value):
    return value
"""
    }
]
