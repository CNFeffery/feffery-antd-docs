import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


code_string = [
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
