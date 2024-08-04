import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAvatar(),
            fac.AntdAvatar(mode='text', text='F'),
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
            ),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdAvatar(),
        fac.AntdAvatar(mode='text', text='F'),
        fac.AntdAvatar(
            mode='image',
            src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
        ),
    ]
)
"""
    }
]
