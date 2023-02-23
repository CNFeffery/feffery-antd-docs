from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdComment
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
                            'title': '数据展示'
                        },
                        {
                            'title': 'AntdComment 评论'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在各种场景下作为功能逻辑的触发点。')
                    ]
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
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀'
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
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀'
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
                        fac.AntdComment(
                            authorName='费弗里',
                            authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
                            publishTime={
                                'value': '2022-01-01 19:29:01',
                                'format': 'YYYY-MM-DD hh:mm:ss'
                            },
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
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
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
    avatarProps={
        'mode': 'image',
        'src': '/assets/imgs/avatar-demo.jpg'
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
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
                            avatarProps={
                                'mode': 'image',
                                'src': '/assets/imgs/avatar-demo.jpg'
                            },
                            fromNow=True
                        ),

                        fac.AntdDivider(
                            '展示相对发表时间',
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
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
    avatarProps={
        'mode': 'image',
        'src': '/assets/imgs/avatar-demo.jpg'
    },
    fromNow=True
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
                    id='展示相对发表时间',
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
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
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

                        fac.AntdParagraph(
                            [
                                '评论本身可以作为其他评论的子元素。从而实现嵌套评论楼中楼效果'
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
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
    avatarProps={
        'mode': 'image',
        'src': '/assets/imgs/avatar-demo.jpg'
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
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
                            defaultAction='liked',
                            likesCount=1
                        ),

                        fac.AntdDivider(
                            '设置初始化点赞及反对状态',
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
fac.AntdComment(
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
    defaultAction='liked',
    likesCount=1
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
                    id='设置初始化点赞及反对状态',
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
                            commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
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
                                    showCount=True,
                                    style={
                                        'width': '100%'
                                    }
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
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdComment(
    id='comment-demo',
    authorName='费弗里',
    authorNameHref='https://github.com/CNFeffery/feffery-antd-components',
    publishTime={
        'value': '2022-01-01 19:29:01',
        'format': 'YYYY-MM-DD hh:mm:ss'
    },
    commentContent='我希望feffery-components项目系列组件可以帮助更多人快速开发心仪的应用！😀',
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
            showCount=True,
            style={
                'width': '100%'
            }
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
    [Output('comment-demo', 'children'),
     Output('comment-demo-input', 'value')],
    [Input('comment-demo-submit', 'nClicks'),
     Input({'type': 'comment-demo-children', 'index': ALL}, 'deleteClicks')],
    [State('comment-demo-input', 'value'),
     State('comment-demo', 'children')],
    prevent_initial_call=True
)
def comment_demo_add_children_callback(nClicks, deleteClicks, value, children):
    # 本次回调由子回复删除功能触发
    if 'deleteClicks' in dash.callback_context.triggered[0]['prop_id']:
        triggerIndex = eval(dash.callback_context.triggered[0]['prop_id'].replace(
            '.deleteClicks', ''))['index']

        return [
            child for child in children if child['props']['id']['index'] != triggerIndex
        ], dash.no_update

    if value:
        return children + [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4())
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value,
                showReply=False,
                showDelete=True
            )
        ] if children else [
            fac.AntdComment(
                id={
                    'type': 'comment-demo-children',
                    'index': str(uuid.uuid4())
                },
                authorName='dash学习者',
                publishTime={
                    'value': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'format': 'YYYY-MM-DD hh:mm:ss'
                },
                commentContent=value,
                showReply=False,
                showDelete=True
            )
        ], None

    else:
        return children, None
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
                    {'title': '自定义头像', 'href': '#自定义头像'},
                    {'title': '展示相对发表时间', 'href': '#自定义头像'},
                    {'title': '嵌套评论', 'href': '#嵌套评论'},
                    {'title': '设置初始化点赞及反对状态', 'href': '#设置初始化点赞及反对状态'},
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
            component_name='AntdComment'
        )
    ],
    style={
        'display': 'flex'
    }
)
