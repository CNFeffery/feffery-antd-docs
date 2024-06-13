import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('封面图片示例', innerTextOrientation='left'),
            fac.AntdCard(
                '内容',
                title='标题',
                coverImg={
                    'alt': '图片加载失败！',
                    'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
                },
                style={'width': 300, 'marginBottom': 10},
            ),
            fac.AntdDivider('加载失败alt信息示例', innerTextOrientation='left'),
            fac.AntdCard(
                '内容',
                title='标题',
                coverImg={
                    'alt': '图片加载失败！',
                    'src': 'https://错误的src地址',
                },
                style={'width': 300, 'marginBottom': 10},
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('封面图片示例', innerTextOrientation='left'),
        fac.AntdCard(
            '内容',
            title='标题',
            coverImg={
                'alt': '图片加载失败！',
                'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
            },
            style={'width': 300, 'marginBottom': 10},
        ),
        fac.AntdDivider('加载失败alt信息示例', innerTextOrientation='left'),
        fac.AntdCard(
            '内容',
            title='标题',
            coverImg={
                'alt': '图片加载失败！',
                'src': 'https://错误的src地址',
            },
            style={'width': 300, 'marginBottom': 10},
        ),
    ],
    direction='vertical',
)
"""
    }
]
