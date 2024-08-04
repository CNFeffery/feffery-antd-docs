import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


code_string = [
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
