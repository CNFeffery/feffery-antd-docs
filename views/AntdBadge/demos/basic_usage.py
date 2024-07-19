import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdBadge(
                fac.AntdAvatar(
                    mode='image',
                    src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                ),
                count=6,
            ),
            fac.AntdBadge(
                fac.AntdAvatar(
                    mode='image',
                    src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                ),
                count=56,
                overflowCount=50,
            ),
            fac.AntdBadge(
                fac.AntdAvatar(
                    mode='image',
                    shape='square',
                    src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                ),
                dot=True,
            ),
            fac.AntdBadge(
                fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
                count=6,
            ),
            fac.AntdBadge(
                fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
                count=56,
                overflowCount=50,
            ),
            fac.AntdBadge(
                fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
                dot=True,
            ),
            fac.AntdBadge(
                fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
                dot=True,
                offset=[-8, 6],
            ),
        ],
        size=20,
        wrap=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
            ),
            count=6,
        ),
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
            ),
            count=56,
            overflowCount=50,
        ),
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                shape='square',
                src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
            ),
            dot=True,
        ),
        fac.AntdBadge(
            fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
            count=6,
        ),
        fac.AntdBadge(
            fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
            count=56,
            overflowCount=50,
        ),
        fac.AntdBadge(
            fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
            dot=True,
        ),
        fac.AntdBadge(
            fac.AntdIcon(icon='fc-advertising', style={'fontSize': '40px'}),
            dot=True,
            offset=[-8, 6],
        ),
    ],
    size=20,
    wrap=True,
)
"""
    }
]