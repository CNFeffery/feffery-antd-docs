import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdDivider('AntdForm整体配置', innerTextOrientation='left'),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdInput(), label='表单' + '项' * i
                        )
                        for i in range(1, 4)
                    ],
                    labelCol={'flex': 'none'},
                    wrapperCol={'flex': 'auto'},
                    style={'width': 300},
                )
            ),
            fac.AntdDivider(
                'AntdFormItem独立配置', innerTextOrientation='left'
            ),
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDivider(
                'AntdForm Global Configuration', innerTextOrientation='left'
            ),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdInput(), label='Form' + ' Item' * i
                        )
                        for i in range(1, 4)
                    ],
                    labelCol={'flex': 'none'},
                    wrapperCol={'flex': 'auto'},
                    style={'width': 300},
                )
            ),
            fac.AntdDivider(
                'AntdFormItem Individual Configuration',
                innerTextOrientation='left',
            ),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdInput(),
                            label='Example 1',
                            labelCol={'flex': '1'},
                            wrapperCol={'flex': '1'},
                        ),
                        fac.AntdFormItem(
                            fac.AntdInput(),
                            label='Example 2',
                            labelCol={'flex': 'none'},
                            wrapperCol={'flex': 'auto'},
                        ),
                    ],
                    style={'width': 300},
                )
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdDivider(
        'AntdForm Global Configuration', innerTextOrientation='left'
    ),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(), label='Form' + ' Item' * i
                )
                for i in range(1, 4)
            ],
            labelCol={'flex': 'none'},
            wrapperCol={'flex': 'auto'},
            style={'width': 300},
        )
    ),
    fac.AntdDivider(
        'AntdFormItem Individual Configuration',
        innerTextOrientation='left',
    ),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(),
                    label='Example 1',
                    labelCol={'flex': '1'},
                    wrapperCol={'flex': '1'},
                ),
                fac.AntdFormItem(
                    fac.AntdInput(),
                    label='Example 2',
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
