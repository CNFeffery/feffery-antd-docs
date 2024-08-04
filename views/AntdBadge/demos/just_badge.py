import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdBadge(count=8),
            fac.AntdBadge(count=101),
            fac.AntdBadge(count=101, size='small'),
            fac.AntdBadge(dot=True, status='success'),
            fac.AntdBadge(dot=True, status='error'),
            fac.AntdBadge(dot=True, status='default'),
            fac.AntdBadge(dot=True, status='processing'),
            fac.AntdBadge(dot=True, status='warning'),
        ],
        size=20,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdBadge(count=8),
        fac.AntdBadge(count=101),
        fac.AntdBadge(count=101, size='small'),
        fac.AntdBadge(dot=True, status='success'),
        fac.AntdBadge(dot=True, status='error'),
        fac.AntdBadge(dot=True, status='default'),
        fac.AntdBadge(dot=True, status='processing'),
        fac.AntdBadge(dot=True, status='warning'),
    ],
    size=20,
)
"""
    }
]
