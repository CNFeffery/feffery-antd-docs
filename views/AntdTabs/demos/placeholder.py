import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTabs(
        items=[],
        placeholder=fac.AntdEmpty(description='当前没有可用的标签页哦'),
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTabs(
    items=[],
    placeholder=fac.AntdEmpty(description='当前没有可用的标签页哦'),
)
"""
    }
]
