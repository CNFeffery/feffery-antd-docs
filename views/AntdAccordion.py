from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdAccordion
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
                                'title': '数据展示'
                            },
                            {
                                'title': 'AntdAccordion 手风琴'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　展示一组同级内容的特别方式。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdAccordion(
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        )
                                    }
                                    for i in range(1, 6)
                                ]
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
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            )
        }
        for i in range(1, 6)
    ]
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
                            fac.AntdAccordion(
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                accordion=False
                            ),

                            fac.AntdDivider(
                                '关闭手风琴模式',
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
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            )
        }
        for i in range(1, 6)
    ],
    accordion=False
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
                        id='关闭手风琴模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '手风琴模式开',
                                innerTextOrientation='left'
                            ),
                            fac.AntdAccordion(
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultActiveKey=['3']
                            ),

                            fac.AntdDivider(
                                '手风琴模式关',
                                innerTextOrientation='left'
                            ),
                            fac.AntdAccordion(
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultActiveKey=['1', '3', '4'],
                                accordion=False
                            ),

                            fac.AntdDivider(
                                '设置默认展开项',
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
    '手风琴模式开',
    innerTextOrientation='left'
),
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            )
        }
        for i in range(1, 6)
    ],
    defaultActiveKey=['3']
),

fac.AntdDivider(
    '手风琴模式关',
    innerTextOrientation='left'
),
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            )
        }
        for i in range(1, 6)
    ],
    defaultActiveKey=['1', '3', '4'],
    accordion=False
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
                        id='设置默认展开项',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAccordion(
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                expandIconPosition='right'
                            ),

                            fac.AntdDivider(
                                '不同的折叠图标方位',
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
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            )
        }
        for i in range(1, 6)
    ],
    expandIconPosition='right'
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
                        id='不同的折叠图标方位',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAccordion(
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        ),
                                        'extra': fac.AntdButton(
                                            '额外示例',
                                            type='link',
                                            size='small'
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                collapsible='header'
                            ),

                            fac.AntdDivider(
                                '手风琴项额外内容',
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
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            ),
            'extra': fac.AntdButton(
                '额外示例',
                type='link',
                size='small'
            )
        }
        for i in range(1, 6)
    ],
    collapsible='header'
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
                        id='手风琴项额外内容',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAccordion(
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                ghost=True
                            ),

                            fac.AntdDivider(
                                '透明面板模式',
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
fac.AntdAccordion(
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            )
        }
        for i in range(1, 6)
    ],
    ghost=True
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
                        id='透明面板模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAccordion(
                                id='accordion-demo',
                                items=[
                                    {
                                        'title': f'手风琴项示例{i}',
                                        'key': i,
                                        'children': fac.AntdText(
                                            f'手风琴项示例{i}'
                                        )
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultActiveKey=['2']
                            ),

                            fac.AntdParagraph(
                                id='accordion-demo-output'
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
fac.AntdAccordion(
    id='accordion-demo',
    items=[
        {
            'title': f'手风琴项示例{i}',
            'key': i,
            'children': fac.AntdText(
                f'手风琴项示例{i}'
            )
        }
        for i in range(1, 6)
    ],
    defaultActiveKey=['2']
),

fac.AntdParagraph(
    id='accordion-demo-output'
)

...

@app.callback(
    Output('accordion-demo-output', 'children'),
    Input('accordion-demo', 'activeKey')
)
def accordion_demo(activeKey):

    return f'activeKey: {activeKey}'
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
                        {'title': '关闭手风琴模式', 'href': '#关闭手风琴模式'},
                        {'title': '设置默认展开项', 'href': '#设置默认展开项'},
                        {'title': '不同的折叠图标方位', 'href': '#不同的折叠图标方位'},
                        {'title': '手风琴项额外内容', 'href': '#手风琴项额外内容'},
                        {'title': '透明面板模式', 'href': '#透明面板模式'},
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
                component_name='AntdAccordion',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
