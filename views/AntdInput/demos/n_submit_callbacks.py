import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('基本示例', innerTextOrientation='left'),
            fac.AntdInput(
                id='input-enter-demo',
                placeholder='聚焦于此后按下enter',
            ),
            fac.AntdCard(
                id='input-enter-demo-output', headStyle={'display': 'none'}
            ),
            fac.AntdDivider('模拟登录示例', innerTextOrientation='left'),
            fac.AntdCard(
                fac.AntdSpace(
                    [
                        fac.AntdAlert(
                            message='聚焦于以下输入框后按下enter键，会得到和点击登录按钮相同的效果。',
                            type='info',
                            showIcon=True,
                            messageRenderMode='marquee',
                        ),
                        fac.AntdInput(
                            id='input-enter-demo-login',
                            placeholder='请输入用户名',
                            prefix=fac.AntdIcon(icon='antd-user'),
                        ),
                        fac.AntdInput(
                            id='input-enter-demo-password',
                            placeholder='请输入密码',
                            prefix=fac.AntdIcon(icon='antd-key'),
                            mode='password',
                        ),
                        fac.AntdCenter(
                            [
                                fac.AntdButton(
                                    '登录',
                                    type='primary',
                                    id='input-enter-demo-login-btn',
                                ),
                                fac.AntdButton(
                                    '取消',
                                    type='default',
                                    id='input-enter-demo-cancel-btn',
                                ),
                            ],
                            style={'gap': 10},
                        ),
                        fac.AntdText(
                            id='input-enter-demo-login-output',
                            style={'marginTop': 10},
                        ),
                    ],
                    direction='vertical',
                    style={'width': '100%'},
                ),
                headStyle={'display': 'none'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


# 基本示例nSubmit回调函数
@app.callback(
    Output('input-enter-demo-output', 'children'),
    Input('input-enter-demo', 'nSubmit'),
)
def input_enter_dmeo(nSubmit):
    return f'nSubmit: {nSubmit}'


# 模拟登录示例nSubmit回调函数
@app.callback(
    Output('input-enter-demo-login-output', 'children'),
    [
        Input('input-enter-demo-login-btn', 'nClicks'),
        Input('input-enter-demo-login', 'nSubmit'),
        Input('input-enter-demo-password', 'nSubmit'),
    ],
    prevent_initial_call=True,
)
def input_enter_dmeo_login(nClicks1, nSubmit1, nSubmit2):
    if nClicks1 is None:
        nClicks1 = 0
    if nSubmit1 is None:
        nSubmit1 = 0
    if nSubmit2 is None:
        nSubmit2 = 0

    return f'登录次数：{nClicks1+nSubmit1+nSubmit2}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('基本示例', innerTextOrientation='left'),
        fac.AntdInput(
            id='input-enter-demo',
            placeholder='聚焦于此后按下enter',
        ),
        fac.AntdCard(
            id='input-enter-demo-output', headStyle={'display': 'none'}
        ),
        fac.AntdDivider('模拟登录示例', innerTextOrientation='left'),
        fac.AntdCard(
            fac.AntdSpace(
                [
                    fac.AntdAlert(
                        message='聚焦于以下输入框后按下enter键，会得到和点击登录按钮相同的效果。',
                        type='info',
                        showIcon=True,
                        messageRenderMode='marquee',
                    ),
                    fac.AntdInput(
                        id='input-enter-demo-login',
                        placeholder='请输入用户名',
                        prefix=fac.AntdIcon(icon='antd-user'),
                    ),
                    fac.AntdInput(
                        id='input-enter-demo-password',
                        placeholder='请输入密码',
                        prefix=fac.AntdIcon(icon='antd-key'),
                        mode='password',
                    ),
                    fac.AntdCenter(
                        [
                            fac.AntdButton(
                                '登录',
                                type='primary',
                                id='input-enter-demo-login-btn',
                            ),
                            fac.AntdButton(
                                '取消',
                                type='default',
                                id='input-enter-demo-cancel-btn',
                            ),
                        ],
                        style={'gap': 10},
                    ),
                    fac.AntdText(
                        id='input-enter-demo-login-output',
                        style={'marginTop': 10},
                    ),
                ],
                direction='vertical',
                style={'width': '100%'},
            ),
            headStyle={'display': 'none'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)

...

# 基本示例nSubmit回调函数
@app.callback(
    Output('input-enter-demo-output', 'children'),
    Input('input-enter-demo', 'nSubmit'),
)
def input_enter_dmeo(nSubmit):
    return f'nSubmit: {nSubmit}'


# 模拟登录示例nSubmit回调函数
@app.callback(
    Output('input-enter-demo-login-output', 'children'),
    [
        Input('input-enter-demo-login-btn', 'nClicks'),
        Input('input-enter-demo-login', 'nSubmit'),
        Input('input-enter-demo-password', 'nSubmit'),
    ],
    prevent_initial_call=True,
)
def input_enter_dmeo_login(nClicks1, nSubmit1, nSubmit2):
    if nClicks1 is None:
        nClicks1 = 0
    if nSubmit1 is None:
        nSubmit1 = 0
    if nSubmit2 is None:
        nSubmit2 = 0

    return f'登录次数：{nClicks1+nSubmit1+nSubmit2}'
"""
    }
]
