import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSteps(
        steps=[{'title': f'步骤{i + 1}'} for i in range(3)],
        current=1,
        percent=66,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSteps(
    steps=[{'title': f'步骤{i + 1}'} for i in range(3)],
    current=1,
    percent=66,
)
"""
    }
]
