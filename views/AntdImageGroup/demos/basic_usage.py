import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdImageGroup(
        fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        fac.AntdImage(
                            src=f'/assets/imgs/components/AntdImage/示例图片{i}.png',
                            height=100,
                        )
                        for i in range(2, 5)
                    ]
                ),
                fac.AntdSpace(
                    [
                        fac.AntdImage(
                            src=f'/assets/imgs/components/AntdImage/示例图片{i}.png',
                            height=100,
                        )
                        for i in range(5, 7)
                    ]
                ),
                fac.AntdSpace(
                    [
                        fac.AntdImage(
                            src=f'/assets/imgs/components/AntdImage/示例图片{i}.png',
                            height=100,
                        )
                        for i in range(7, 9)
                    ]
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdImageGroup(
    fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdImage(
                        src=f'/assets/imgs/components/AntdImage/示例图片{i}.png',
                        height=100,
                    )
                    for i in range(2, 5)
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdImage(
                        src=f'/assets/imgs/components/AntdImage/示例图片{i}.png',
                        height=100,
                    )
                    for i in range(5, 7)
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdImage(
                        src=f'/assets/imgs/components/AntdImage/示例图片{i}.png',
                        height=100,
                    )
                    for i in range(7, 9)
                ]
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )
)
"""
    }
]
