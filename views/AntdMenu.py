import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdMenu

docs_content = html.Div(
    [
        html.H2(
            'AntdMenu(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '基础使用方式', 'href': '#基础使用方式'},
                        {'title': '不同的整体显示模式', 'href': '#不同的整体显示模式'},
                        {'title': '切换色彩风格', 'href': '#切换色彩风格'},
                        {'title': '指定默认展开的SubMenu', 'href': '#指定默认展开的SubMenu'},
                        {'title': '设置默认选中的菜单项', 'href': '#设置默认选中的菜单项'},
                        {'title': '使用前缀图标', 'href': '#使用前缀图标'},
                        {'title': '添加导航菜单动态折叠/展开按钮', 'href': '#添加导航菜单动态折叠/展开按钮'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ]
                },
            ]
        ),
        html.Span(
            '主要参数说明：',
            id='主要参数说明',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        dcc.Markdown(open('documents/AntdMenu.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Span(
            '使用示例：',
            id='使用示例',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        html.Hr(),

        html.Div(
            [
                html.Strong(
                    '基础使用方式：',
                    id='基础使用方式',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ]
                    ),
                    style={
                        'width': '250px'
                    }
                )
                ```
                '''),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ]
                    ),
                    style={
                        'width': '250px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '不同的整体显示模式：',
                    id='不同的整体显示模式',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdDivider(children='默认mode="vertical"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ]
                    ),
                    style={
                        'width': '250px'
                    }
                ),

                fac.AntdDivider(children='mode="inline"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline'
                    ),
                    style={
                        'width': '250px'
                    }
                ),

                fac.AntdDivider(children='mode="horizontal"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='horizontal'
                    ),
                    style={
                        'width': '250px'
                    }
                )
                ```
                '''),

                fac.AntdDivider(children='默认mode="vertical"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ]
                    ),
                    style={
                        'width': '250px'
                    }
                ),

                fac.AntdDivider(children='mode="inline"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline'
                    ),
                    style={
                        'width': '250px'
                    }
                ),

                fac.AntdDivider(children='mode="horizontal"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='horizontal'
                    ),
                    style={
                        'width': '250px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '切换色彩风格：',
                    id='切换色彩风格',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdDivider(children='默认theme="light"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline'
                    ),
                    style={
                        'width': '250px'
                    }
                ),

                fac.AntdDivider(children='theme="dark"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline',
                        theme='dark'
                    ),
                    style={
                        'width': '250px'
                    }
                )
                ```
                '''),

                fac.AntdDivider(children='默认theme="light"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline'
                    ),
                    style={
                        'width': '250px'
                    }
                ),

                fac.AntdDivider(children='theme="dark"', innerTextOrientation='left'),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline',
                        theme='dark'
                    ),
                    style={
                        'width': '250px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '指定默认展开的SubMenu：',
                    id='指定默认展开的SubMenu',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline',
                        theme='dark',
                        defaultOpenKeys=['1', '3']
                    ),
                    style={
                        'width': '250px'
                    }
                )
                ```
                '''),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline',
                        theme='dark',
                        defaultOpenKeys=['1', '3']
                    ),
                    style={
                        'width': '250px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置默认选中的菜单项：',
                    id='设置默认选中的菜单项',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline',
                        theme='dark',
                        defaultOpenKeys=['1'],
                        defaultSelectedKey='1-2-2'
                    ),
                    style={
                        'width': '250px'
                    }
                )
                ```
                '''),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'SubMenu',
                                'props': {
                                    'key': f'{sub_menu}',
                                    'title': f'子菜单{sub_menu}'
                                },
                                'children': [
                                    {
                                        'component': 'ItemGroup',
                                        'props': {
                                            'key': f'{sub_menu}-{item_group}',
                                            'title': f'菜单项分组{sub_menu}-{item_group}'
                                        },
                                        'children': [
                                            {
                                                'component': 'Item',
                                                'props': {
                                                    'key': f'{sub_menu}-{item_group}-{item}',
                                                    'title': f'菜单项{sub_menu}-{item_group}-{item}'
                                                }
                                            }
                                            for item in range(1, 3)
                                        ]
                                    }
                                    for item_group in range(1, 3)
                                ]
                            }
                            for sub_menu in range(1, 5)
                        ],
                        mode='inline',
                        theme='dark',
                        defaultOpenKeys=['1'],
                        defaultSelectedKey='1-2-2'
                    ),
                    style={
                        'width': '250px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '使用前缀图标：',
                    id='使用前缀图标',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'Item',
                                'props': {
                                    'key': f'图标{icon}',
                                    'title': f'图标{icon}',
                                    'icon': icon
                                }
                            }
                            for icon in [
                                'home',
                                'upload',
                                'bar-chart',
                                'pie-chart',
                                'dot-chart',
                                'line-chart',
                                'apartment',
                                'app-store',
                                'app-store-add',
                                'bell',
                                'calculator',
                                'calendar',
                                'database',
                                'history'
                            ]
                        ],
                        mode='inline'
                    ),
                    style={
                        'width': '250px'
                    }
                )
                ```
                '''),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                            {
                                'component': 'Item',
                                'props': {
                                    'key': f'图标{icon}',
                                    'title': f'图标{icon}',
                                    'icon': icon
                                }
                            }
                            for icon in [
                                'home',
                                'upload',
                                'bar-chart',
                                'pie-chart',
                                'dot-chart',
                                'line-chart',
                                'apartment',
                                'app-store',
                                'app-store-add',
                                'bell',
                                'calculator',
                                'calendar',
                                'database',
                                'history'
                            ]
                        ],
                        mode='inline'
                    ),
                    style={
                        'width': '250px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '添加导航菜单动态折叠/展开按钮：',
                    id='添加导航菜单动态折叠/展开按钮',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                                      {
                                          'component': 'Item',
                                          'props': {
                                              'key': f'图标{icon}',
                                              'title': f'图标{icon}',
                                              'icon': icon
                                          }
                                      }
                                      for icon in [
                                'home',
                                'upload',
                                'bar-chart',
                                'pie-chart',
                                'dot-chart',
                                'line-chart',
                                'apartment',
                                'app-store',
                                'app-store-add',
                                'bell',
                                'calculator',
                                'calendar',
                                'database',
                                'history'
                            ]
                                  ] + [
                                      {
                                          'component': 'Item',
                                          'props': {
                                              'key': '菜单项测试',
                                              'title': '菜单项测试'
                                          }
                                      }
                                  ],
                        mode='inline',
                        renderCollapsedButton=True
                    ),
                    style={
                        'width': '250px'
                    }
                )
                ```
                '''),

                html.Div(
                    fac.AntdMenu(
                        menuItems=[
                                      {
                                          'component': 'Item',
                                          'props': {
                                              'key': f'图标{icon}',
                                              'title': f'图标{icon}',
                                              'icon': icon
                                          }
                                      }
                                      for icon in [
                                'home',
                                'upload',
                                'bar-chart',
                                'pie-chart',
                                'dot-chart',
                                'line-chart',
                                'apartment',
                                'app-store',
                                'app-store-add',
                                'bell',
                                'calculator',
                                'calendar',
                                'database',
                                'history'
                            ]
                                  ] + [
                                      {
                                          'component': 'Item',
                                          'props': {
                                              'key': '菜单项测试',
                                              'title': '菜单项测试'
                                          }
                                      }
                                  ],
                        mode='inline',
                        renderCollapsedButton=True
                    ),
                    style={
                        'width': '250px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '回调示例：',
                    id='回调示例',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        html.Div(
                            fac.AntdMenu(
                                id='menu-demo',
                                menuItems=[
                                              {
                                                  'component': 'Item',
                                                  'props': {
                                                      'key': f'图标{icon}',
                                                      'title': f'图标{icon}',
                                                      'icon': icon
                                                  }
                                              }
                                              for icon in [
                                        'home',
                                        'upload',
                                        'bar-chart',
                                        'pie-chart',
                                        'dot-chart',
                                        'line-chart',
                                        'apartment',
                                        'app-store',
                                        'app-store-add',
                                        'bell',
                                        'calculator',
                                        'calendar',
                                        'database',
                                        'history'
                                    ]
                                          ] + [
                                              {
                                                  'component': 'Item',
                                                  'props': {
                                                      'key': '菜单项测试',
                                                      'title': '菜单项测试'
                                                  }
                                              }
                                          ],
                                defaultSelectedKey='图标home',
                                mode='inline',
                                renderCollapsedButton=True
                            ),
                            style={
                                'flex': 'none',
                                'width': '250px'
                            }
                        ),

                        html.Div(
                            html.Em('图标home', id='menu-demo-output'),
                            style={
                                'flex': 'auto'
                            }
                        )
                    ],
                    style={
                        'width': '100%',
                        'height': '800px',
                        'display': 'flex'
                    }
                )
                ...               
                @app.callback(
                    Output('menu-demo-output', 'children'),
                    Input('menu-demo', 'currentKey'),
                    prevent_initial_call=True
                )
                def menu_callback_demo(currentKey):
                
                    return currentKey

                ```
                '''),

                html.Div(
                    [
                        html.Div(
                            fac.AntdMenu(
                                id='menu-demo',
                                menuItems=[
                                              {
                                                  'component': 'Item',
                                                  'props': {
                                                      'key': f'图标{icon}',
                                                      'title': f'图标{icon}',
                                                      'icon': icon
                                                  }
                                              }
                                              for icon in [
                                        'home',
                                        'upload',
                                        'bar-chart',
                                        'pie-chart',
                                        'dot-chart',
                                        'line-chart',
                                        'apartment',
                                        'app-store',
                                        'app-store-add',
                                        'bell',
                                        'calculator',
                                        'calendar',
                                        'database',
                                        'history'
                                    ]
                                          ] + [
                                              {
                                                  'component': 'Item',
                                                  'props': {
                                                      'key': '菜单项测试',
                                                      'title': '菜单项测试'
                                                  }
                                              }
                                          ],
                                defaultSelectedKey='图标home',
                                mode='inline',
                                renderCollapsedButton=True
                            ),
                            style={
                                'flex': 'none',
                                'width': '250px'
                            }
                        ),

                        html.Div(
                            html.Em('图标home', id='menu-demo-output'),
                            style={
                                'flex': 'auto'
                            }
                        )
                    ],
                    style={
                        'width': '100%',
                        'height': '800px',
                        'display': 'flex'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
