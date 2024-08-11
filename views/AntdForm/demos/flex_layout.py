import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('AntdForm整体配置', innerTextOrientation='left'),
        fac.AntdCenter(
            fac.AntdForm(
                [
                    fac.AntdFormItem(fac.AntdInput(), label='表单' + '项' * i)
                    for i in range(1, 4)
                ],
                labelCol={'flex': 'none'},
                wrapperCol={'flex': 'auto'},
                style={'width': 300},
            )
        ),
        fac.AntdDivider('AntdFormItem独立配置', innerTextOrientation='left'),
        fac.AntdCenter(
            fac.AntdForm(
                [
                    fac.AntdFormItem(
                        fac.AntdInput(),
                        label='示例1',
                        labelCol={'flex': '1'},
                        wrapperCol={'flex': '1'},
                    ),
                    fac.AntdFormItem(
                        fac.AntdInput(),
                        label='示例2',
                        labelCol={'flex': 'none'},
                        wrapperCol={'flex': 'auto'},
                    ),
                ],
                style={'width': 300},
            )
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('AntdForm整体配置', innerTextOrientation='left'),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(fac.AntdInput(), label='表单' + '项' * i)
                for i in range(1, 4)
            ],
            labelCol={'flex': 'none'},
            wrapperCol={'flex': 'auto'},
            style={'width': 300},
        )
    ),
    fac.AntdDivider('AntdFormItem独立配置', innerTextOrientation='left'),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(),
                    label='示例1',
                    labelCol={'flex': '1'},
                    wrapperCol={'flex': '1'},
                ),
                fac.AntdFormItem(
                    fac.AntdInput(),
                    label='示例2',
                    labelCol={'flex': 'none'},
                    wrapperCol={'flex': 'auto'},
                ),
            ],
            style={'width': 300},
        )
    ),
]
"""
    }
]
