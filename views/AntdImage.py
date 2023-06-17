from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

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
                                'title': 'AntdImage 图片'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于展示单张或一组图片。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdImage(
                                src='/assets/imgs/流浪地球2海报.jpg',
                                height=400
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
fac.AntdImage(
    src='/assets/imgs/流浪地球2海报.jpg',
    height=400
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
                            fac.AntdImage(
                                src='/assets/imgs/流浪地球2海报.jpg',
                                height=400,
                                preview=False
                            ),

                            fac.AntdDivider(
                                '静态模式',
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
fac.AntdImage(
    src='/assets/imgs/流浪地球2海报.jpg',
    height=400,
    preview=False
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
                        id='静态模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'multiImageMode="fold"（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdImage(
                                src=[
                                    '/assets/imgs/image示例1.png',
                                    '/assets/imgs/image示例2.png',
                                    '/assets/imgs/image示例3.png',
                                    '/assets/imgs/image示例4.png',
                                    '/assets/imgs/image示例5.png',
                                    '/assets/imgs/image示例6.png',
                                    '/assets/imgs/image示例7.png',
                                ],
                                height=80
                            ),

                            fac.AntdDivider(
                                'multiImageMode="unfold"（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdImage(
                                src=[
                                    '/assets/imgs/image示例1.png',
                                    '/assets/imgs/image示例2.png',
                                    '/assets/imgs/image示例3.png',
                                    '/assets/imgs/image示例4.png',
                                    '/assets/imgs/image示例5.png',
                                    '/assets/imgs/image示例6.png',
                                    '/assets/imgs/image示例7.png'
                                ],
                                multiImageMode='unfold',
                                height=80
                            ),

                            fac.AntdDivider(
                                '展示一组图片',
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
    'multiImageMode="fold"（默认）',
    innerTextOrientation='left'
),
fac.AntdImage(
    src=[
        '/assets/imgs/image示例1.png',
        '/assets/imgs/image示例2.png',
        '/assets/imgs/image示例3.png',
        '/assets/imgs/image示例4.png',
        '/assets/imgs/image示例5.png',
        '/assets/imgs/image示例6.png',
        '/assets/imgs/image示例7.png',
    ],
    height=80
),

fac.AntdDivider(
    'multiImageMode="unfold"（默认）',
    innerTextOrientation='left'
),
fac.AntdImage(
    src=[
        '/assets/imgs/image示例1.png',
        '/assets/imgs/image示例2.png',
        '/assets/imgs/image示例3.png',
        '/assets/imgs/image示例4.png',
        '/assets/imgs/image示例5.png',
        '/assets/imgs/image示例6.png',
        '/assets/imgs/image示例7.png'
    ],
    multiImageMode='unfold',
    height=80
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
                        id='展示一组图片',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '默认占位图',
                                innerTextOrientation='left'
                            ),
                            fac.AntdImage(
                                src='/assets/imgs/不存在图片示例.jpg',
                                preview=False,
                                height=100
                            ),

                            fac.AntdDivider(
                                '自定义占位图',
                                innerTextOrientation='left'
                            ),
                            fac.AntdImage(
                                src='/assets/imgs/不存在图片示例.jpg',
                                fallback='/assets/imgs/image回滚占位图示例1.png',
                                preview=False,
                                height=100
                            ),

                            fac.AntdDivider(
                                '加载失败占位图',
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
    '默认占位图',
    innerTextOrientation='left'
),
fac.AntdImage(
    src='/assets/imgs/不存在图片示例.jpg',
    preview=False,
    height=100
),

fac.AntdDivider(
    '自定义占位图',
    innerTextOrientation='left'
),
fac.AntdImage(
    src='/assets/imgs/不存在图片示例.jpg',
    fallback='/assets/imgs/image回滚占位图示例1.png',
    preview=False,
    height=100
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
                        id='加载失败占位图',
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
                        {'title': '静态模式', 'href': '#静态模式'},
                        {'title': '展示一组图片', 'href': '#展示一组图片'},
                        {'title': '加载失败占位图', 'href': '#加载失败占位图'},
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
                component_name='AntdImage',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
