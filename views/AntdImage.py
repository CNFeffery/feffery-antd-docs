from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdImage(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdImage.md', encoding='utf-8').read()
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
                        fac.AntdImage(
                            src='assets/imgs/fac-logo.svg'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdImage(
    src='assets/imgs/fac-logo.svg'
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
                        fac.AntdDivider('multiImageMode="fold"（默认）', innerTextOrientation='left'),
                        fac.AntdImage(
                            src=[
                                'assets/imgs/fac-logo.svg',
                                'assets/imgs/山海情.webp',
                                'assets/imgs/antd-logo.svg',
                                'assets/imgs/react-logo.svg',
                            ],
                            height=200
                        ),
                        fac.AntdDivider('multiImageMode="unfold"', innerTextOrientation='left'),
                        fac.AntdImage(
                            src=[
                                'assets/imgs/fac-logo.svg',
                                'assets/imgs/山海情.webp',
                                'assets/imgs/antd-logo.svg',
                                'assets/imgs/react-logo.svg',
                            ],
                            multiImageMode='unfold',
                            height=200
                        ),

                        fac.AntdDivider(
                            '多图模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider('multiImageMode="fold"（默认）', innerTextOrientation='left'),
fac.AntdImage(
    src=[
        'assets/imgs/fac-logo.svg',
        'assets/imgs/山海情.webp',
        'assets/imgs/antd-logo.svg',
        'assets/imgs/react-logo.svg',
    ],
    height=200
),
fac.AntdDivider('multiImageMode="unfold"', innerTextOrientation='left'),
fac.AntdImage(
    src=[
        'assets/imgs/fac-logo.svg',
        'assets/imgs/山海情.webp',
        'assets/imgs/antd-logo.svg',
        'assets/imgs/react-logo.svg',
    ],
    multiImageMode='unfold',
    height=200
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
                    id='多图模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        # 传入无效的图片地址
                        fac.AntdImage(
                            src='assets/imgs/fac-logo_.svg'
                        ),

                        fac.AntdDivider(
                            '加载失败时的占位图',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
# 传入无效的图片地址
fac.AntdImage(
    src='assets/imgs/fac-logo_.svg'
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
                    id='加载失败时的占位图',
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
                            {'title': '多图模式', 'href': '#多图模式'},
                            {'title': '加载失败时的占位图', 'href': '#加载失败时的占位图'},
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
