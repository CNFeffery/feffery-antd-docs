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
                            'title': '布局'
                        },
                        {
                            'title': 'AntdDivider 分割线'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于对页面功能区进行水平或竖直方向上的分割。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdDivider(),

                        fac.AntdDivider(isDashed=True),

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
fac.AntdDivider(),
fac.AntdDivider(isDashed=True)

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
                        # 默认居中
                        fac.AntdDivider('AntdDivider'),

                        # 左对齐
                        fac.AntdDivider(
                            'AntdDivider',
                            innerTextOrientation='left'
                        ),

                        # 右对齐且设置内嵌文字样式
                        fac.AntdDivider(
                            'AntdDivider',
                            innerTextOrientation='right',
                            fontStyle='oblique'
                        ),

                        fac.AntdDivider(
                            '内嵌文字及显示位置',
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
# 默认居中
fac.AntdDivider('AntdDivider'),

# 左对齐
fac.AntdDivider(
    'AntdDivider',
    innerTextOrientation='left'
),

# 右对齐且设置内嵌文字样式
fac.AntdDivider(
    'AntdDivider',
    innerTextOrientation='right',
    fontStyle='oblique'
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
                    id='内嵌文字及显示位置',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                '项目1',
                                fac.AntdDivider(
                                    direction='vertical'
                                ),
                                '项目2',
                                fac.AntdDivider(
                                    direction='vertical',
                                    lineColor='black'
                                ),
                                '项目3',
                                fac.AntdDivider(
                                    direction='vertical',
                                    lineColor='red'
                                ),
                                '项目4'
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    [
        '项目1',
        fac.AntdDivider(
            direction='vertical'
        ),
        '项目2',
        fac.AntdDivider(
            direction='vertical',
            lineColor='black'
        ),
        '项目3',
        fac.AntdDivider(
            direction='vertical',
            lineColor='red'
        ),
        '项目4'
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
                    id='竖直分割线',
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
                    {'title': '内嵌文字及显示位置', 'href': '#内嵌文字及显示位置'},
                    {'title': '竖直分割线', 'href': '#竖直分割线'},
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
            component_name='AntdDivider'
        )
    ],
    style={
        'display': 'flex'
    }
)
