import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdLayout(
            [
                fac.AntdSider(
                    [
                        # 自定义折叠按钮
                        fac.AntdButton(
                            id='menu-collapse-sider-custom-demo-trigger',
                            icon=fac.AntdIcon(
                                id='menu-collapse-sider-custom-demo-trigger-icon',
                                icon='antd-arrow-left',
                                style={'fontSize': '14px'},
                            ),
                            shape='circle',
                            type='text',
                            style={
                                'position': 'absolute',
                                'zIndex': 1,
                                'top': 25,
                                'right': -13,
                                'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 10px 0px',
                                'background': 'white',
                            },
                        ),
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
                        ),
                    ],
                    id='menu-collapse-sider-custom-demo',
                    collapsible=True,
                    collapsedWidth=60,
                    trigger=None,
                    style={'position': 'relative'},
                ),
                fac.AntdContent(style={'background': '#f8f9fa'}),
            ],
            style={'height': 600},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdLayout(
            [
                fac.AntdSider(
                    [
                        # custom collapse button
                        fac.AntdButton(
                            id='menu-collapse-sider-custom-demo-trigger',
                            icon=fac.AntdIcon(
                                id='menu-collapse-sider-custom-demo-trigger-icon',
                                icon='antd-arrow-left',
                                style={'fontSize': '14px'},
                            ),
                            shape='circle',
                            type='text',
                            style={
                                'position': 'absolute',
                                'zIndex': 1,
                                'top': 25,
                                'right': -13,
                                'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 10px 0px',
                                'background': 'white',
                            },
                        ),
                        fac.AntdMenu(
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
                                ]
                            ],
                            mode='inline',
                            style={'height': '100%', 'overflow': 'hidden auto'},
                        ),
                    ],
                    id='menu-collapse-sider-custom-demo',
                    collapsible=True,
                    collapsedWidth=60,
                    trigger=None,
                    style={'position': 'relative'},
                ),
                fac.AntdContent(style={'background': '#f8f9fa'}),
            ],
            style={'height': 600},
        )

    return demo_contents


app.clientside_callback(
    """(nClicks, collapsed) => {
        return [!collapsed, collapsed ? 'antd-arrow-left' : 'antd-arrow-right'];
    }""",
    [
        Output('menu-collapse-sider-custom-demo', 'collapsed'),
        Output('menu-collapse-sider-custom-demo-trigger-icon', 'icon'),
    ],
    Input('menu-collapse-sider-custom-demo-trigger', 'nClicks'),
    State('menu-collapse-sider-custom-demo', 'collapsed'),
    prevent_initial_call=True,
)


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': '''
fac.AntdLayout(
    [
        fac.AntdSider(
            [
                # 自定义折叠按钮
                fac.AntdButton(
                    id='menu-collapse-sider-custom-demo-trigger',
                    icon=fac.AntdIcon(
                        id='menu-collapse-sider-custom-demo-trigger-icon',
                        icon='antd-arrow-left',
                        style={'fontSize': '14px'},
                    ),
                    shape='circle',
                    type='text',
                    style={
                        'position': 'absolute',
                        'zIndex': 1,
                        'top': 25,
                        'right': -13,
                        'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 10px 0px',
                        'background': 'white',
                    },
                ),
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
                ),
            ],
            id='menu-collapse-sider-custom-demo',
            collapsible=True,
            collapsedWidth=60,
            trigger=None,
            style={'position': 'relative'},
        ),
        fac.AntdContent(style={'background': '#f8f9fa'}),
    ],
    style={'height': 600},
)

...

app.clientside_callback(
    """(nClicks, collapsed) => {
        return [!collapsed, collapsed ? 'antd-arrow-left' : 'antd-arrow-right'];
    }""",
    [
        Output('menu-collapse-sider-custom-demo', 'collapsed'),
        Output('menu-collapse-sider-custom-demo-trigger-icon', 'icon'),
    ],
    Input('menu-collapse-sider-custom-demo-trigger', 'nClicks'),
    State('menu-collapse-sider-custom-demo', 'collapsed'),
    prevent_initial_call=True,
)
'''
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': '''
fac.AntdLayout(
    [
        fac.AntdSider(
            [
                # custom collapse button
                fac.AntdButton(
                    id='menu-collapse-sider-custom-demo-trigger',
                    icon=fac.AntdIcon(
                        id='menu-collapse-sider-custom-demo-trigger-icon',
                        icon='antd-arrow-left',
                        style={'fontSize': '14px'},
                    ),
                    shape='circle',
                    type='text',
                    style={
                        'position': 'absolute',
                        'zIndex': 1,
                        'top': 25,
                        'right': -13,
                        'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 10px 0px',
                        'background': 'white',
                    },
                ),
                fac.AntdMenu(
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
                        ]
                    ],
                    mode='inline',
                    style={'height': '100%', 'overflow': 'hidden auto'},
                ),
            ],
            id='menu-collapse-sider-custom-demo',
            collapsible=True,
            collapsedWidth=60,
            trigger=None,
            style={'position': 'relative'},
        ),
        fac.AntdContent(style={'background': '#f8f9fa'}),
    ],
    style={'height': 600},
)

...

app.clientside_callback(
    """(nClicks, collapsed) => {
        return [!collapsed, collapsed ? 'antd-arrow-left' : 'antd-arrow-right'];
    }""",
    [
        Output('menu-collapse-sider-custom-demo', 'collapsed'),
        Output('menu-collapse-sider-custom-demo-trigger-icon', 'icon'),
    ],
    Input('menu-collapse-sider-custom-demo-trigger', 'nClicks'),
    State('menu-collapse-sider-custom-demo', 'collapsed'),
    prevent_initial_call=True,
)
'''
            }
        ]
