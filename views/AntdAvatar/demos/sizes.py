import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAvatar(size='small'),
            fac.AntdAvatar(),
            fac.AntdAvatar(size='large'),
            fac.AntdAvatar(size=64),
        ],
        align='center',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdAvatar(size='small'),
        fac.AntdAvatar(),
        fac.AntdAvatar(size='large'),
        fac.AntdAvatar(size=64),
    ],
    align='center',
)
"""
    }
]
