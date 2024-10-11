import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdDivider('layout="vertical"', innerTextOrientation='left'),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(fac.AntdInput(), label='用户名'),
                        fac.AntdFormItem(
                            fac.AntdInput(mode='password'), label='密码'
                        ),
                        fac.AntdFormItem(
                            fac.AntdButton('登录', type='primary')
                        ),
                    ],
                    layout='vertical',
                    style={'width': 300},
                )
            ),
            fac.AntdDivider('layout="inline"', innerTextOrientation='left'),
            fac.AntdForm(
                [
                    fac.AntdFormItem(fac.AntdInput(), label='用户名'),
                    fac.AntdFormItem(
                        fac.AntdInput(mode='password'), label='密码'
                    ),
                    fac.AntdFormItem(fac.AntdButton('登录', type='primary')),
                ],
                layout='inline',
                style={'justifyContent': 'center'},
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDivider('layout="vertical"', innerTextOrientation='left'),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(fac.AntdInput(), label='Username'),
                        fac.AntdFormItem(
                            fac.AntdInput(mode='password'), label='Password'
                        ),
                        fac.AntdFormItem(
                            fac.AntdButton('Login', type='primary')
                        ),
                    ],
                    layout='vertical',
                    style={'width': 300},
                )
            ),
            fac.AntdDivider('layout="inline"', innerTextOrientation='left'),
            fac.AntdForm(
                [
                    fac.AntdFormItem(fac.AntdInput(), label='Username'),
                    fac.AntdFormItem(
                        fac.AntdInput(mode='password'), label='Password'
                    ),
                    fac.AntdFormItem(fac.AntdButton('Login', type='primary')),
                ],
                layout='inline',
                style={'justifyContent': 'center'},
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdDivider('layout="vertical"', innerTextOrientation='left'),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(fac.AntdInput(), label='用户名'),
                fac.AntdFormItem(
                    fac.AntdInput(mode='password'), label='密码'
                ),
                fac.AntdFormItem(fac.AntdButton('登录', type='primary')),
            ],
            layout='vertical',
            style={'width': 300},
        )
    ),
    fac.AntdDivider('layout="inline"', innerTextOrientation='left'),
    fac.AntdForm(
        [
            fac.AntdFormItem(fac.AntdInput(), label='用户名'),
            fac.AntdFormItem(fac.AntdInput(mode='password'), label='密码'),
            fac.AntdFormItem(fac.AntdButton('登录', type='primary')),
        ],
        layout='inline',
        style={'justifyContent': 'center'},
    ),
]
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdDivider('layout="vertical"', innerTextOrientation='left'),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(fac.AntdInput(), label='Username'),
                fac.AntdFormItem(
                    fac.AntdInput(mode='password'), label='Password'
                ),
                fac.AntdFormItem(
                    fac.AntdButton('Login', type='primary')
                ),
            ],
            layout='vertical',
            style={'width': 300},
        )
    ),
    fac.AntdDivider('layout="inline"', innerTextOrientation='left'),
    fac.AntdForm(
        [
            fac.AntdFormItem(fac.AntdInput(), label='Username'),
            fac.AntdFormItem(
                fac.AntdInput(mode='password'), label='Password'
            ),
            fac.AntdFormItem(fac.AntdButton('Login', type='primary')),
        ],
        layout='inline',
        style={'justifyContent': 'center'},
    ),
]
"""
            }
        ]
