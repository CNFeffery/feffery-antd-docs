import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTabs(
        items=[
            {
                'key': f'标签页{i}',
                'label': f'标签页{i}',
                'icon': fac.AntdIcon(icon='antd-user'),
            }
            for i in range(1, 6)
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}',
            'icon': fac.AntdIcon(icon='antd-user'),
        }
        for i in range(1, 6)
    ]
)
"""
    }
]
