import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdEmpty(
        image='/assets/imgs/components/AntdEmpty/自定义占位图.png',
        description=fac.AntdText('当前页面开发中...', type='secondary'),
        imageStyle={'height': 250},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdEmpty(
    image='/assets/imgs/components/AntdEmpty/自定义占位图.png',
    description=fac.AntdText('当前页面开发中...', type='secondary'),
    imageStyle={'height': 250},
)
"""
    }
]
