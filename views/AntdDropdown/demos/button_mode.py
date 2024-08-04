import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDropdown(
                title='触发点',
                buttonMode=True,
                menuItems=[
                    {'title': '子页面1'},
                    {'title': '子页面2'},
                    {'isDivider': True},
                    {'title': '子页面3-1'},
                    {'title': '子页面3-2'},
                ],
            ),
            fac.AntdDropdown(
                title='触发点',
                buttonMode=True,
                buttonProps={'size': 'large', 'type': 'dashed'},
                menuItems=[
                    {'title': '子页面1'},
                    {'title': '子页面2'},
                    {'isDivider': True},
                    {'title': '子页面3-1'},
                    {'title': '子页面3-2'},
                ],
            ),
            fac.AntdDropdown(
                title='触发点',
                buttonMode=True,
                buttonProps={
                    'size': 'small',
                    'type': 'primary',
                    'danger': True,
                },
                menuItems=[
                    {'title': '子页面1'},
                    {'title': '子页面2'},
                    {'isDivider': True},
                    {'title': '子页面3-1'},
                    {'title': '子页面3-2'},
                ],
            ),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
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
        ),

        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            buttonProps={
                'size': 'large',
                'type': 'dashed'
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
        ),

        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            buttonProps={
                'size': 'small',
                'type': 'primary',
                'danger': True
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
    ]
)
"""
    }
]
