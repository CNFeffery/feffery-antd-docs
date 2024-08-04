import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTag(
                content='fac.AntdTag',
                href='AntdTag',
                # 跳转行为：当页跳转
                target='_self',
                color='blue',
            ),
            fac.AntdTag(
                content='fmc官网',
                href='https://fmc.feffery.tech',
                # 跳转行为：新标签页跳转（默认）
                target='_blank',
                color='green',
            ),
            fac.AntdTag(
                content='fuc官网', href='https://fuc.feffery.tech', color='cyan'
            ),
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
            content='fac.AntdTag',
            href='AntdTag',
            # 跳转行为：当页跳转
            target='_self',
            color='blue',
        ),
        fac.AntdTag(
            content='fmc官网',
            href='https://fmc.feffery.tech',
            # 跳转行为：新标签页跳转（默认）
            target='_blank',
            color='green',
        ),
        fac.AntdTag(
            content='fuc官网', href='https://fuc.feffery.tech', color='cyan'
        ),
    ],
    wrap=True,
    style={
        'width': '100%',
    },
)
"""
    }
]
