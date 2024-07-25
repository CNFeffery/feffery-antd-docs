import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTabs(
                items=[
                    {'key': f'标签页{i}', 'label': f'标签页{i}'}
                    for i in range(1, 6)
                ],
                type=type_,
            )
            for type_ in ['line', 'card', 'editable-card']
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdTabs(
            items=[
                {'key': f'标签页{i}', 'label': f'标签页{i}'}
                for i in range(1, 6)
            ],
            type=type_,
        )
        for type_ in ['line', 'card', 'editable-card']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
