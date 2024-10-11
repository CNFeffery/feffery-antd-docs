import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdCenter(
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(),
                        label='用户名',
                        tooltip='输入您的用户名信息',
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(mode='password'),
                        label='密码',
                        tooltip='输入您的账户密码信息',
                    ),
                    fac.AntdFormItem(
                        fac.AntdButton('登录', type='primary'),
                        wrapperCol={'offset': 6},
                    ),
                ],
                labelCol={'span': 6},
                wrapperCol={'span': 18},
                style={'width': 300},
            )
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdCenter(
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(),
                        label='Username',
                        tooltip='Enter your username information',
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(mode='password'),
                        label='Password',
                        tooltip='Enter your account password information',
                    ),
                    fac.AntdFormItem(
                        fac.AntdButton('Login', type='primary'),
                        wrapperCol={'offset': 8},
                    ),
                ],
                labelCol={'span': 8},
                wrapperCol={'span': 16},
                style={'width': 300},
            )
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdCenter(
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdInput(),
                label='用户名',
                tooltip='输入您的用户名信息',
            ),
            fac.AntdFormItem(
                fac.AntdInput(mode='password'),
                label='密码',
                tooltip='输入您的账户密码信息',
            ),
            fac.AntdFormItem(
                fac.AntdButton('登录', type='primary'),
                wrapperCol={'offset': 6},
            ),
        ],
        labelCol={'span': 6},
        wrapperCol={'span': 18},
        style={'width': 300},
    )
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdCenter(
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdInput(),
                label='Username',
                tooltip='Enter your username information',
            ),
            fac.AntdFormItem(
                fac.AntdInput(mode='password'),
                label='Password',
                tooltip='Enter your account password information',
            ),
            fac.AntdFormItem(
                fac.AntdButton('Login', type='primary'),
                wrapperCol={'offset': 8},
            ),
        ],
        labelCol={'span': 8},
        wrapperCol={'span': 16},
        style={'width': 300},
    )
)
"""
            }
        ]
