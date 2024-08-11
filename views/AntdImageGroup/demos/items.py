import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdImageGroup(
        fac.AntdImage(
            src='/assets/imgs/components/AntdImage/示例图片2.png',
            height=200,
        ),
        items=[
            f'/assets/imgs/components/AntdImage/示例图片{i}.png'
            for i in range(2, 9)
        ],
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdImageGroup(
    fac.AntdImage(
        src='/assets/imgs/components/AntdImage/示例图片2.png',
        height=200,
    ),
    items=[
        f'/assets/imgs/components/AntdImage/示例图片{i}.png'
        for i in range(2, 9)
    ],
)
"""
    }
]
