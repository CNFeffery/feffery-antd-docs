import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRate(
        count=10, tooltips=[f'等级{i + 1}' for i in range(10)]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRate(
    count=10, tooltips=[f'等级{i + 1}' for i in range(10)]
)
"""
    }
]
