from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdPagination

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdPagination(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdPagination.md', encoding='utf-8').read()
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
                        fac.AntdPagination(
                            defaultPageSize=10,
                            total=100
                        ),

                        fac.AntdDivider(
                            '基础使用方式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPagination(
    defaultPageSize=10,
    total=100
)'''
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
                    id='基础使用方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('默认hideOnSinglePage=False', innerTextOrientation='left'),

                        fac.AntdPagination(
                            total=10,
                            pageSize=20
                        ),

                        fac.AntdDivider('hideOnSinglePage=True', innerTextOrientation='left'),

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

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　当total参数小于等于当前pageSize时，'),
                                fac.AntdText('设置参数'),
                                fac.AntdText('hideOnSinglePage=True', code=True),
                                fac.AntdText('时会自动隐藏分页组件')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider('默认hideOnSinglePage=False', innerTextOrientation='left'),

fac.AntdPagination(
    total=10,
    pageSize=20
),

fac.AntdDivider('hideOnSinglePage=True', innerTextOrientation='left'),

fac.AntdPagination(
    total=10,
    pageSize=20,
    hideOnSinglePage=True
)'''
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
                            'showQuickJumper、showSizeChanger的使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
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
)'''
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
                    id='showQuickJumper、showSizeChanger的使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPagination(
                            defaultPageSize=10,
                            total=100,
                            simple=True
                        ),

                        fac.AntdDivider(
                            '开启极简模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPagination(
    defaultPageSize=10,
    total=100,
    simple=True
)'''
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
                    id='开启极简模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdSpace(
                                id='pagination-demo-output',
                                direction='vertical'
                            ),
                            text='回调中'
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    fac.AntdSpace(
        id='pagination-demo-output',
        direction='vertical'
    ),
    text='回调中'
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
                            {'title': '基础使用方式', 'href': '#基础使用方式'},
                            {'title': '仅有1页时自动隐藏分页组件', 'href': '#仅有1页时自动隐藏分页组件'},
                            {'title': 'showQuickJumper、showSizeChanger的使用',
                             'href': '#showQuickJumper、showSizeChanger的使用'},
                            {'title': '开启极简模式', 'href': '#开启极简模式'},
                            {'title': '回调示例', 'href': '#回调示例'},
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
