import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCarousel(
        [
            fac.AntdCenter(
                i,
                style={
                    'color': 'white',
                    'fontSize': 36,
                    'height': 160,
                    'backgroundColor': '#364d79',
                },
            )
            for i in range(1, 6)
        ],
        autoplay=True,
        autoplaySpeed=500,  # 500毫秒切换一次
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdCarousel(
    [
        fac.AntdCenter(
            i,
            style={
                'color': 'white',
                'fontSize': 36,
                'height': 160,
                'backgroundColor': '#364d79',
            },
        )
        for i in range(1, 6)
    ],
    autoplay=True,
    autoplaySpeed=500,  # 500毫秒切换一次
)
"""
    }
]
