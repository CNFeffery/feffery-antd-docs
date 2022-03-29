from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdSpace(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdSpace.md', encoding='utf-8').read()
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

                        fac.AntdDivider('默认水平方向', innerTextOrientation='left'),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ]
                        ),

                        fac.AntdDivider('竖直方向', innerTextOrientation='left'),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdSpace', strong=True),
                                fac.AntdText('可以视作页面元素排列的快捷方式，可以解决简单的多个组件水平方向或竖直方向上单一的等间距排列需求'
                                             '更复杂的网格排列需求请移步'),
                                fac.AntdText('AntdRow/AntdCol', strong=True),
                                fac.AntdText('进行进一步学习')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdDivider('默认水平方向', innerTextOrientation='left'),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ]
),

fac.AntdDivider('竖直方向', innerTextOrientation='left'),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    direction='vertical'
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

                        fac.AntdDivider('start对齐方式', innerTextOrientation='left'),

                        fac.AntdParagraph('水平方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '25px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '10px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='start',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdParagraph('竖直方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '25px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='start',
                            direction='vertical',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdDivider('end对齐方式', innerTextOrientation='left'),

                        fac.AntdParagraph('水平方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '25px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '10px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='end',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdParagraph('竖直方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '25px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='end',
                            direction='vertical',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdDivider('center对齐方式', innerTextOrientation='left'),

                        fac.AntdParagraph('水平方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '25px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '10px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='center',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdParagraph('竖直方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '25px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='center',
                            direction='vertical',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdDivider('baseline对齐方式', innerTextOrientation='left'),

                        fac.AntdParagraph('水平方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '25px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '10px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='baseline',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdParagraph('竖直方向：', strong=True),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '25px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            align='baseline',
                            direction='vertical',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdDivider(
                            '不同的对齐方式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdDivider('start对齐方式', innerTextOrientation='left'),

fac.AntdParagraph('水平方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '25px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '10px',
                'width': '50px'
            }
        )
    ],
    align='start',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdParagraph('竖直方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '25px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    align='start',
    direction='vertical',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdDivider('end对齐方式', innerTextOrientation='left'),

fac.AntdParagraph('水平方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '25px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '10px',
                'width': '50px'
            }
        )
    ],
    align='end',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdParagraph('竖直方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '25px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    align='end',
    direction='vertical',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdDivider('center对齐方式', innerTextOrientation='left'),

fac.AntdParagraph('水平方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '25px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '10px',
                'width': '50px'
            }
        )
    ],
    align='center',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdParagraph('竖直方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '25px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    align='center',
    direction='vertical',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdDivider('baseline对齐方式', innerTextOrientation='left'),

fac.AntdParagraph('水平方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '25px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '10px',
                'width': '50px'
            }
        )
    ],
    align='baseline',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdParagraph('竖直方向：', strong=True),

fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '25px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    align='baseline',
    direction='vertical',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
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
                    id='不同的对齐方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('size="middle"', innerTextOrientation='left'),
                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            size='middle',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),
                        fac.AntdDivider('size="large"', innerTextOrientation='left'),
                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            size='large',
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdDivider('size=50', innerTextOrientation='left'),
                        fac.AntdSpace(
                            [
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(0, 146, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                ),
                                html.Div(
                                    style={
                                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                                        'height': '50px',
                                        'width': '50px'
                                    }
                                )
                            ],
                            size=50,
                            style={
                                'backgroundColor': 'rgba(241, 241, 241, 0.6)',
                                'padding': '10px'
                            }
                        ),

                        fac.AntdDivider(
                            '调节间隔尺寸',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdDivider('size="middle"', innerTextOrientation='left'),
fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    size='middle',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),
fac.AntdDivider('size="large"', innerTextOrientation='left'),
fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    size='large',
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
),

fac.AntdDivider('size=50', innerTextOrientation='left'),
fac.AntdSpace(
    [
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(0, 146, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        ),
        html.Div(
            style={
                'backgroundColor': 'rgba(64, 173, 255, 1)',
                'height': '50px',
                'width': '50px'
            }
        )
    ],
    size=50,
    style={
        'backgroundColor': 'rgba(241, 241, 241, 0.6)',
        'padding': '10px'
    }
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
                    id='调节间隔尺寸',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                html.Div('子组件1'),
                                html.Div('子组件2'),
                                html.Div('子组件3')
                            ],
                            addSplitLine=True,
                            style={
                                'padding': '10px'
                            }
                        ),

                        fac.AntdDivider(
                            '添加分隔线',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        html.Div('子组件1'),
        html.Div('子组件2'),
        html.Div('子组件3')
    ],
    addSplitLine=True,
    style={
        'padding': '10px'
    }
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
                    id='添加分隔线',
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
                            {'title': '不同的对齐方式', 'href': '#不同的对齐方式'},
                            {'title': '调节间隔尺寸', 'href': '#调节间隔尺寸'},
                            {'title': '添加分隔线', 'href': '#添加分隔线'},
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
