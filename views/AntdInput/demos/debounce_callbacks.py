import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app
from dash import html


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdText('当前debounceWait(单位：ms)：'),
                    fac.AntdInputNumber(
                        id='input-debounce-wait-demo',
                        value=500,
                        min=0,
                        precision=0,
                    ),
                ],
                style={
                    'justify-content': 'space-between',
                    'width': '100%',
                },
            ),
            fac.AntdInput(
                id='input-debounce-demo',
                placeholder='请输入内容',
                maxLength=10,
            ),
            fac.AntdCard(
                [
                    html.Div(id='input-not-debounce-demo-output'),
                    html.Div(id='input-debounce-demo-output'),
                ],
                headStyle={'display': 'none'},
                bodyStyle={'flex-direction': 'column'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


# 通过AntdInputNumber回调设定input的debounceWait数值
@app.callback(
    Output('input-debounce-demo', 'debounceWait'),
    Input('input-debounce-wait-demo', 'value'),
)
def set_debounce_wait(value):
    return value


@app.callback(
    Output('input-not-debounce-demo-output', 'children'),
    Input('input-debounce-demo', 'value'),
)
def input_demo(value):
    return f'value: {value}'


@app.callback(
    Output('input-debounce-demo-output', 'children'),
    Input('input-debounce-demo', 'debounceValue'),
)
def input_debounce_demo(debounceValue):
    return f'debounceValue: {debounceValue}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdText('当前debounceWait(单位：ms)：'),
                fac.AntdInputNumber(
                    id='input-debounce-wait-demo',
                    value=500,
                    min=0,
                    precision=0,
                ),
            ],
            style={
                'justify-content': 'space-between',
                'width': '100%',
            },
        ),
        fac.AntdInput(
            id='input-debounce-demo',
            placeholder='请输入内容',
            maxLength=10,
        ),
        fac.AntdCard(
            [
                html.Div(id='input-not-debounce-demo-output'),
                html.Div(id='input-debounce-demo-output'),
            ],
            headStyle={'display': 'none'},
            bodyStyle={'flex-direction': 'column'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)

...

# 通过AntdInputNumber回调设定input的debounceWait数值
@app.callback(
    Output('input-debounce-demo', 'debounceWait'),
    Input('input-debounce-wait-demo', 'value'),
)
def set_debounce_wait(value):
    return value


@app.callback(
    Output('input-not-debounce-demo-output', 'children'),
    Input('input-debounce-demo', 'value'),
)
def input_demo(value):
    return f'value: {value}'


@app.callback(
    Output('input-debounce-demo-output', 'children'),
    Input('input-debounce-demo', 'debounceValue'),
)
def input_debounce_demo(debounceValue):
    return f'debounceValue: {debounceValue}'
"""
    }
]
