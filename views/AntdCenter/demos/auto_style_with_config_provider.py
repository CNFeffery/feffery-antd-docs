import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdConfigProvider(
        [
            fac.AntdCenter('demo1', style={'height': 200}),
            fac.AntdCenter(
                'demo2',
                style={'height': 200, 'fontSize': 24, 'color': '#ffffb8'},
            ),
        ],
        algorithm='dark',
        token={'colorTextBase': '#d3adf7', 'fontSize': 56},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdConfigProvider(
    [
        fac.AntdCenter('demo1', style={'height': 200}),
        fac.AntdCenter(
            'demo2',
            style={'height': 200, 'fontSize': 24, 'color': '#ffffb8'},
        ),
    ],
    algorithm='dark',
    token={'colorTextBase': '#d3adf7', 'fontSize': 56},
)
"""
    }
]
