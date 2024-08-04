import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


code_string = [
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
