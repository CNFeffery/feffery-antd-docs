import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdImage(
        src='/assets/imgs/components/AntdImage/示例图片1.jpg', height=400
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdImage(
    src='/assets/imgs/components/AntdImage/示例图片1.jpg.jpg', height=400
)
"""
    }
]
