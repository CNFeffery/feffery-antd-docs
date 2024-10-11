import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdCenter(
            fac.AntdSpace(
                [
                    fac.AntdAlert(
                        message='示例用户名：fac  密码：123456 你可以故意输错用户名或密码来查看不同的校验反馈结果',
                        type='info',
                        showIcon=True,
                        messageRenderMode='marquee',
                        style={'marginBottom': '10px'},
                    ),
                    fac.AntdForm(
                        [
                            fac.AntdFormItem(
                                fac.AntdInput(
                                    id='form-item-validate-demo-username'
                                ),
                                id='form-item-validate-demo-username-container',
                                label='用户名',
                            ),
                            fac.AntdFormItem(
                                fac.AntdInput(
                                    id='form-item-validate-demo-password',
                                    mode='password',
                                ),
                                id='form-item-validate-demo-password-container',
                                label='密码',
                            ),
                            fac.AntdFormItem(
                                fac.AntdButton(
                                    '登录',
                                    id='form-item-validate-demo-submit',
                                    type='primary',
                                )
                            ),
                        ],
                        layout='vertical',
                    ),
                ],
                direction='vertical',
                style={'width': 400},
            ),
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdCenter(
            fac.AntdSpace(
                [
                    fac.AntdAlert(
                        message='Example username: fac Password: 123456 You can intentionally enter the wrong username or password to see different validation feedback results.',
                        type='info',
                        showIcon=True,
                        messageRenderMode='marquee',
                        style={'marginBottom': '10px'},
                    ),
                    fac.AntdForm(
                        [
                            fac.AntdFormItem(
                                fac.AntdInput(
                                    id='form-item-validate-demo-username'
                                ),
                                id='form-item-validate-demo-username-container',
                                label='Username',
                            ),
                            fac.AntdFormItem(
                                fac.AntdInput(
                                    id='form-item-validate-demo-password',
                                    mode='password',
                                ),
                                id='form-item-validate-demo-password-container',
                                label='Password',
                            ),
                            fac.AntdFormItem(
                                fac.AntdButton(
                                    'Login',
                                    id='form-item-validate-demo-submit',
                                    type='primary',
                                )
                            ),
                        ],
                        layout='vertical',
                    ),
                ],
                direction='vertical',
                style={'width': 400},
            ),
        )

    return demo_contents


@app.callback(
    [
        Output('form-item-validate-demo-username-container', 'validateStatus'),
        Output('form-item-validate-demo-password-container', 'validateStatus'),
        Output('form-item-validate-demo-username-container', 'help'),
        Output('form-item-validate-demo-password-container', 'help'),
    ],
    Input('form-item-validate-demo-submit', 'nClicks'),
    [
        State('form-item-validate-demo-username', 'value'),
        State('form-item-validate-demo-password', 'value'),
    ],
    prevent_initial_call=True,
)
def form_item_validate_demo(nClicks, username, password):
    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        if username and password:
            return [
                None if username == 'fac' else 'error',
                ('success' if password == '123456' else 'error')
                if username == 'fac'
                else None,
                None if username == 'fac' else '用户不存在！',
                ('密码正确！' if password == '123456' else '密码错误！')
                if username == 'fac'
                else None,
            ]

        return [
            None if username else 'error',
            None if password else 'error',
            None if username else '用户名不能为空！',
            None if password else '密码不能为空！',
        ]

    elif current_locale == 'en-us':
        if username and password:
            return [
                None if username == 'fac' else 'error',
                ('success' if password == '123456' else 'error')
                if username == 'fac'
                else None,
                None if username == 'fac' else 'User does not exist!',
                (
                    'Password correct!'
                    if password == '123456'
                    else 'Password error!'
                )
                if username == 'fac'
                else None,
            ]

        return [
            None if username else 'error',
            None if password else 'error',
            None if username else 'Username cannot be empty!',
            None if password else 'Password cannot be empty!',
        ]


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdCenter(
    fac.AntdSpace(
        [
            fac.AntdAlert(
                message='示例用户名：fac  密码：123456 你可以故意输错用户名或密码来查看不同的校验反馈结果',
                type='info',
                showIcon=True,
                messageRenderMode='marquee',
                style={'marginBottom': '10px'},
            ),
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='form-item-validate-demo-username'
                        ),
                        id='form-item-validate-demo-username-container',
                        label='用户名',
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='form-item-validate-demo-password',
                            mode='password',
                        ),
                        id='form-item-validate-demo-password-container',
                        label='密码',
                    ),
                    fac.AntdFormItem(
                        fac.AntdButton(
                            '登录',
                            id='form-item-validate-demo-submit',
                            type='primary',
                        )
                    ),
                ],
                layout='vertical',
            ),
        ],
        direction='vertical',
        style={'width': 400},
    ),
)

