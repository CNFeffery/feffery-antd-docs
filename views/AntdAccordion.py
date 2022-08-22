from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
import feffery_utils_components as fuc

import callbacks.AntdAccordion

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdAccordion(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdAccordion.md', encoding='utf-8').read()
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
                        fac.AntdAccordion(
                            [
                                fac.AntdAccordionItem(
                                    f'手风琴项{i}测试',
                                    title=f'手风琴项{i}',
                                    key=i
                                )
                                for i in range(5)
                            ]
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
fac.AntdAccordion(
    [
        fac.AntdAccordionItem(
            f'手风琴项{i}测试',
            title=f'手风琴项{i}',
            key=i
        )
        for i in range(5)
    ]
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdAccordion(
                            [
                                fac.AntdAccordionItem(
                                    f'手风琴项{i}测试',
                                    title=f'手风琴项{i}',
                                    key=i
                                )
                                for i in range(5)
                            ],
                            accordion=False
                        ),

                        fac.AntdDivider(
                            '非手风琴模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdAccordion(
    [
        fac.AntdAccordionItem(
            f'手风琴项{i}测试',
            title=f'手风琴项{i}',
            key=i
        )
        for i in range(5)
    ],
    accordion=False
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
                    id='非手风琴模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdAccordion(
                            [
                                fac.AntdAccordionItem(
                                    f'手风琴项{i}测试',
                                    title=f'手风琴项{i}',
                                    key=str(i)
                                )
                                for i in range(5)
                            ],
                            id='accordion-demo',
                            defaultActiveKey='3'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('activeKey：'),
                                fac.AntdText(id='accordion-demo-output')
                            ]
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
fac.AntdAccordion(
    [
        fac.AntdAccordionItem(
            f'手风琴项{i}测试',
            title=f'手风琴项{i}',
            key=str(i)
        )
        for i in range(5)
    ],
    id='accordion-demo',
    defaultActiveKey='3'
),

fac.AntdParagraph(
    [
        fac.AntdText('activeKey：'),
        fac.AntdText(id='accordion-demo-output')
    ]
)

...

@app.callback(
    Output('accordion-demo-output', 'children'),
    Input('accordion-demo', 'activeKey')
)
def accordion_demo_callback(activeKey):

    return str(activeKey)
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
                            {'title': '非手风琴模式', 'href': '#非手风琴模式'},
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
