import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
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

    return demo_contents


code_string = [
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
