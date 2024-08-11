import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCheckableTag(
                content=f'标签{i}',
            )
            for i in range(1, 6)
        ],
        wrap=True,
        style={
            'width': '100%',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdTag(
            content=f'标签{i}',
        )
        for i in range(1, 6)
    ],
    wrap=True,
    style={
        'width': '100%',
    },
)
"""
    }
]
