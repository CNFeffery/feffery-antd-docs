import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdAvatarGroup(
        [
            fac.AntdAvatar(
                mode='text', text='F', style={'background': background}
            )
            for background in [
                '#d29200',
                '#ffb900',
                '#fff100',
                '#d83b01',
                '#ea4300',
                '#00188f',
                '#004b50',
            ]
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdAvatarGroup(
    [
        fac.AntdAvatar(
            mode='text', text='F', style={'background': background}
        )
        for background in [
            '#d29200',
            '#ffb900',
            '#fff100',
            '#d83b01',
            '#ea4300',
            '#00188f',
            '#004b50',
        ]
    ]
)
"""
    }
]