...

@app.callback(
    [
        Output('form-item-validate-demo-username-container', 'validateStatus'),
        Output('form-item-validate-demo-password-container', 'validateStatus'),
        Output('form-item-validate-demo-username-container', 'help'),
        Output('form-item-validate-demo-password-container', 'help'),
    ],
    Input('form-item-validate-demo-submit', 'nClicks'),
    [
        State('form-item-validate-demo-username', 'value'),
        State('form-item-validate-demo-password', 'value'),
    ],
    prevent_initial_call=True,
)
def form_item_validate_demo(nClicks, username, password):
    if username and password:
        return [
            None if username == 'fac' else 'error',
            ('success' if password == '123456' else 'error')
            if username == 'fac'
            else None,
            None if username == 'fac' else '用户不存在！',
            ('密码正确！' if password == '123456' else '密码错误！')
            if username == 'fac'
            else None,
        ]

    return [
        None if username else 'error',
        None if password else 'error',
        None if username else '用户名不能为空！',
        None if password else '密码不能为空！',
    ]
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdCenter(
    fac.AntdSpace(
        [
            fac.AntdAlert(
                message='Example username: fac Password: 123456 You can intentionally enter the wrong username or password to see different validation feedback results.',
                type='info',
                showIcon=True,
                messageRenderMode='marquee',
                style={'marginBottom': '10px'},
            ),
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='form-item-validate-demo-username'
                        ),
                        id='form-item-validate-demo-username-container',
                        label='Username',
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(
                            id='form-item-validate-demo-password',
                            mode='password',
                        ),
                        id='form-item-validate-demo-password-container',
                        label='Password',
                    ),
                    fac.AntdFormItem(
                        fac.AntdButton(
                            'Login',
                            id='form-item-validate-demo-submit',
                            type='primary',
                        )
                    ),
                ],
                layout='vertical',
            ),
        ],
        direction='vertical',
        style={'width': 400},
    ),
)

...

@app.callback(
    [
        Output('form-item-validate-demo-username-container', 'validateStatus'),
        Output('form-item-validate-demo-password-container', 'validateStatus'),
        Output('form-item-validate-demo-username-container', 'help'),
        Output('form-item-validate-demo-password-container', 'help'),
    ],
    Input('form-item-validate-demo-submit', 'nClicks'),
    [
        State('form-item-validate-demo-username', 'value'),
        State('form-item-validate-demo-password', 'value'),
    ],
    prevent_initial_call=True,
)
def form_item_validate_demo(nClicks, username, password):
    if username and password:
        return [
            None if username == 'fac' else 'error',
            ('success' if password == '123456' else 'error')
            if username == 'fac'
            else None,
            None if username == 'fac' else 'User does not exist!',
            (
                'Password correct!'
                if password == '123456'
                else 'Password error!'
            )
            if username == 'fac'
            else None,
        ]

    return [
        None if username else 'error',
        None if password else 'error',
        None if username else 'Username cannot be empty!',
        None if password else 'Password cannot be empty!',
    ]
"""
            }
        ]
