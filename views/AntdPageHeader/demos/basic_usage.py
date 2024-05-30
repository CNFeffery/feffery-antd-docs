import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPageHeader(
        title='页头标题示例', subTitle='页头副标题示例'
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdPageHeader(
    title='页头标题示例',
    subTitle='页头副标题示例'
)
"""
    }
]
