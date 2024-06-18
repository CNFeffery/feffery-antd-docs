import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdAvatar(icon=icon, style={'background': '#4551f5'})
            for icon in [
                'antd-user',
                'antd-team',
                'antd-github',
                'antd-fire',
                'antd-thunderbolt',
                'antd-robot',
            ]
        ],
        wrap=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdAvatar(icon=icon, style={'background': '#4551f5'})
        for icon in [
            'antd-user',
            'antd-team',
            'antd-github',
            'antd-fire',
            'antd-thunderbolt',
            'antd-robot',
        ]
    ],
    wrap=True,
)
"""
    }
]
