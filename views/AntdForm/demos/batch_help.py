import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdForm(
            [
                fac.AntdFormItem(fac.AntdInput(), label=f'表单项{i}')
                for i in range(1, 6)
            ],
            id='batch-helps-form-demo',
            enableBatchControl=True,
            layout='vertical',
            helps={
                f'表单项{i}': f'这是表单项{i}的帮助信息' for i in range(1, 6)
            },
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdForm(
            [
                fac.AntdFormItem(fac.AntdInput(), label=f'FormItem{i}')
                for i in range(1, 6)
            ],
            id='batch-helps-form-demo',
            enableBatchControl=True,
            layout='vertical',
            helps={
                f'FormItem{i}': f'This is the help information for FormItem{i}'
                for i in range(1, 6)
            },
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdForm(
    [
        fac.AntdFormItem(fac.AntdInput(), label=f'表单项{i}')
        for i in range(1, 6)
    ],
    id='batch-helps-form-demo',
    enableBatchControl=True,
    layout='vertical',
    helps={f'表单项{i}': f'这是表单项{i}的帮助信息' for i in range(1, 6)},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdForm(
    [
        fac.AntdFormItem(fac.AntdInput(), label=f'FormItem{i}')
        for i in range(1, 6)
    ],
    id='batch-helps-form-demo',
    enableBatchControl=True,
    layout='vertical',
    helps={
        f'FormItem{i}': f'This is the help information for FormItem{i}'
        for i in range(1, 6)
    },
)
"""
            }
        ]
