from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdAnchor(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdAnchor.md', encoding='utf-8').read()
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

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdAnchor(
                                    linkDict=[
                                        {'title': '示例2-1', 'href': '#示例2-1'},
                                        {'title': '示例2-1-1', 'href': '#示例2-1-1'},
                                        {'title': '示例2-1-2', 'href': '#示例2-1-2'},
                                        {'title': '示例2-2', 'href': '#示例2-2'},
                                    ],
                                    align='right',
                                    containerId='anchor-container-demo',
                                    targetOffset=100
                                ),
                                html.Div(
                                    [
                                        html.H5('示例2-1', id='示例2-1', style={'marginBottom': '800px'}),
                                        html.H5('示例2-1-1', id='示例2-1-1', style={'marginBottom': '800px'}),
                                        html.H5('示例2-1-2', id='示例2-1-2', style={'marginBottom': '800px'}),
                                        html.H5('示例2-2', id='示例2-2', style={'marginBottom': '800px'}),
                                    ]
                                )
                            ],
                            id='anchor-container-demo',
                            style={
                                'maxHeight': '500px',
                                'overflowY': 'auto',
                                'position': 'relative',
                                'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                                'padding': '20px'
                            }
                        ),

                        fac.AntdDivider(
                            '锚点示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fac.AntdAnchor(
            linkDict=[
                {'title': '示例2-1', 'href': '#示例2-1'},
                {'title': '示例2-1-1', 'href': '#示例2-1-1'},
                {'title': '示例2-1-2', 'href': '#示例2-1-2'},
                {'title': '示例2-2', 'href': '#示例2-2'},
            ],
            align='right',
            containerId='anchor-container-demo',
            targetOffset=100
        ),
        html.Div(
            [
                html.H5('示例2-1', id='示例2-1', style={'marginBottom': '800px'}),
                html.H5('示例2-1-1', id='示例2-1-1', style={'marginBottom': '800px'}),
                html.H5('示例2-1-2', id='示例2-1-2', style={'marginBottom': '800px'}),
                html.H5('示例2-2', id='示例2-2', style={'marginBottom': '800px'}),
            ]
        )
    ],
    id='anchor-container-demo',
    style={
        'maxHeight': '500px',
        'overflowY': 'auto',
        'position': 'relative',
        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
        'padding': '20px'
    }
)'''
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
                    id='锚点示例',
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
                            {'title': '锚点示例', 'href': '#锚点示例'}
                        ]
                    },
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
