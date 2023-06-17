from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdPagination
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
                                'title': '导航'
                            },
                            {
                                'title': 'AntdPagination 分页'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　采用分页的形式分隔长列表，每次只加载单页内容。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdPagination(
                                defaultPageSize=10,
                                total=100
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
fac.AntdPagination(
    defaultPageSize=10,
    total=100
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
                                '默认hideOnSinglePage=False',
                                innerTextOrientation='left'
                            ),

                            fac.AntdPagination(
                                total=10,
                                pageSize=20
                            ),

                            fac.AntdDivider(
                                'hideOnSinglePage=True',
                                innerTextOrientation='left'
                            ),

                            fac.AntdPagination(
                                total=10,
                                pageSize=20,
                                hideOnSinglePage=True
                            ),

                            fac.AntdDivider(
                                '仅有1页时自动隐藏分页组件',
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
    '默认hideOnSinglePage=False',
    innerTextOrientation='left'
),

fac.AntdPagination(
    total=10,
    pageSize=20
),

fac.AntdDivider(
    'hideOnSinglePage=True',
    innerTextOrientation='left'
),

fac.AntdPagination(
    total=10,
    pageSize=20,
    hideOnSinglePage=True
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
                        id='仅有1页时自动隐藏分页组件',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdPagination(
                                defaultPageSize=10,
                                total=100,
                                showQuickJumper=True,
                                showSizeChanger=False,
                                showTotalPrefix='总记录数：',
                                showTotalSuffix='条！🧐'
                            ),

                            fac.AntdDivider(
                                '添加更多功能',
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
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    showQuickJumper=True,
    showSizeChanger=False,
    showTotalPrefix='总记录数：',
    showTotalSuffix='条！🧐'
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
                        id='添加更多功能',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdPagination(
                                defaultPageSize=10,
                                total=100,
                                simple=True,
                                showTotal=False
                            ),

                            fac.AntdDivider(
                                '极简模式',
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
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    simple=True,
    showTotal=False
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
                        id='极简模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdPagination(
                                defaultPageSize=10,
                                total=100,
                                size='small'
                            ),

                            fac.AntdDivider(
                                '迷你模式',
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
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    size='small'
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
                        id='迷你模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                id='pagination-demo-output',
                                direction='vertical'
                            ),

                            fac.AntdPagination(
                                id='pagination-demo',
                                defaultPageSize=10,
                                total=100,
                                pageSizeOptions=[5, 10, 20]
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
fac.AntdSpace(
    id='pagination-demo-output',
    direction='vertical'
),

fac.AntdPagination(
    id='pagination-demo',
    defaultPageSize=10,
    total=100,
    pageSizeOptions=[5, 10, 20]
)

...

@app.callback(
    Output('pagination-demo-output', 'children'),
    [Input('pagination-demo', 'current'),
     Input('pagination-demo', 'pageSize')]
)
def pagination_callback_demo(current, pageSize):

    return [
        fac.AntdText(f'内容项{i}')
        for i in range((current - 1) * pageSize, current * pageSize)
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
                        {'title': '仅有1页时自动隐藏分页组件', 'href': '#仅有1页时自动隐藏分页组件'},
                        {'title': '添加更多功能', 'href': '#添加更多功能'},
                        {'title': '极简模式', 'href': '#极简模式'},
                        {'title': '迷你模式', 'href': '#迷你模式'},
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
                component_name='AntdPagination',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
