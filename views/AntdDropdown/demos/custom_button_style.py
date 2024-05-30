import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDropdown(
        title='触发点',
        buttonMode=True,
        buttonProps={
            'style': {
                'color': 'white',
                'width': 150,
                'background': 'linear-gradient(135deg,#8a2be2,#ffa500,#f8f8ff)',
            }
        },
        menuItems=[
            {'title': '子页面1'},
            {'title': '子页面2'},
            {'isDivider': True},
            {'title': '子页面3-1'},
            {'title': '子页面3-2'},
        ],
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDropdown(
    title='触发点',
    buttonMode=True,
    buttonProps={
        'style': {
            'color': 'white',
            'width': 150,
            'background': 'linear-gradient(135deg,#8a2be2,#ffa500,#f8f8ff)'
        }
    },
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
    ]
)
"""
    }
]
