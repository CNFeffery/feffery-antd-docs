import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDropdown(
                title=placement,
                arrow=True,
                placement=placement,
                menuItems=[
                    {'title': '子页面1'},
                    {'title': '子页面2'},
                    {'isDivider': True},
                    {'title': '子页面3-1'},
                    {'title': '子页面3-2'},
                ],
            )
            for placement in [
                'bottomLeft',
                'bottomCenter',
                'bottomRight',
                'topLeft',
                'topCenter',
                'topRight',
            ]
        ],
        size=20,
        wrap=True
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDropdown(
            title=placement,
            arrow=True,
            placement=placement,
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
        for placement in [
            'bottomLeft', 'bottomCenter', 'bottomRight',
            'topLeft', 'topCenter', 'topRight']
    ],
    size=20,
    wrap=True
)
"""
    }
]
