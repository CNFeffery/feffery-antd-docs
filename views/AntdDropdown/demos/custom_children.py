import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdDropdown(
        fac.AntdAvatar(
            icon='antd-user',
            size='large',
            style={'background': '#1890ff', 'cursor': 'pointer'},
        ),
        menuItems=[
            {
                'title': fac.AntdSpace(
                    [
                        fac.AntdAvatar(
                            text='我',
                            mode='text',
                            style={'background': '#2f54eb'},
                        ),
                        fac.AntdSpace(
                            [
                                '用户示例',
                                fac.AntdTag(content='vip', color='red'),
                            ],
                            direction='vertical',
                            size=0,
                        ),
                    ]
                )
            }
        ],
        trigger='hover',
        placement='bottomRight',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdDropdown(
    fac.AntdAvatar(
        icon='antd-user',
        size='large',
        style={
            'background': '#1890ff',
            'cursor': 'pointer'
        }
    ),
    menuItems=[
        {
            'title': fac.AntdSpace(
                [
                    fac.AntdAvatar(
                        text='我',
                        mode='text',
                        style={
                            'background': '#2f54eb'
                        }
                    ),
                    fac.AntdSpace(
                        [
                            '用户示例',
                            fac.AntdTag(
                                content='vip',
                                color='red'
                            )
                        ],
                        direction='vertical',
                        size=0
                    )
                ]
            )
        }
    ],
    trigger='hover',
    placement='bottomRight'
)
"""
    }
]
