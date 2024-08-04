import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(), label='用户名', required=True
                ),
                fac.AntdFormItem(
                    fac.AntdInput(mode='password'), label='密码', required=True
                ),
                fac.AntdFormItem(
                    fac.AntdButton('登录', type='primary'),
                    wrapperCol={'offset': 5},
                ),
            ],
            labelCol={'span': 5},
            wrapperCol={'span': 19},
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
                fac.AntdInput(), label='用户名', required=True
            ),
            fac.AntdFormItem(
                fac.AntdInput(mode='password'), label='密码', required=True
            ),
            fac.AntdFormItem(
                fac.AntdButton('登录', type='primary'),
                wrapperCol={'offset': 5},
            ),
        ],
        labelCol={'span': 5},
        wrapperCol={'span': 19},
        style={'width': 300},
    )
)
"""
    }
]
