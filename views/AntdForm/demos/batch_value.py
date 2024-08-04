import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdInput(name=f'表单项{i}'), label=f'表单项{i}'
            )
            for i in range(1, 6)
        ],
        id='batch-value-form-demo',
        enableBatchControl=True,
        layout='vertical',
        values={f'表单项{i}': f'这是表单项{i}的设定值' for i in range(1, 6)},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(name=f'表单项{i}'), label=f'表单项{i}'
        )
        for i in range(1, 6)
    ],
    id='batch-value-form-demo',
    enableBatchControl=True,
    layout='vertical',
    values={f'表单项{i}': f'这是表单项{i}的设定值' for i in range(1, 6)},
)
"""
    }
]
