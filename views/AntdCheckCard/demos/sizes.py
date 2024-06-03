import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCheckCard(f'size="{size}"', size=size)
            for size in ['small', 'default', 'large']
        ],
        direction='vertical',
        size=0,
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCheckCard(f'size="{size}"', size=size)
        for size in ['small', 'default', 'large']
    ],
    direction='vertical',
    size=0,
    style={'width': '100%'},
)
"""
    }
]
