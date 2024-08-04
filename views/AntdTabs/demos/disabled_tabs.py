import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('基于disabled参数', innerTextOrientation='left'),
        fac.AntdTabs(
            items=[
                {
                    'key': f'标签页{i}',
                    'label': f'标签页{i}',
                    'disabled': i in [3, 4],
                }
                for i in range(1, 6)
            ]
        ),
        fac.AntdDivider('基于disabledTabKeys参数', innerTextOrientation='left'),
        fac.AntdTabs(
            items=[
                {'key': f'标签页{i}', 'label': f'标签页{i}'}
                for i in range(1, 6)
            ],
            disabledTabKeys=['标签页3', '标签页4'],
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('基于disabled参数', innerTextOrientation='left'),
    fac.AntdTabs(
        items=[
            {
                'key': f'标签页{i}',
                'label': f'标签页{i}',
                'disabled': i in [3, 4],
            }
            for i in range(1, 6)
        ]
    ),
    fac.AntdDivider('基于disabledTabKeys参数', innerTextOrientation='left'),
    fac.AntdTabs(
        items=[
            {'key': f'标签页{i}', 'label': f'标签页{i}'}
            for i in range(1, 6)
        ],
        disabledTabKeys=['标签页3', '标签页4'],
    ),
]
"""
    }
]
