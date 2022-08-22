from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdAvatar(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdAvatar.md', encoding='utf-8').read()
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
                        fac.AntdDivider('mode="icon"（默认）', innerTextOrientation='left'),
                        fac.AntdAvatar(
                            mode='icon',
                            style={
                                'backgroundColor': 'rgb(16, 105, 246)'
                            }
                        ),

                        fac.AntdDivider('mode="text"', innerTextOrientation='left'),
                        fac.AntdAvatar(
                            mode='text',
                            text='费弗里',
                            style={
                                'backgroundColor': 'rgb(16, 105, 246)'
                            }
                        ),

                        fac.AntdDivider('mode="image"', innerTextOrientation='left'),
                        fac.AntdAvatar(
                            mode='image',
                            src='/assets/imgs/avatar-demo.jpg'
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
fac.AntdDivider('mode="icon"（默认）', innerTextOrientation='left'),
fac.AntdAvatar(
    mode='icon',
    style={
        'backgroundColor': 'rgb(16, 105, 246)'
    }
),

fac.AntdDivider('mode="text"', innerTextOrientation='left'),
fac.AntdAvatar(
    mode='text',
    text='费弗里',
    style={
        'backgroundColor': 'rgb(16, 105, 246)'
    }
),

fac.AntdDivider('mode="image"', innerTextOrientation='left'),
fac.AntdAvatar(
    mode='image',
    src='/assets/imgs/avatar-demo.jpg'
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
                        fac.AntdAvatar(
                            mode='icon',
                            size=32,
                            style={
                                'backgroundColor': 'rgb(16, 105, 246)'
                            }
                        ),
                        fac.AntdAvatar(
                            mode='text',
                            size='large',
                            text='费弗里',
                            style={
                                'backgroundColor': 'rgb(16, 105, 246)'
                            }
                        ),
                        fac.AntdAvatar(
                            mode='image',
                            size=48,
                            src='/assets/imgs/avatar-demo.jpg'
                        ),

                        fac.AntdDivider(
                            '不同的尺寸大小',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdAvatar(
    mode='icon',
    size=32,
    style={
        'backgroundColor': 'rgb(16, 105, 246)'
    }
),
fac.AntdAvatar(
    mode='text',
    size='large',
    text='费弗里',
    style={
        'backgroundColor': 'rgb(16, 105, 246)'
    }
),
fac.AntdAvatar(
    mode='image',
    size=48,
    src='/assets/imgs/avatar-demo.jpg'
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
                    id='不同的尺寸大小',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdAvatar(
                            mode='image',
                            src='/assets/imgs/avatar-demo.jpg'
                        ),
                        fac.AntdAvatar(
                            mode='image',
                            shape='square',
                            src='/assets/imgs/avatar-demo.jpg'
                        ),

                        fac.AntdDivider(
                            '不同的形状',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdAvatar(
    mode='image',
    src='/assets/imgs/avatar-demo.jpg'
),
fac.AntdAvatar(
    mode='image',
    shape='square',
    src='/assets/imgs/avatar-demo.jpg'
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
                    id='不同的形状',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    count=6
                                ),
                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        shape='square',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    dot=True
                                )
                            ],
                            size=20
                        ),

                        fac.AntdDivider(
                            '添加徽标',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            count=6
        ),
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                shape='square',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            dot=True
        )
    ],
    size=20
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
                    id='添加徽标',
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
                            {'title': '不同的尺寸大小', 'href': '#不同的尺寸大小'},
                            {'title': '不同的形状', 'href': '#不同的形状'},
                            {'title': '添加徽标', 'href': '#添加徽标'},
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
