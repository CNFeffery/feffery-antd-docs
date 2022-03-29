from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdBreadcrumb(id, className, style, *args, **kwargs)',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5'
                    }
                ),

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
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

                fmc.FefferyMarkdown(
                    markdownStr=open('documents/AntdBreadcrumb.md', encoding='utf-8').read()
                ),

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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
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
                            is_open=False,
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
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
                            is_open=False,
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

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
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
                            is_open=False,
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
                            '添加悬浮菜单',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
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
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='添加悬浮菜单',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdBreadcrumb(
                            separator='->',
                            items=[
                                {
                                    'title': 'feffery-components仓库主页',
                                    'href': 'https://github.com/CNFeffery/feffery-dash-components',
                                    'target': '_blank',
                                    'icon': 'github'
                                },
                                {
                                    'title': 'feffery-antd-components文档首页',
                                    'href': '/',
                                    'target': '_blank',
                                    'icon': 'home'
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
                            '自定义层级分隔符',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdBreadcrumb(
    separator='->',
    items=[
        {
            'title': 'feffery-components仓库主页',
            'href': 'https://github.com/CNFeffery/feffery-dash-components',
            'target': '_blank',
            'icon': 'github'
        },
        {
            'title': 'feffery-antd-components文档首页',
            'href': '/',
            'target': '_blank',
            'icon': 'home'
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
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='自定义层级分隔符',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '主要参数说明', 'href': '#主要参数说明'},
                    {
                        'title': '使用示例',
                        'href': '#使用示例',
                        'children': [
                            {'title': '基础使用', 'href': '#基础使用'},
                            {'title': '添加链接跳转功能', 'href': '#添加链接跳转功能'},
                            {'title': '添加前缀图标', 'href': '#添加前缀图标'},
                            {'title': '添加悬浮菜单', 'href': '#添加悬浮菜单'},
                            {'title': '自定义层级分隔符', 'href': '#自定义层级分隔符'}
                        ]
                    },
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
