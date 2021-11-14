from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.H2(
            'AntdEmpty(id, className, style, *args, **kwargs)',
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
                        {'title': '自定义描述文字', 'href': '#自定义描述文字'},
                        {'title': '自定义提示图片', 'href': '#自定义提示图片'},
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
            markdownStr=open('documents/AntdEmpty.md', encoding='utf-8').read()
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
                fac.AntdEmpty(),

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
fac.AntdEmpty()'''
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
            id='自定义描述文字',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdEmpty(
                    description='这是一段提示文字'
                ),

                fac.AntdDivider(
                    '自定义描述文字',
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
fac.AntdEmpty(
    description='这是一段提示文字'
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
            id='自定义描述文字',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdEmpty(
                    image='/assets/imgs/feffery-antd-components-logo-planB.svg'
                ),

                fac.AntdDivider(
                    '自定义提示图片',
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
fac.AntdEmpty(
    image='/assets/imgs/feffery-antd-components-logo-planB.svg'
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
            id='自定义提示图片',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
