from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdPageHeader
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
                            'title': '导航'
                        },
                        {
                            'title': 'AntdPageHeader 页头'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　页头位于页容器顶部，起到内容概览和引导页级操作的作用。')
                    ]
                ),

                html.Div(
                    [

                        fac.AntdPageHeader(
                            title='页头标题示例',
                            subTitle='页头副标题示例'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '　　最基础的页头包含了自带浏览器后退功能的返回按钮、主标题及副标题信息'
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPageHeader(
    title='页头标题示例',
    subTitle='页头副标题示例'
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
                        fac.AntdPageHeader(
                            fac.AntdSpace(
                                [
                                    fac.AntdButton('按钮1'),
                                    fac.AntdButton('按钮2', type='primary'),
                                    fac.AntdSwitch(
                                        checkedChildren='打开',
                                        unCheckedChildren='关闭'
                                    ),
                                    fac.AntdBadge(status='processing')
                                ]
                            ),
                            title='页头标题示例',
                            subTitle='页头副标题示例'
                        ),

                        fac.AntdDivider(
                            '传入子元素',
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
fac.AntdPageHeader(
    fac.AntdSpace(
        [
            fac.AntdButton('按钮1'),
            fac.AntdButton('按钮2', type='primary'),
            fac.AntdSwitch(
                checkedChildren='打开',
                unCheckedChildren='关闭'
            ),
            fac.AntdBadge(status='processing')
        ]
    ),
    title='页头标题示例',
    subTitle='页头副标题示例'
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
                    id='传入子元素',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPageHeader(
                            id='page-header-demo',
                            title='页头标题示例',
                            subTitle='页头副标题示例',
                            historyBackDisabled=True
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '可用于单纯监听返回按钮的点击事件'
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
fac.AntdPageHeader(
    id='page-header-demo',
    title='页头标题示例',
    subTitle='页头副标题示例',
    historyBackDisabled=True
)

...

@app.callback(
    Output('page-header-demo', 'children'),
    Input('page-header-demo', 'backClicks')
)
def page_header_demo_callback(backClicks):
    return [
        fac.AntdText('backClicks: ', strong=True),
        fac.AntdText(backClicks)
    ]
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
                    {'title': '传入子元素', 'href': '#传入子元素'},
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
            component_name='AntdPageHeader'
        )
    ],
    style={
        'display': 'flex'
    }
)
