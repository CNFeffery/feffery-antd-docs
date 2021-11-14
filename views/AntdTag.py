from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.H2(
            'AntdTag(id, className, style, *args, **kwargs)',
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
                        {'title': '不同的色彩风格', 'href': '#不同的色彩风格'},
                        {'title': '充当链接功能', 'href': '#充当链接功能'},
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
            markdownStr=open('documents/AntdTag.md', encoding='utf-8').read()
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
                fac.AntdTag(
                    content='标签测试'
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
fac.AntdTag(
    content='标签测试'
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
                fac.AntdDivider('内置色彩风格', innerTextOrientation='left'),

                fac.AntdSpace(
                    [
                        fac.AntdTag(
                            content=color,
                            color=color
                        )
                        for color in [
                        'magenta',
                        'red',
                        'volcano',
                        'orange',
                        'gold',
                        'lime',
                        'green',
                        'cyan',
                        'blue',
                        'geekblue',
                        'purple'
                    ]
                    ],
                    direction='vertical'
                ),

                fac.AntdDivider('自定义色彩风格', innerTextOrientation='left'),

                fac.AntdSpace(
                    [
                        fac.AntdTag(
                            content=color,
                            color=color
                        )
                        for color in [
                        '#f50',
                        '#2db7f5',
                        '#87d068',
                        '#108ee9'
                    ]
                    ],
                    direction='vertical'
                ),

                fac.AntdDivider(
                    '不同的色彩风格',
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
fac.AntdDivider('内置色彩风格', innerTextOrientation='left'),

fac.AntdSpace(
    [
        fac.AntdTag(
            content=color,
            color=color
        )
        for color in [
        'magenta',
        'red',
        'volcano',
        'orange',
        'gold',
        'lime',
        'green',
        'cyan',
        'blue',
        'geekblue',
        'purple'
    ]
    ],
    direction='vertical'
),

fac.AntdDivider('自定义色彩风格', innerTextOrientation='left'),

fac.AntdSpace(
    [
        fac.AntdTag(
            content=color,
            color=color
        )
        for color in [
        '#f50',
        '#2db7f5',
        '#87d068',
        '#108ee9'
    ]
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
            id='不同的色彩风格',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdTag(
                    content='fac官方github仓库',
                    color='cyan',
                    href='https://github.com/CNFeffery/feffery-antd-components'
                ),

                fac.AntdDivider(
                    '充当链接功能',
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
fac.AntdTag(
    content='fac官方github仓库',
    color='cyan',
    href='https://github.com/CNFeffery/feffery-antd-components'
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
            id='充当链接功能',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)
