import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDescriptions(
        items=[
            {
                'label': 'item1',
                'children': 'default span',
            },
            {
                'label': 'item2',
                'children': 'span="filled"',
                'span': 'filled',
            },
            {
                'label': 'item3',
                'children': 'span="filled"',
                'span': 'filled',
            },
            {
                'label': 'item4',
                'children': 'default span',
            },
        ],
        bordered=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDescriptions(
    items=[
        {
            'label': 'item1',
            'children': 'default span',
        },
        {
            'label': 'item2',
            'children': 'span="filled"',
            'span': 'filled',
        },
        {
            'label': 'item3',
            'children': 'span="filled"',
            'span': 'filled',
        },
        {
            'label': 'item4',
            'children': 'default span',
        },
    ],
    bordered=True,
)
"""
    }
]
