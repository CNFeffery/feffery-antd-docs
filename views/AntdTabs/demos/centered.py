import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTabs(
        items=[
            {'key': f'标签页{i}', 'label': f'标签页{i}'} for i in range(1, 6)
        ],
        centered=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTabs(
    items=[
        {'key': f'标签页{i}', 'label': f'标签页{i}'} for i in range(1, 6)
    ],
    centered=True,
)
"""
    }
]
