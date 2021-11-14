from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.H2(
            'AntdCollapse(children, id, className, style, *args, **kwargs)',
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

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '基础使用', 'href': '#基础使用'},
                        {'title': '透明面板模式', 'href': '#透明面板模式'},
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
            markdownStr=open('documents/AntdCollapse.md', encoding='utf-8').read()
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
                fac.AntdCollapse(
                    fac.AntdText('测试内容'),
                    title='点击此处展开',
                    is_open=False
                ),

                fac.AntdDivider(
                    '基础使用',
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
fac.AntdCollapse(
    fac.AntdText('测试内容'),
    title='点击此处展开',
    is_open=False
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
                fac.AntdCollapse(
                    fac.AntdText('测试内容'),
                    title='点击此处展开',
                    is_open=False,
                    ghost=True
                ),

                fac.AntdDivider(
                    '透明面板模式',
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
fac.AntdCollapse(
    fac.AntdText('测试内容'),
    title='点击此处展开',
    is_open=False,
    ghost=True
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
            id='透明面板模式',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
