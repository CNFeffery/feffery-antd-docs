import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdAccordion(
        items=[
            {
                'title': f'手风琴项示例{i}',
                'key': i,
                'children': fac.AntdText(f'手风琴项示例{i}'),
                'extra': fac.AntdButton('额外内容', type='link', size='small'),
            }
            for i in range(1, 6)
        ],
        collapsible='header',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(f'手风琴项示例{i}'),
            'extra': fac.AntdButton('额外内容', type='link', size='small'),
        }
        for i in range(1, 6)
    ],
    collapsible='header',
)
"""
    }
]
