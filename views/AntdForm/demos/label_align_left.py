import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(fac.AntdInput(), label='用户名'),
                fac.AntdFormItem(fac.AntdInput(mode='password'), label='密码'),
                fac.AntdFormItem(
                    fac.AntdButton('登录', type='primary'),
                    wrapperCol={'offset': 4},
                ),
            ],
            labelCol={'span': 4},
            wrapperCol={'span': 20},
            labelAlign='left',
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
            fac.AntdFormItem(fac.AntdInput(), label='用户名'),
            fac.AntdFormItem(fac.AntdInput(mode='password'), label='密码'),
            fac.AntdFormItem(
                fac.AntdButton('登录', type='primary'),
                wrapperCol={'offset': 4},
            ),
        ],
        labelCol={'span': 4},
        wrapperCol={'span': 20},
        labelAlign='left',
        style={'width': 300},
    )
)
"""
    }
]
