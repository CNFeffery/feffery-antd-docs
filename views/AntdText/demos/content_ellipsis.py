import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdText(
                '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100, ellipsis=True
            ),
            fac.AntdText(
                '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100,
                ellipsis={'suffix': '👉'},
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
        fac.AntdText(
            '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100, ellipsis=True
        ),
        fac.AntdText(
            '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100,
            ellipsis={'suffix': '👉'},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
