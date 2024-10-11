import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdDivider(
                'labelWrap=False（默认）', innerTextOrientation='left'
            ),
            fac.AntdCenter(
                fac.AntdForm(
                    [fac.AntdFormItem(fac.AntdInput(), label='超长标签' * 2)],
                    labelCol={'span': 6},
                    labelAlign='left',
                    style={'width': 300},
                )
            ),
            fac.AntdDivider('labelWrap=True', innerTextOrientation='left'),
            fac.AntdCenter(
                fac.AntdForm(
                    [fac.AntdFormItem(fac.AntdInput(), label='超长标签' * 2)],
                    labelCol={'span': 6},
                    labelAlign='left',
                    labelWrap=True,
                    style={'width': 300},
                )
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDivider(
                'labelWrap=False (default)', innerTextOrientation='left'
            ),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdInput(), label=('Extra Long Label')
                        )
                    ],
                    labelCol={'span': 6},
                    labelAlign='left',
                    style={'width': 300},
                )
            ),
            fac.AntdDivider('labelWrap=True', innerTextOrientation='left'),
            fac.AntdCenter(
                fac.AntdForm(
                    [
                        fac.AntdFormItem(
                            fac.AntdInput(), label=('Extra Long Label')
                        )
                    ],
                    labelCol={'span': 6},
                    labelAlign='left',
                    labelWrap=True,
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
    fac.AntdDivider('labelWrap=False（默认）', innerTextOrientation='left'),
    fac.AntdCenter(
        fac.AntdForm(
            [fac.AntdFormItem(fac.AntdInput(), label='超长标签' * 2)],
            labelCol={'span': 6},
            labelAlign='left',
            style={'width': 300},
        )
    ),
    fac.AntdDivider('labelWrap=True', innerTextOrientation='left'),
    fac.AntdCenter(
        fac.AntdForm(
            [fac.AntdFormItem(fac.AntdInput(), label='超长标签' * 2)],
            labelCol={'span': 6},
            labelAlign='left',
            labelWrap=True,
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
        'labelWrap=False (default)', innerTextOrientation='left'
    ),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(), label=('Extra Long Label')
                )
            ],
            labelCol={'span': 6},
            labelAlign='left',
            style={'width': 300},
        )
    ),
    fac.AntdDivider('labelWrap=True', innerTextOrientation='left'),
    fac.AntdCenter(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(), label=('Extra Long Label')
                )
            ],
            labelCol={'span': 6},
            labelAlign='left',
            labelWrap=True,
            style={'width': 300},
        )
    ),
]
"""
            }
        ]
