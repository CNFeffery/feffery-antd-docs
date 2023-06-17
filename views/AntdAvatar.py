import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdAvatar
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
                                'title': '数据展示'
                            },
                            {
                                'title': 'AntdAvatar 头像'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染图标、文字或图片形式的头像。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdAvatar(),
                                    fac.AntdAvatar(
                                        mode='text',
                                        text='F'
                                    ),
                                    fac.AntdAvatar(
                                        mode='image',
                                        src='/assets/imgs/avatar-demo.jpg'
                                    )
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
fac.AntdSpace(
    [
        fac.AntdAvatar(),
        fac.AntdAvatar(
            mode='text',
            text='F'
        ),
        fac.AntdAvatar(
            mode='image',
            src='/assets/imgs/avatar-demo.jpg'
        )
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
                            fac.AntdSpace(
                                [
                                    fuc.FefferyHexColorPicker(
                                        id='avatar-bg-color-input'
                                    ),

                                    fac.AntdSpace(
                                        [
                                            fac.AntdAvatar(
                                                id='avatar-bg-color-icon-demo'
                                            ),
                                            fac.AntdAvatar(
                                                id='avatar-bg-color-text-demo',
                                                mode='text',
                                                text='F'
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '设置背景色',
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
        fuc.FefferyHexColorPicker(
            id='avatar-bg-color-input'
        ),

        fac.AntdSpace(
            [
                fac.AntdAvatar(
                    id='avatar-bg-color-icon-demo'
                ),
                fac.AntdAvatar(
                    id='avatar-bg-color-text-demo',
                    mode='text',
                    text='F'
                ),
            ]
        )
    ],
    style={
        'width': '100%'
    }
)

...

@app.callback(
    [Output('avatar-bg-color-icon-demo', 'style'),
     Output('avatar-bg-color-text-demo', 'style')],
    Input('avatar-bg-color-input', 'color')
)
def avatar_bg_color_demo(color):

    return [
        {
            'background': color
        }
    ] * 2
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
                        id='设置背景色',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdAvatar(
                                        icon=icon,
                                        style={
                                            'background': '#4551f5'
                                        }
                                    )
                                    for icon in [
                                        'antd-user',
                                        'antd-team',
                                        'antd-github',
                                        'antd-fire',
                                        'antd-thunderbolt',
                                        'antd-robot'
                                    ]
                                ],
                                wrap=True
                            ),

                            fac.AntdDivider(
                                '使用AntdIcon中的丰富图标',
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
        fac.AntdAvatar(
            icon=icon,
            style={
                'background': '#4551f5'
            }
        )
        for icon in [
            'antd-user',
            'antd-team',
            'antd-github',
            'antd-fire',
            'antd-thunderbolt',
            'antd-robot'
        ]
    ],
    wrap=True
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
                        id='使用AntdIcon中的丰富图标',
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
                                '搭配徽标使用',
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
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='搭配徽标使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdAvatar(),
                                    fac.AntdAvatar(
                                        size='small'
                                    ),
                                    fac.AntdAvatar(
                                        size='large'
                                    ),
                                    fac.AntdAvatar(
                                        size=64
                                    ),
                                ],
                                align='center'
                            ),

                            fac.AntdDivider(
                                '设置头像大小',
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
        fac.AntdAvatar(),
        fac.AntdAvatar(
            size='small'
        ),
        fac.AntdAvatar(
            size='large'
        ),
        fac.AntdAvatar(
            size=64
        ),
    ],
    align='center'
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
                        id='设置头像大小',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAvatar(
                                mode='image',
                                src='/assets/imgs/avatar-demo.jpg',
                                size={
                                    'xs': 24,
                                    'sm': 28,
                                    'md': 32,
                                    'lg': 36,
                                    'xl': 40,
                                    'xxl': 45
                                }
                            ),

                            fac.AntdDivider(
                                '响应式调整大小',
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
fac.AntdAvatar(
    mode='image',
    src='/assets/imgs/avatar-demo.jpg',
    size={
        'xs': 24,
        'sm': 28,
        'md': 32,
        'lg': 36,
        'xl': 40,
        'xxl': 45
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
                        id='响应式调整大小',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAvatar(
                                mode='image',
                                src='/assets/imgs/avatar-demo.jpg',
                                size='large',
                                shape='square'
                            ),

                            fac.AntdDivider(
                                '方形头像',
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
fac.AntdAvatar(
    mode='image',
    src='/assets/imgs/avatar-demo.jpg',
    size='large',
    shape='square'
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
                        id='方形头像',
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
                        {'title': '设置背景色', 'href': '#设置背景色'},
                        {'title': '使用AntdIcon中的丰富图标', 'href': '#使用AntdIcon中的丰富图标'},
                        {'title': '搭配徽标使用', 'href': '#搭配徽标使用'},
                        {'title': '设置头像大小', 'href': '#设置头像大小'},
                        {'title': '响应式大小', 'href': '#响应式大小'},
                        {'title': '方形头像', 'href': '#方形头像'},
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
                component_name='AntdAvatar',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
