import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdRibbon(
                fuc.FefferyDiv(
                    shadow='always-shadow',
                    style={
                        'height': '200px',
                        'width': '300px',
                        'borderRadius': '10px',
                    },
                ),
                text='缎带示例',
            ),
            fac.AntdRibbon(
                fuc.FefferyDiv(
                    shadow='always-shadow',
                    style={
                        'height': '200px',
                        'width': '300px',
                        'borderRadius': '10px',
                    },
                ),
                text='缎带示例',
                placement='start',
                color='#ff4d4f',
            ),
        ],
        direction='vertical',
        size='large',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdRibbon(
            fuc.FefferyDiv(
                shadow='always-shadow',
                style={
                    'height': '200px',
                    'width': '300px',
                    'borderRadius': '10px',
                },
            ),
            text='缎带示例',
        ),
        fac.AntdRibbon(
            fuc.FefferyDiv(
                shadow='always-shadow',
                style={
                    'height': '200px',
                    'width': '300px',
                    'borderRadius': '10px',
                },
            ),
            text='缎带示例',
            placement='start',
            color='#ff4d4f',
        ),
    ],
    direction='vertical',
    size='large',
)
"""
    }
]
