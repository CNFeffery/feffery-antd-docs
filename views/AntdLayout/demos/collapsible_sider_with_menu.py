import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdLayout(
        [
            fac.AntdSider(
                [
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'Item',
                                'props': {
                                    'key': f'图标{icon}',
                                    'title': f'图标{icon}',
                                    'icon': icon,
                                },
                            }
                            for icon in [
                                'antd-home',
                                'antd-cloud-upload',
                                'antd-bar-chart',
                                'antd-pie-chart',
                                'antd-dot-chart',
                                'antd-line-chart',
                                'antd-apartment',
                                'antd-app-store',
                                'antd-app-store-add',
                                'antd-bell',
                                'antd-calculator',
                                'antd-calendar',
                                'antd-database',
                                'antd-history',
                            ]
                        ],
                        mode='inline',
                        style={'height': '100%', 'overflow': 'hidden auto'},
                    )
                ],
                collapsible=True,
                collapsedWidth=60,
                style={'backgroundColor': 'rgb(240, 242, 245)'},
            ),
            fac.AntdContent(
                fac.AntdCenter(
                    fac.AntdTitle('内容区示例', level=2, style={'margin': '0'}),
                    style={
                        'height': '100%',
                    },
                ),
                style={'backgroundColor': 'white'},
            ),
        ],
        style={'height': '100vh'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdLayout(
    [
        fac.AntdSider(
            [
                fac.AntdMenu(
                    menuItems=[
                        {
                            'component': 'Item',
                            'props': {
                                'key': f'图标{icon}',
                                'title': f'图标{icon}',
                                'icon': icon,
                            },
                        }
                        for icon in [
                            'antd-home',
                            'antd-cloud-upload',
                            'antd-bar-chart',
                            'antd-pie-chart',
                            'antd-dot-chart',
                            'antd-line-chart',
                            'antd-apartment',
                            'antd-app-store',
                            'antd-app-store-add',
                            'antd-bell',
                            'antd-calculator',
                            'antd-calendar',
                            'antd-database',
                            'antd-history',
                        ]
                    ],
                    mode='inline',
                    style={'height': '100%', 'overflow': 'hidden auto'},
                )
            ],
            collapsible=True,
            collapsedWidth=60,
            style={'backgroundColor': 'rgb(240, 242, 245)'},
        ),
        fac.AntdContent(
            fac.AntdCenter(
                fac.AntdTitle('内容区示例', level=2, style={'margin': '0'}),
                style={
                    'height': '100%',
                },
            ),
            style={'backgroundColor': 'white'},
        ),
    ],
    style={'height': '100vh'},
)
"""
    }
]
