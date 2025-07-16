import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInputNumber(
                variant=variant,
                placeholder=f'variant="{variant}"',
                style={'width': 200},
            )
            for variant in ['outlined', 'borderless', 'filled', 'underlined']
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
        fac.AntdInputNumber(
            variant=variant,
            placeholder=f'variant="{variant}"',
            style={'width': 200},
        )
        for variant in ['outlined', 'borderless', 'filled', 'underlined']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
