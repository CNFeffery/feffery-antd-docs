import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider(
            'multiImageMode="fold"（默认）', innerTextOrientation='left'
        ),
        fac.AntdImage(
            src=[
                f'/assets/imgs/components/AntdImage/示例图片{i}.png'
                for i in range(2, 9)
            ],
            height=80,
        ),
        fac.AntdDivider(
            'multiImageMode="unfold"（默认）', innerTextOrientation='left'
        ),
        fac.AntdImage(
            src=[
                f'/assets/imgs/components/AntdImage/示例图片{i}.png'
                for i in range(2, 9)
            ],
            multiImageMode='unfold',
            height=80,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider(
        'multiImageMode="fold"（默认）', innerTextOrientation='left'
    ),
    fac.AntdImage(
        src=[
            f'/assets/imgs/components/AntdImage/示例图片{i}.png'
            for i in range(2, 9)
        ],
        height=80,
    ),
    fac.AntdDivider(
        'multiImageMode="unfold"（默认）', innerTextOrientation='left'
    ),
    fac.AntdImage(
        src=[
            f'/assets/imgs/components/AntdImage/示例图片{i}.png'
            for i in range(2, 9)
        ],
        multiImageMode='unfold',
        height=80,
    ),
]
"""
    }
]
