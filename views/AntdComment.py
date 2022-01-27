from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdComment

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdComment(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdComment.md', encoding='utf-8').read()
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
                        fac.AntdComment(
                            authorName='费弗里',
                            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
                            publishTime={
                                'value': '2022-01-01 19:29:01',
                                'format': 'YYYY-MM-DD hh:mm:ss'
                            },
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀'
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
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀'
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
                        fac.AntdComment(
                            authorName='费弗里',
                            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
                            publishTime={
                                'value': '2022-01-01 19:29:01',
                                'format': 'YYYY-MM-DD hh:mm:ss'
                            },
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
                            avatarProps={
                                'mode': 'image',
                                'src': '/assets/imgs/avatar-demo.jpg'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义头像',
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
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
    avatarProps={
        'mode': 'image',
        'src': '/assets/imgs/avatar-demo.jpg'
    }
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
                    id='自定义头像',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdComment(
                            authorName='费弗里',
                            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
                            publishTime={
                                'value': '2022-01-01 19:29:01',
                                'format': 'YYYY-MM-DD hh:mm:ss'
                            },
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
                            avatarProps={
                                'mode': 'image',
                                'src': '/assets/imgs/avatar-demo.jpg'
                            },
                            fromNow=True
                        ),

                        fac.AntdDivider(
                            '相对发表时间模式',
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
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
    avatarProps={
        'mode': 'image',
        'src': '/assets/imgs/avatar-demo.jpg'
    },
    fromNow=True
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
                    id='相对发表时间模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdComment(
                            [
                                fac.AntdComment(
                                    authorName='dash爱好者',
                                    publishTime={
                                        'value': '2022-01-01 19:34:19',
                                        'format': 'YYYY-MM-DD hh:mm:ss'
                                    },
                                    commentContent='资瓷一个！😊'
                                ),
                                fac.AntdComment(
                                    authorName='dash-player',
                                    publishTime={
                                        'value': '2022-01-01 19:40:29',
                                        'format': 'YYYY-MM-DD hh:mm:ss'
                                    },
                                    commentContent='我要好好学习dash和fac，争取早日开发出自己的个人博客网站！'
                                )
                            ],
                            authorName='费弗里',
                            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
                            publishTime={
                                'value': '2022-01-01 19:29:01',
                                'format': 'YYYY-MM-DD hh:mm:ss'
                            },
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
                            avatarProps={
                                'mode': 'image',
                                'src': '/assets/imgs/avatar-demo.jpg'
                            }
                        ),

                        fac.AntdDivider(
                            '嵌套评论',
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
fac.AntdComment(
    [
        fac.AntdComment(
            authorName='dash爱好者',
            publishTime={
                'value': '2022-01-01 19:34:19',
                'format': 'YYYY-MM-DD hh:mm:ss'
            },
            commentContent='资瓷一个！😊'
        ),
        fac.AntdComment(
            authorName='dash-player',
            publishTime={
                'value': '2022-01-01 19:40:29',
                'format': 'YYYY-MM-DD hh:mm:ss'
            },
            commentContent='我要好好学习dash和fac，争取早日开发出自己的个人博客网站！'
        )
    ],
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
    avatarProps={
        'mode': 'image',
        'src': '/assets/imgs/avatar-demo.jpg'
    }
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
                    id='嵌套评论',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdComment(
                            authorName='费弗里',
                            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
                            publishTime={
                                'value': '2022-01-01 19:29:01',
                                'format': 'YYYY-MM-DD hh:mm:ss'
                            },
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
                            defaultAction='liked',
                            likesCount=1
                        ),

                        fac.AntdDivider(
                            '预设点赞/反对状态',
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
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
    defaultAction='liked',
    likesCount=1
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
                    id='预设点赞/反对状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdComment(
                            id='comment-demo',
                            authorName='费弗里',
                            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
                            publishTime={
                                'value': '2022-01-01 19:29:01',
                                'format': 'YYYY-MM-DD hh:mm:ss'
                            },
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
                            defaultAction='liked',
                            likesCount=1
                        ),

                        fac.AntdSpace(
                            [
                                fac.AntdInput(
                                    id='comment-demo-input',
                                    placeholder='发表你的感想...',
                                    mode='text-area',
                                    maxLength=140,
                                    allowClear=True,
                                    showCount=True
                                ),

                                fac.AntdButton(
                                    '提交评论',
                                    id='comment-demo-submit',
                                    type='primary',
                                    style={
                                        'float': 'right'
                                    }
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '回调示例',
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
fac.AntdComment(
    id='comment-demo',
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的网站应用！😀',
    defaultAction='liked',
    likesCount=1
),

fac.AntdSpace(
    [
        fac.AntdInput(
            id='comment-demo-input',
            placeholder='发表你的感想...',
            mode='text-area',
            maxLength=140,
            allowClear=True,
            showCount=True
        ),

        fac.AntdButton(
            '提交评论',
            id='comment-demo-submit',
            type='primary',
            style={
                'float': 'right'
            }
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)
...
@app.callback(
    Output('comment-demo', 'children'),
    Input('comment-demo-submit', 'nClicks'),
    [State('comment-demo-input', 'value'),
     State('comment-demo', 'children')],
    prevent_initial_call=True
)
def comment_demo_add_children_callback(nClicks, value, children):
    if value:
        return children + [
            fac.AntdComment(
                authorName=request.remote_addr,
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value
            )
        ] if children else [
            fac.AntdComment(
                authorName=request.remote_addr,
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value
            )
        ]

    else:
        return children
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
                    id='回调示例',
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
                            {'title': '自定义头像', 'href': '#自定义头像'},
                            {'title': '相对发表时间模式', 'href': '#相对发表时间模式'},
                            {'title': '嵌套评论', 'href': '#嵌套评论'},
                            {'title': '预设点赞/反对状态', 'href': '#预设点赞/反对状态'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
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
