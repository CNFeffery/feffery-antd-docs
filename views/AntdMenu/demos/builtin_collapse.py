import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdMenu(
            defaultSelectedKey='icon antd-home',
            menuItems=[
                {
                    'component': 'Item',
                    'props': {
                        'key': f'icon {icon}',
                        'title': f'icon {icon}',
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdMenu(
    defaultSelectedKey='icon antd-home',
    menuItems=[
        {
            'component': 'Item',
            'props': {
                'key': f'icon {icon}',
                'title': f'icon {icon}',
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
