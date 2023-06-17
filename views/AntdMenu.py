from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdMenu
from .side_props import render_side_props_layout


def docs_content(language: str = '中文'):

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(
                        duration=0.3
                    ),

                    fac.AntdBreadcrumb(
                        items=[
                            {
                                'title': '组件介绍'
                            },
                            {
                                'title': '导航'
                            },
                            {
                                'title': 'AntdMenu 导航菜单'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                '　　导航菜单用于引导用户在不同层级的页面之间进行跳转，一般分为顶部导航和侧边导航，顶部导航提供全局性的类目和功能，侧边导航提供多级结构来收纳和排列网站架构。')
                        ]
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
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
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
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='基础使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '默认mode="vertical"',
                                innerTextOrientation='left'
                            ),

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
                                'mode="inline"',
                                innerTextOrientation='left'
                            ),

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

                            fac.AntdDivider(
                                'mode="horizontal"',
                                innerTextOrientation='left'
                            ),

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
                                '不同的显示模式',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdDivider(
    '默认mode="vertical"',
    innerTextOrientation='left'
),

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
    'mode="inline"',
    innerTextOrientation='left'
),

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

fac.AntdDivider(
    'mode="horizontal"',
    innerTextOrientation='left'
),

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
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='不同的显示模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'theme="dark"',
                                innerTextOrientation='left'
                            ),

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
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdDivider(
    'theme="dark"',
    innerTextOrientation='left'
),

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
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
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
                                    defaultOpenKeys=['1', '3']
                                ),
                                style={
                                    'width': '250px'
                                }
                            ),

                            fac.AntdDivider(
                                '设置默认展开项',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
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
        defaultOpenKeys=['1', '3']
    ),
    style={
        'width': '250px'
    }
)
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='设置默认展开项',
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
                                '设置默认选中项',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
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
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='设置默认选中项',
                        className='div-highlight'
                    ),

                    html.Div(
                        [

                            html.Div(
                                fac.AntdMenu(
                                    defaultSelectedKey='图标antd-home',
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
                                            'fc-organization'
                                        ]
                                    ],
                                    mode='inline'
                                ),
                                style={
                                    'width': '250px'
                                }
                            ),

                            fac.AntdDivider(
                                '设置菜单项前缀图标',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText('　　通过icon参数可引用'),
                                    fac.AntdText('AntdIcon', strong=True),
                                    fac.AntdText('中所有内置icon充当菜单项前缀图标')
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
html.Div(
    fac.AntdMenu(
        defaultSelectedKey='图标antd-home',
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
                'fc-organization'
            ]
        ],
        mode='inline'
    ),
    style={
        'width': '250px'
    }
)
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='设置菜单项前缀图标',
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
                                                'key': 'AntdMenu文档页',
                                                'title': 'AntdMenu文档页',
                                                'href': '/AntdMenu'
                                            }
                                        },
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': 'fac仓库',
                                                'title': 'fac仓库',
                                                'href': 'https://github.com/CNFeffery/feffery-antd-components'
                                            }
                                        },
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': 'fuc仓库',
                                                'title': 'fuc仓库',
                                                'href': 'https://github.com/CNFeffery/feffery-utils-components'
                                            }
                                        },
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': 'fmc仓库',
                                                'title': 'fmc仓库',
                                                'href': 'https://github.com/CNFeffery/feffery-markdown-components'
                                            }
                                        },
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': 'feffery博客园',
                                                'title': 'feffery博客园',
                                                'href': 'https://www.cnblogs.com/feffery/'
                                            }
                                        }
                                    ],
                                    mode='inline',
                                    theme='dark'
                                ),
                                style={
                                    'width': '250px'
                                }
                            ),

                            fac.AntdDivider(
                                '链接跳转功能',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
html.Div(
    fac.AntdMenu(
        menuItems=[
            {
                'component': 'Item',
                'props': {
                    'key': 'AntdMenu文档页',
                    'title': 'AntdMenu文档页',
                    'href': '/AntdMenu'
                }
            },
            {
                'component': 'Item',
                'props': {
                    'key': 'fac仓库',
                    'title': 'fac仓库',
                    'href': 'https://github.com/CNFeffery/feffery-antd-components'
                }
            },
            {
                'component': 'Item',
                'props': {
                    'key': 'fuc仓库',
                    'title': 'fuc仓库',
                    'href': 'https://github.com/CNFeffery/feffery-utils-components'
                }
            },
            {
                'component': 'Item',
                'props': {
                    'key': 'fmc仓库',
                    'title': 'fmc仓库',
                    'href': 'https://github.com/CNFeffery/feffery-markdown-components'
                }
            },
            {
                'component': 'Item',
                'props': {
                    'key': 'feffery博客园',
                    'title': 'feffery博客园',
                    'href': 'https://www.cnblogs.com/feffery/'
                }
            }
        ],
        mode='inline',
        theme='dark'
    ),
    style={
        'width': '250px'
    }
)
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='链接跳转功能',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdMenu(
                                defaultSelectedKey='图标antd-home',
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
                                        'fc-organization'
                                    ]
                                ],
                                mode='inline',
                                renderCollapsedButton=True,
                                theme='dark',
                                style={
                                    'maxWidth': '225px'
                                }
                            ),

                            fac.AntdDivider(
                                '使用自带的折叠功能',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdMenu(
    defaultSelectedKey='图标antd-home',
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
            'fc-organization'
        ]
    ],
    mode='inline',
    renderCollapsedButton=True,
    theme='dark',
    style={
        'maxWidth': '225px'
    }
)
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='使用自带的折叠功能',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '基于AntdSider自带折叠功能',
                                innerTextOrientation='left'
                            ),

                            # 侧边栏自带折叠触发区域默认会紧贴页面下边界
                            # 这里为方便局部展示示例，基于fuc.FefferyStyle强制覆盖默认样式
                            fuc.FefferyStyle(
                                rawStyle='''
.sider-demo .ant-layout-sider-trigger {
  position: absolute !important;
}
'''
                            ),

                            html.Div(
                                [
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
                                                                    'icon': icon
                                                                }
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
                                                                'antd-history'
                                                            ]
                                                        ],
                                                        mode='inline',
                                                        style={
                                                            'height': '100%',
                                                            'overflow': 'hidden auto'
                                                        }
                                                    )
                                                ],
                                                collapsible=True,
                                                collapsedWidth=60
                                            ),

                                            fac.AntdContent(
                                                style={
                                                    'background': '#f8f9fa'
                                                }
                                            )
                                        ],
                                        style={
                                            'height': '600px'
                                        }
                                    )
                                ],
                                className='sider-demo',
                                style={
                                    'height': '600px',
                                    'border': '1px solid rgb(241, 241, 241)'
                                }
                            ),

                            fac.AntdDivider(
                                '基于AntdSider的自定义折叠触发',
                                innerTextOrientation='left'
                            ),

                            html.Div(
                                [
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
                                                            style={
                                                                'fontSize': '14px'
                                                            }
                                                        ),
                                                        shape='circle',
                                                        type='text',
                                                        style={
                                                            'position': 'absolute',
                                                            'zIndex': 1,
                                                            'top': 25,
                                                            'right': -13,
                                                            'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 10px 0px',
                                                            'background': 'white'
                                                        }
                                                    ),

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
                                                                'antd-history'
                                                            ]
                                                        ],
                                                        mode='inline',
                                                        style={
                                                            'height': '100%',
                                                            'overflow': 'hidden auto'
                                                        }
                                                    )
                                                ],
                                                id='menu-collapse-sider-custom-demo',
                                                collapsible=True,
                                                collapsedWidth=60,
                                                trigger=None,
                                                style={
                                                    'position': 'relative'
                                                }
                                            ),

                                            fac.AntdContent(
                                                style={
                                                    'background': '#f8f9fa'
                                                }
                                            )
                                        ],
                                        style={
                                            'height': '600px'
                                        }
                                    )
                                ],
                                style={
                                    'height': '600px',
                                    'border': '1px solid rgb(241, 241, 241)'
                                }
                            ),

                            fac.AntdDivider(
                                '配合AntdSider的折叠功能',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString="""
fac.AntdDivider(
    '基于AntdSider自带折叠功能',
    innerTextOrientation='left'
),

# 侧边栏自带折叠触发区域默认会紧贴页面下边界
# 这里为方便局部展示示例，基于fuc.FefferyStyle强制覆盖默认样式
fuc.FefferyStyle(
    rawStyle='''
.sider-demo .ant-layout-sider-trigger {
  position: absolute !important;
}
'''
),

html.Div(
    [
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
                                        'icon': icon
                                    }
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
                                    'antd-history'
                                ]
                            ],
                            mode='inline',
                            style={
                                'height': '100%',
                                'overflow': 'hidden auto'
                            }
                        )
                    ],
                    collapsible=True,
                    collapsedWidth=60
                ),

                fac.AntdContent(
                    style={
                        'background': '#f8f9fa'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    className='sider-demo',
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
),

fac.AntdDivider(
    '基于AntdSider的自定义折叠触发',
    innerTextOrientation='left'
),

html.Div(
    [
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
                                style={
                                    'fontSize': '14px'
                                }
                            ),
                            shape='circle',
                            type='text',
                            style={
                                'position': 'absolute',
                                'zIndex': 1,
                                'top': 25,
                                'right': -13,
                                'boxShadow': 'rgb(0 0 0 / 10%) 0px 4px 10px 0px',
                                'background': 'white'
                            }
                        ),

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
                                    'antd-history'
                                ]
                            ],
                            mode='inline',
                            style={
                                'height': '100%',
                                'overflow': 'hidden auto'
                            }
                        )
                    ],
                    id='menu-collapse-sider-custom-demo',
                    collapsible=True,
                    collapsedWidth=60,
                    trigger=None,
                    style={
                        'position': 'relative'
                    }
                ),

                fac.AntdContent(
                    style={
                        'background': '#f8f9fa'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
    }
)

...

app.clientside_callback(
    '''(nClicks, collapsed) => {
        return [!collapsed, collapsed ? 'antd-arrow-left' : 'antd-arrow-right'];
    }''',
    [Output('menu-collapse-sider-custom-demo', 'collapsed'),
     Output('menu-collapse-sider-custom-demo-trigger-icon', 'icon')],
    Input('menu-collapse-sider-custom-demo-trigger', 'nClicks'),
    State('menu-collapse-sider-custom-demo', 'collapsed'),
    prevent_initial_call=True
)
"""
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='配合AntdSider的折叠功能',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdMenu(
                                id='menu-demo',
                                currentKey='1-1-1',
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

                            html.Div(
                                id='menu-demo-output',
                                style={
                                    'height': '200px',
                                    'background': '#a5d8ff',
                                    'color': 'white',
                                    'fontSize': '24px',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),

                            fac.AntdDivider(
                                '回调示例',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdMenu(
    id='menu-demo',
    currentKey='1-1-1',
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

html.Div(
    id='menu-demo-output',
    style={
        'height': '200px',
        'background': '#a5d8ff',
        'color': 'white',
        'fontSize': '24px',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    }
)

...

@app.callback(
    Output('menu-demo-output', 'children'),
    Input('menu-demo', 'currentKey')
)
def menu_callback_demo(currentKey):

    return f'currentKey: {currentKey}'
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
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
                ],
                style={
                    'flex': 'auto',
                    'padding': '25px'
                }
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': '基础使用', 'href': '#基础使用'},
                        {'title': '不同的显示模式', 'href': '#不同的显示模式'},
                        {'title': '切换色彩风格', 'href': '#切换色彩风格'},
                        {'title': '设置默认展开项', 'href': '#设置默认展开项'},
                        {'title': '设置默认选中项', 'href': '#设置默认选中项'},
                        {'title': '设置菜单项前缀图标', 'href': '#设置菜单项前缀图标'},
                        {'title': '链接跳转功能', 'href': '#链接跳转功能'},
                        {'title': '使用自带的折叠功能', 'href': '#使用自带的折叠功能'},
                        {'title': '配合AntdSider的折叠功能', 'href': '#配合AntdSider的折叠功能'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ],
                    offsetTop=0
                ),
                style={
                    'flex': 'none',
                    'padding': '25px'
                }
            ),
            # 侧边参数栏
            render_side_props_layout(
                component_name='AntdMenu',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
