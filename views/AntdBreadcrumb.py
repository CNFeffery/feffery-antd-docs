from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from .side_props import render_side_props_layout

docs_content = html.Div(
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
                            'title': 'AntdBreadcrumb 面包屑'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于展示当前页面在系统层级结构中的位置。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdBreadcrumb(
                            items=[
                                {
                                    'title': '首页'
                                },
                                {
                                    'title': '下属页面1'
                                },
                                {
                                    'title': '下属页面1-1'
                                }
                            ]
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
fac.AntdBreadcrumb(
    items=[
        {
            'title': '首页'
        },
        {
            'title': '下属页面1'
        },
        {
            'title': '下属页面1-1'
        }
    ]
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
                        fac.AntdBreadcrumb(
                            items=[
                                {
                                    'title': 'feffery-components仓库主页',
                                    'href': 'https://github.com/CNFeffery/feffery-dash-components',
                                    'target': '_blank'
                                },
                                {
                                    'title': 'feffery-antd-components文档首页',
                                    'href': '/',
                                    'target': '_blank'
                                },
                                {
                                    'title': 'AntdBreadcrumb文档页',
                                    'href': '/AntdBreadcrumb',
                                    'target': '_blank'
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '添加链接跳转功能',
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
fac.AntdBreadcrumb(
    items=[
        {
            'title': 'feffery-components仓库主页',
            'href': 'https://github.com/CNFeffery/feffery-dash-components',
            'target': '_blank'
        },
        {
            'title': 'feffery-antd-components文档首页',
            'href': '/',
            'target': '_blank'
        },
        {
            'title': 'AntdBreadcrumb文档页',
            'href': '/AntdBreadcrumb',
            'target': '_blank'
        }
    ]
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
                    id='添加链接跳转功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdBreadcrumb(
                            items=[
                                {
                                    'title': 'feffery-components仓库主页',
                                    'href': 'https://github.com/CNFeffery/feffery-dash-components',
                                    'target': '_blank',
                                    'icon': 'antd-github'
                                },
                                {
                                    'title': 'feffery-antd-components文档首页',
                                    'href': '/',
                                    'target': '_blank',
                                    'icon': 'antd-home'
                                },
                                {
                                    'title': 'AntdBreadcrumb文档页',
                                    'href': '/AntdBreadcrumb',
                                    'target': '_blank',
                                    'icon': 'fc-approval'
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '添加前缀图标',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '通过参数',
                                fac.AntdText(
                                    'icon',
                                    code=True
                                ),
                                '，可基于图标代号直接使用',
                                fac.AntdText(
                                    'AntdIcon',
                                    strong=True
                                ),
                                '中的各种图标作为节点的前缀图标'
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdBreadcrumb(
    items=[
        {
            'title': 'feffery-components仓库主页',
            'href': 'https://github.com/CNFeffery/feffery-dash-components',
            'target': '_blank',
            'icon': 'antd-github'
        },
        {
            'title': 'feffery-antd-components文档首页',
            'href': '/',
            'target': '_blank',
            'icon': 'antd-home'
        },
        {
            'title': 'AntdBreadcrumb文档页',
            'href': '/AntdBreadcrumb',
            'target': '_blank',
            'icon': 'fc-approval'
        }
    ]
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
                    id='添加前缀图标',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdBreadcrumb(
                            items=[
                                {
                                    'title': 'feffery-components仓库主页',
                                    'href': 'https://github.com/CNFeffery/feffery-dash-components',
                                    'target': '_blank',
                                    'icon': 'antd-github'
                                },
                                {
                                    'title': 'feffery-antd-components文档首页',
                                    'href': '/',
                                    'target': '_blank',
                                    'icon': 'antd-home',
                                    'menuItems': [
                                        {
                                            'title': 'feffery-utils-components',
                                            'href': 'https://github.com/CNFeffery/feffery-utils-components',
                                            'target': '_blank'
                                        },
                                        {
                                            'title': 'feffery-antd-charts',
                                            'href': 'https://github.com/CNFeffery/feffery-antd-charts',
                                            'target': '_blank'
                                        },
                                        {
                                            'title': 'feffery-markdown-components',
                                            'href': 'https://github.com/CNFeffery/feffery-markdown-components',
                                            'target': '_blank'
                                        }
                                    ]
                                },
                                {
                                    'title': 'AntdBreadcrumb文档页',
                                    'href': '/AntdBreadcrumb',
                                    'target': '_blank',
                                    'icon': 'fc-approval'
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '节点添加悬浮菜单',
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
fac.AntdBreadcrumb(
    items=[
        {
            'title': 'feffery-components仓库主页',
            'href': 'https://github.com/CNFeffery/feffery-dash-components',
            'target': '_blank',
            'icon': 'antd-github'
        },
        {
            'title': 'feffery-antd-components文档首页',
            'href': '/',
            'target': '_blank',
            'icon': 'antd-home',
            'menuItems': [
                {
                    'title': 'feffery-utils-components',
                    'href': 'https://github.com/CNFeffery/feffery-utils-components',
                    'target': '_blank'
                },
                {
                    'title': 'feffery-antd-charts',
                    'href': 'https://github.com/CNFeffery/feffery-antd-charts',
                    'target': '_blank'
                },
                {
                    'title': 'feffery-markdown-components',
                    'href': 'https://github.com/CNFeffery/feffery-markdown-components',
                    'target': '_blank'
                }
            ]
        },
        {
            'title': 'AntdBreadcrumb文档页',
            'href': '/AntdBreadcrumb',
            'target': '_blank',
            'icon': 'fc-approval'
        }
    ]
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
                    id='节点添加悬浮菜单',
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
                    {'title': '添加链接跳转功能', 'href': '#添加链接跳转功能'},
                    {'title': '添加前缀图标', 'href': '#添加前缀图标'},
                    {'title': '节点添加悬浮菜单', 'href': '#节点添加悬浮菜单'},
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
            component_name='AntdBreadcrumb'
        )
    ],
    style={
        'display': 'flex'
    }
)
