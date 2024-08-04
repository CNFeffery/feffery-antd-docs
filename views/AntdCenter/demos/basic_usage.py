import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCenter(
                '常规居中',
                style={'width': 300, 'height': 150, 'background': '#f0f0f0'},
            ),
            fac.AntdParagraph(
                [
                    '测试内容',
                    fac.AntdCenter(
                        '行内居中',
                        style={
                            'width': 100,
                            'height': 100,
                            'background': '#f0f0f0',
                        },
                        inline=True,
                    ),
                    '测试内容',
                ]
            ),
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
        fac.AntdCenter(
            '常规居中',
            style={'width': 300, 'height': 150, 'background': '#f0f0f0'},
        ),
        fac.AntdParagraph(
            [
                '测试内容',
                fac.AntdCenter(
                    '行内居中',
                    style={
                        'width': 100,
                        'height': 100,
                        'background': '#f0f0f0',
                    },
                    inline=True,
                ),
                '测试内容',
            ]
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
