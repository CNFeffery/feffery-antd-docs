import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCollapse(
                fac.AntdParagraph('内容示例' * 20),
                title=f'size="{size}"',
                size=size,
                isOpen=False,
                style={'width': 300},
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
        fac.AntdCollapse(
            fac.AntdParagraph('内容示例' * 20),
            title=f'size="{size}"',
            style={'width': 300},
        )
        for size in ['small', 'middle', 'large']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
