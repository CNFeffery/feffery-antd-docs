import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdDivider('禁用部分选项', innerTextOrientation='left'),
            fac.AntdCheckboxGroup(
                options=[
                    {
                        'label': f'选项{i}',
                        'value': f'选项{i}',
                        'disabled': i % 2 != 0,
                    }
                    for i in range(5)
                ]
            ),
            fac.AntdDivider('禁用整体', innerTextOrientation='left'),
            fac.AntdCheckboxGroup(
                options=[
                    {'label': f'选项{i}', 'value': f'选项{i}'} for i in range(5)
                ],
                disabled=True,
            ),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDivider(
                'Disabled part of options', innerTextOrientation='left'
            ),
            fac.AntdCheckboxGroup(
                options=[
                    {
                        'label': f'Option{i}',
                        'value': f'Option{i}',
                        'disabled': i % 2 != 0,
                    }
                    for i in range(5)
                ]
            ),
            fac.AntdDivider('Disabled all', innerTextOrientation='left'),
            fac.AntdCheckboxGroup(
                options=[
                    {'label': f'Option{i}', 'value': f'Option{i}'}
                    for i in range(5)
                ],
                disabled=True,
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
    fac.AntdDivider('禁用部分选项', innerTextOrientation='left'),
    fac.AntdCheckboxGroup(
        options=[
            {
                'label': f'选项{i}',
                'value': f'选项{i}',
                'disabled': i % 2 != 0,
            }
            for i in range(5)
        ]
    ),
    fac.AntdDivider('禁用整体', innerTextOrientation='left'),
    fac.AntdCheckboxGroup(
        options=[
            {'label': f'选项{i}', 'value': f'选项{i}'} for i in range(5)
        ],
        disabled=True,
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
        'Disabled part of options', innerTextOrientation='left'
    ),
    fac.AntdCheckboxGroup(
        options=[
            {
                'label': f'Option{i}',
                'value': f'Option{i}',
                'disabled': i % 2 != 0,
            }
            for i in range(5)
        ]
    ),
    fac.AntdDivider('Disabled all', innerTextOrientation='left'),
    fac.AntdCheckboxGroup(
        options=[
            {'label': f'Option{i}', 'value': f'Option{i}'}
            for i in range(5)
        ],
        disabled=True,
    ),
]
"""
            }
        ]
