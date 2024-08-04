import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('手风琴模式开', innerTextOrientation='left'),
        fac.AntdAccordion(
            items=[
                {
                    'title': f'手风琴项示例{i}',
                    'key': i,
                    'children': fac.AntdText(f'手风琴项示例{i}'),
                }
                for i in range(1, 6)
            ],
            defaultActiveKey=['3'],
        ),
        fac.AntdDivider('手风琴模式关', innerTextOrientation='left'),
        fac.AntdAccordion(
            items=[
                {
                    'title': f'手风琴项示例{i}',
                    'key': i,
                    'children': fac.AntdText(f'手风琴项示例{i}'),
                }
                for i in range(1, 6)
            ],
            defaultActiveKey=['1', '3', '4'],
            accordion=False,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('手风琴模式开', innerTextOrientation='left'),
    fac.AntdAccordion(
        items=[
            {
                'title': f'手风琴项示例{i}',
                'key': i,
                'children': fac.AntdText(f'手风琴项示例{i}'),
            }
            for i in range(1, 6)
        ],
        defaultActiveKey=['3'],
    ),
    fac.AntdDivider('手风琴模式关', innerTextOrientation='left'),
    fac.AntdAccordion(
        items=[
            {
                'title': f'手风琴项示例{i}',
                'key': i,
                'children': fac.AntdText(f'手风琴项示例{i}'),
            }
            for i in range(1, 6)
        ],
        defaultActiveKey=['1', '3', '4'],
        accordion=False,
    ),
]
"""
    }
]
