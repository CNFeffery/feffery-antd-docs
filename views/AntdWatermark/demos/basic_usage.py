import feffery_antd_components as fac
from dash.dependencies import Component
from dash import html


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdWatermark(
            html.Div(
                style={
                    'height': '500px',
                    'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                    'marginBottom': '25px',
                }
            ),
            content='水印内容测试',
            fontSize=28,
        ),
        fac.AntdWatermark(
            html.Div(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdInput(autoComplete='off'), label='用户名'
                        ),
                        fac.AntdFormItem(
                            fac.AntdInput(mode='password'), label='密码'
                        ),
                        fac.AntdFormItem(
                            fac.AntdCheckbox(label='记住密码'),
                            wrapperCol={'offset': 4},
                        ),
                        fac.AntdFormItem(
                            fac.AntdButton('登录', type='primary'),
                            wrapperCol={'offset': 4},
                        ),
                    ],
                    labelCol={'span': 4},
                    wrapperCol={'span': 8},
                ),
                style={
                    'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                    'padding': '25px',
                },
            ),
            content='水印内容测试',
            fontSize=22,
            rotate=22,
            gapX=50,
            gapY=50,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdWatermark(
    html.Div(
        style={
            'height': '500px',
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'marginBottom': '25px'
        }
    ),
    content='水印内容测试',
    fontSize=28
),

fac.AntdWatermark(
    html.Div(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(
                        autoComplete='off'
                    ),
                    label='用户名'
                ),
                fac.AntdFormItem(
                    fac.AntdInput(
                        mode='password'
                    ),
                    label='密码'
                ),
                fac.AntdFormItem(
                    fac.AntdCheckbox(
                        label='记住密码'
                    ),
                    wrapperCol={
                        'offset': 4
                    }
                ),
                fac.AntdFormItem(
                    fac.AntdButton(
                        '登录',
                        type='primary'
                    ),
                    wrapperCol={
                        'offset': 4
                    }
                )
            ],
            labelCol={
                'span': 4
            },
            wrapperCol={
                'span': 8
            }
        ),
        style={
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'padding': '25px'
        }
    ),
    content='水印内容测试',
    fontSize=22,
    rotate=22,
    gapX=50,
    gapY=50
)
"""
    }
]
