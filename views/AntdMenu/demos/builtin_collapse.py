import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdMenu(
        defaultSelectedKey='图标antd-home',
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
                'fc-services',
                'fc-questions',
                'fc-organization',
            ]
        ],
        mode='inline',
        renderCollapsedButton=True,
        style={'maxWidth': 256},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdMenu(
    defaultSelectedKey='图标antd-home',
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
            'fc-services',
            'fc-questions',
            'fc-organization',
        ]
    ],
    mode='inline',
    renderCollapsedButton=True,
    style={'maxWidth': 256},
)
"""
    }
]
