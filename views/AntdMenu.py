from dash import html
from dash import dcc
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
            ],
            containerId='docs-content',
            targetOffset=200
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

        html.Div(
            html.Span(
                '使用示例',
                id='使用示例',
                style={
                    'borderLeft': '4px solid grey',
                    'padding': '3px 0 3px 10px',
                    'backgroundColor': '#f5f5f5',
                    'fontWeight': 'bold',
                    'fontSize': '1.2rem'
                }
            ),
            style={
                'marginBottom': '10px'
            }
        ),

        html.Div(
            [
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

                fac.AntdDivider(
                    '基础使用方式',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='基础使用方式',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '不同的整体显示模式',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='不同的整体显示模式',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '切换色彩风格',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='切换色彩风格',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '指定默认展开的SubMenu',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='指定默认展开的SubMenu',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '设置默认选中的菜单项',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='设置默认选中的菜单项',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '使用前缀图标',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='使用前缀图标',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '添加导航菜单动态折叠/展开按钮',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='添加导航菜单动态折叠/展开按钮',
            className='div-highlight'
        ),

        html.Div(
            [
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
                                mode='inline'
                            ),
                            style={
                                'flex': 'none',
                                'width': '250px'
                            }
                        ),

                        html.Div(
                            fac.AntdSpin(
                                html.Em('图标home', id='menu-demo-output'),
                                text='回调中'
                            ),
                            style={
                                'flex': 'auto'
                            }
                        ),
                    ],
                    style={
                        'width': '100%',
                        'height': '800px',
                        'display': 'flex'
                    }
                ),

                fac.AntdDivider(
                    '回调示例',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                                mode='inline'
                            ),
                            style={
                                'flex': 'none',
                                'width': '250px'
                            }
                        ),

                        html.Div(
                            fac.AntdSpin(
                                html.Em('图标home', id='menu-demo-output'),
                                text='回调中'
                            ),
                            style={
                                'flex': 'auto'
                            }
                        ),
                    ],
                    style={
                        'width': '100%',
                        'height': '800px',
                        'display': 'flex'
                    }
                ),
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
                    title='点击查看代码',
                    is_open=False,
                    ghost=True
                )

            ],
            style={
                'marginBottom': '40px',
                'padding': '10px 10px 20px 10px',
                'border': '1px solid #f0f0f0'
            },
            id='回调示例',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
