import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('默认占位图', innerTextOrientation='left'),
        fac.AntdImage(
            src='/assets/imgs/不存在图片示例.jpg', preview=False, height=100
        ),
        fac.AntdDivider('自定义占位图', innerTextOrientation='left'),
        fac.AntdImage(
            src='/assets/imgs/不存在图片示例.jpg',
            fallback='/assets/imgs/components/AntdImage/示例占位图.png',
            preview=False,
            height=100,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('默认占位图', innerTextOrientation='left'),
    fac.AntdImage(
        src='/assets/imgs/不存在图片示例.jpg', preview=False, height=100
    ),
    fac.AntdDivider('自定义占位图', innerTextOrientation='left'),
    fac.AntdImage(
        src='/assets/imgs/不存在图片示例.jpg',
        fallback='/assets/imgs/components/AntdImage/示例占位图.png',
        preview=False,
        height=100,
    ),
]
"""
    }
]
