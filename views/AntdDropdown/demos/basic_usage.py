import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDropdown(
        title='触发点',
        menuItems=[
            {'title': '选项1'},
            {'title': '选项2'},
            {'isDivider': True},
            {'title': '选项3-1'},
            {'title': '选项3-2'},
        ],
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDropdown(
    title='触发点',
    menuItems=[
        {
            'title': '选项1'
        },
        {
            'title': '选项2'
        },
        {
            'isDivider': True
        },
        {
            'title': '选项3-1'
        },
        {
            'title': '选项3-2'
        }
    ]
)
"""
    }
]
