import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAccordion(
                items=[
                    {
                        'title': f'{size}手风琴项示例{i}',
                        'key': i,
                        'children': fac.AntdText(f'{size}手风琴项示例{i}'),
                    }
                    for i in range(1, 3)
                ],
                size=size,
            )
            for size in ['small', 'middle', 'large']
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
        fac.AntdAccordion(
            items=[
                {
                    'title': f'{size}手风琴项示例{i}',
                    'key': i,
                    'children': fac.AntdText(f'{size}手风琴项示例{i}'),
                }
                for i in range(1, 3)
            ],
            size=size,
        )
        for size in ['small', 'middle', 'large']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
