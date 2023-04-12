from dash import html, dcc
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdBadge
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
                            'title': 'AntdBadge 徽标数'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　一般出现在通知图标或头像的右上角，用于显示需要处理的消息条数，通过醒目视觉形式吸引用户处理。')
                    ]
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
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    count=56,
                                    overflowCount=50
                                ),

                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        shape='square',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    dot=True
                                ),

                                fac.AntdBadge(
                                    fac.AntdIcon(
                                        icon='fc-advertising',
                                        style={
                                            'fontSize': '40px'
                                        }
                                    ),
                                    count=6
                                ),

                                fac.AntdBadge(
                                    fac.AntdIcon(
                                        icon='fc-advertising',
                                        style={
                                            'fontSize': '40px'
                                        }
                                    ),
                                    count=56,
                                    overflowCount=50
                                ),

                                fac.AntdBadge(
                                    fac.AntdIcon(
                                        icon='fc-advertising',
                                        style={
                                            'fontSize': '40px'
                                        }
                                    ),
                                    dot=True
                                ),

                                fac.AntdBadge(
                                    fac.AntdIcon(
                                        icon='fc-advertising',
                                        style={
                                            'fontSize': '40px'
                                        }
                                    ),
                                    dot=True,
                                    offset=[-8, 6]
                                )
                            ],
                            size=20
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　徽标最常见的用法是为其'),
                                fac.AntdText('children', code=True),
                                fac.AntdText('添加角标形式的徽标数，主要用于'),
                                fac.AntdText('AntdIcon', code=True),
                                fac.AntdText('、'),
                                fac.AntdText('AntdAvatar', code=True),
                                fac.AntdText('等组件')
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
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
                src='/assets/imgs/avatar-demo.jpg'
            ),
            count=56,
            overflowCount=50
        ),

        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                shape='square',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            dot=True
        ),

        fac.AntdBadge(
            fac.AntdIcon(
                icon='fc-advertising',
                style={
                    'fontSize': '40px'
                }
            ),
            count=6
        ),

        fac.AntdBadge(
            fac.AntdIcon(
                icon='fc-advertising',
                style={
                    'fontSize': '40px'
                }
            ),
            count=56,
            overflowCount=50
        ),

        fac.AntdBadge(
            fac.AntdIcon(
                icon='fc-advertising',
                style={
                    'fontSize': '40px'
                }
            ),
            dot=True
        ),

        fac.AntdBadge(
            fac.AntdIcon(
                icon='fc-advertising',
                style={
                    'fontSize': '40px'
                }
            ),
            dot=True,
            offset=[-8, 6]
        )
    ],
    size=20
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
                            'size="default"（默认）',
                            innerTextOrientation='left'
                        ),
                        fac.AntdSpace(
                            [
                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    count=6,
                                    color='yellow'
                                ),

                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    count=56,
                                    overflowCount=50,
                                    color='orange'
                                ),

                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        shape='square',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    dot=True,
                                    color='cyan'
                                )
                            ],
                            size=20
                        ),

                        fac.AntdDivider(
                            'size="small"',
                            innerTextOrientation='left'
                        ),
                        fac.AntdSpace(
                            [
                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    count=6,
                                    color='yellow',
                                    size='small'
                                ),

                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    count=56,
                                    overflowCount=50,
                                    color='orange',
                                    size='small'
                                ),

                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        shape='square',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    dot=True,
                                    color='cyan',
                                    size='small'
                                )
                            ],
                            size=20
                        ),

                        fac.AntdDivider(
                            '不同尺寸及颜色',
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
    'size="default"（默认）',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            count=6,
            color='yellow'
        ),

        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            count=56,
            overflowCount=50,
            color='orange'
        ),

        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                shape='square',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            dot=True,
            color='cyan'
        )
    ],
    size=20
),

fac.AntdDivider(
    'size="small"',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            count=6,
            color='yellow',
            size='small'
        ),

        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            count=56,
            overflowCount=50,
            color='orange',
            size='small'
        ),

        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                shape='square',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            dot=True,
            color='cyan',
            size='small'
        )
    ],
    size=20
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
                    id='不同尺寸及颜色',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdBadge(count=8),
                                fac.AntdBadge(count=101),
                                fac.AntdBadge(count=101, size='small'),
                                fac.AntdBadge(dot=True, status='success'),
                                fac.AntdBadge(dot=True, status='error'),
                                fac.AntdBadge(dot=True, status='default'),
                                fac.AntdBadge(dot=True, status='processing'),
                                fac.AntdBadge(dot=True, status='warning'),
                            ],
                            size=20
                        ),

                        fac.AntdDivider(
                            '独立使用徽标',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　当'),
                                fac.AntdText('AntdBadge', strong=True),
                                fac.AntdText('不传入'),
                                fac.AntdText('children', code=True),
                                fac.AntdText('参数时，可独立使用，'),
                                fac.AntdText('其中', strong=True),
                                fac.AntdText('status="processing"', code=True),
                                fac.AntdText('仅徽标独立使用时可用，否则会出现显示异常')
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdBadge(count=8),
        fac.AntdBadge(count=101),
        fac.AntdBadge(count=101, size='small'),
        fac.AntdBadge(dot=True, status='success'),
        fac.AntdBadge(dot=True, status='error'),
        fac.AntdBadge(dot=True, status='default'),
        fac.AntdBadge(dot=True, status='processing'),
        fac.AntdBadge(dot=True, status='warning'),
    ],
    size=20
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
                    id='独立使用徽标',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '计数随机递增',
                                    id='badge-demo-generate',
                                    type='primary'
                                ),
                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    id='badge-demo-1',
                                    count=6
                                ),
                                fac.AntdBadge(
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    ),
                                    id='badge-demo-2',
                                    count=0,
                                    dot=True
                                )
                            ],
                            size=20
                        ),

                        fac.AntdDivider(
                            '动态数值变化',
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
fac.AntdSpace(
    [
        fac.AntdButton(
            '计数随机递增',
            id='badge-demo-generate',
            type='primary'
        ),
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            id='badge-demo-1',
            count=6
        ),
        fac.AntdBadge(
            fac.AntdAvatar(
                mode='image',
                src='/assets/imgs/avatar-demo.jpg'
            ),
            id='badge-demo-2',
            count=0,
            dot=True
        )
    ],
    size=20
)

