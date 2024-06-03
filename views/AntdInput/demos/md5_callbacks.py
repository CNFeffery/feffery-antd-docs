import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app
from dash import html


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                id='input-md5-demo',
                placeholder='请输入密码',
                mode='password',
                passwordUseMd5=True,
                maxLength=10,
            ),
            fac.AntdCard(
                [
                    html.Div(id='input-not-md5-demo-output'),
                    html.Div(id='input-md5-demo-output'),
                ],
                headStyle={'display': 'none'},
                bodyStyle={'flex-direction': 'column'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


@app.callback(
    Output('input-not-md5-demo-output', 'children'),
    Input('input-md5-demo', 'value'),
)
def input_demo(value):
    return f'value: {value}'


@app.callback(
    Output('input-md5-demo-output', 'children'),
    Input('input-md5-demo', 'md5Value'),
)
def input_debounce_demo(md5Value):
    return f'md5Value: {md5Value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            id='input-md5-demo',
            placeholder='请输入密码',
            mode='password',
            passwordUseMd5=True,
            maxLength=10,
        ),
        fac.AntdCard(
            [
                html.Div(id='input-not-md5-demo-output'),
                html.Div(id='input-md5-demo-output'),
            ],
            headStyle={'display': 'none'},
            bodyStyle={'flex-direction': 'column'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)


@app.callback(
    Output('input-not-md5-demo-output', 'children'),
    Input('input-md5-demo', 'value'),
)
def input_demo(value):
    return f'value: {value}'


@app.callback(
    Output('input-md5-demo-output', 'children'),
    Input('input-md5-demo', 'md5Value'),
)
def input_debounce_demo(md5Value):
    return f'md5Value: {md5Value}'
"""
    }
]
