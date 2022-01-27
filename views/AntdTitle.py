from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTitle(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdTitle.md', encoding='utf-8').read()
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
                        fac.AntdParagraph(
                            [
                                fac.AntdTitle('一级标题', level=1),
                                fac.AntdTitle('二级标题', level=2),
                                fac.AntdTitle('三级标题', level=3),
                                fac.AntdTitle('四级标题', level=4),
                                fac.AntdTitle('五级标题', level=5)
                            ]
                        ),

                        fac.AntdDivider(
                            '不同的标题级别',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdTitle', strong=True),
                                fac.AntdText('拥有'),
                                fac.AntdText('AntdText', strong=True),
                                fac.AntdText('的所有常规渲染模式，参数同样适用，这里就不再赘述，仅展示不同'),
                                fac.AntdText('level', strong=True),
                                fac.AntdText('参数下的效果'),
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdParagraph(
    [
        fac.AntdTitle('一级标题', level=1),
        fac.AntdTitle('二级标题', level=2),
        fac.AntdTitle('三级标题', level=3),
        fac.AntdTitle('四级标题', level=4),
        fac.AntdTitle('五级标题', level=5)
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
                    id='不同的标题级别',
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
                            {'title': '不同的标题级别', 'href': '#不同的标题级别'},
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