...

import random

...

@app.callback(
    [Output('badge-demo-1', 'count'),
     Output('badge-demo-2', 'count')],
    Input('badge-demo-generate', 'nClicks'),
    [State('badge-demo-1', 'count'),
     State('badge-demo-2', 'count')],
    prevent_initial_call=True
)
def badge_callback_demo(nClicks, count1, count2):
    return count1 + random.randint(1, 10), count2 + random.randint(1, 10)
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
                    id='动态数值变化',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdAlert(
                            type='info',
                            showIcon=True,
                            message='请你在点击【创建新一局游戏】后，以最快的速度对下方具有红点徽标的3个头像进行点击，全部耗时（单位：秒）即为你的成绩！',
                            messageRenderMode='marquee',
                            style={
                                'marginBottom': '5px'
                            }
                        ),
                        fac.AntdButton(
                            '创建新一局游戏',
                            id='badge-click-demo-reset',
                            type='primary'
                        ),
                        fac.AntdDivider(),
                        dcc.Store(id='badge-click-demo-start-time'),
                        html.Div(
                            id='badges-area',
                            style={
                                'display': 'flex',
                                'justifyContent': 'center'
                            }
                        ),
                        html.Div(
                            id='badge-click-demo-score',
                            style={
                                'display': 'flex',
                                'justifyContent': 'center'
                            }
                        ),

                        fac.AntdDivider(
                            '基于点击事件实现更多功能',
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
fac.AntdAlert(
    type='info',
    showIcon=True,
    message='请你在点击【创建新一局游戏】后，以最快的速度对下方具有红点徽标的3个头像进行点击，全部耗时（单位：秒）即为你的成绩！',
    messageRenderMode='marquee',
    style={
        'marginBottom': '5px'
    }
),
fac.AntdButton(
    '创建新一局游戏',
    id='badge-click-demo-reset',
    type='primary'
),
fac.AntdDivider(),
dcc.Store(id='badge-click-demo-start-time'),
html.Div(
    id='badges-area',
    style={
        'display': 'flex',
        'justifyContent': 'center'
    }
),
html.Div(
    id='badge-click-demo-score',
    style={
        'display': 'flex',
        'justifyContent': 'center'
    }
)

...

@app.callback(
    [Output('badges-area', 'children'),
     Output('badge-click-demo-start-time', 'data')],
    Input('badge-click-demo-reset', 'nClicks'),
    prevent_initial_call=True
)
def badge_click_demo_callback1(nClicks):
    badges_count = [1] * 3 + [0] * 7
    random.shuffle(badges_count)

    return [
        [
            fac.AntdBadge(
                fac.AntdAvatar(
                    mode='image',
                    src='/assets/imgs/avatar-demo.jpg',
                    style={
                        'cursor': 'pointer'
                    }
                ),
                id={
                    'type': 'badge-click-demo',
                    'index': idx
                },
                count=c,
                dot=True,
                style={
                    'cursor': 'pointer'
                }
            )
            for idx, c in enumerate(badges_count)
        ],
        {
            'start-time': time.time()
        }
    ]


@app.callback(
    Output({'type': 'badge-click-demo', 'index': MATCH}, 'count'),
    Input({'type': 'badge-click-demo', 'index': MATCH}, 'nClicks'),
    State({'type': 'badge-click-demo', 'index': MATCH}, 'count'),
    prevent_initial_call=True
)
def badge_click_demo_callback2(nClicks, count_):
    return 0 if count_ != 0 else dash.no_update


@app.callback(
    Output('badge-click-demo-score', 'children'),
    Input({'type': 'badge-click-demo', 'index': ALL}, 'count'),
    State('badge-click-demo-start-time', 'data'),
    prevent_initial_call=True
)
def badge_click_demo_callback3(counts, start_time):
    if sum(counts) == 0:
        return fac.AntdParagraph(
            [
                fac.AntdText('你的得分：', strong=True),
                fac.AntdText('%s秒' % round(
                    time.time() - start_time['start-time'], 3))
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
                    id='基于点击事件实现更多功能',
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
                    {'title': '不同尺寸及颜色', 'href': '#不同尺寸及颜色'},
                    {'title': '独立使用徽标', 'href': '#独立使用徽标'},
                    {'title': '动态数值变化', 'href': '#动态数值变化'},
                    {'title': '基于点击事件实现更多功能', 'href': '#基于点击事件实现更多功能'},
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
            component_name='AntdBadge'
        )
    ],
    style={
        'display': 'flex'
    }
)
