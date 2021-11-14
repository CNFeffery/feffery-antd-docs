from dash import dcc
from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.H2(
            'AntdBackTop(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '回到顶部示例', 'href': '#回到顶部示例'}
                    ]
                },
            ],
            containerId='docs-content',
            targetOffset=200
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

        fuc.FefferyMarkdown(
            markdownStr=open('documents/AntdBackTop.md', encoding='utf-8').read()
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
                html.Div(
                    [
                        fac.AntdBackTop(
                            containerId='back-top-container-demo',
                            duration=1
                        ),
                        fac.AntdTitle(
                            '向下滑动一段距离',
                            level=4
                        )
                    ] + [
                        html.Div(
                            [
                                i if i % 2 == 0 else html.Br() for i in range(200)
                            ]
                        )
                    ],
                    id='back-top-container-demo',
                    style={
                        'maxHeight': '500px',
                        'overflowY': 'auto',
                        'position': 'relative',
                        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                        'padding': '20px'
                    }
                ),

                fac.AntdDivider(
                    '回到顶部示例',
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
html.Div(
    [
        fac.AntdBackTop(
            containerId='back-top-container-demo',
            duration=1
        ),
        fac.AntdTitle(
            '向下滑动一段距离',
            level=4
        )
    ] + [
        html.Div(
            [
                i if i % 2 == 0 else html.Br() for i in range(200)
            ]
        )
    ],
    id='back-top-container-demo',
    style={
        'maxHeight': '500px',
        'overflowY': 'auto',
        'position': 'relative',
        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
        'padding': '20px'
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
            id='回到顶部示例',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
