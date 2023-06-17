from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdTransfer
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
                                'title': '数据录入'
                            },
                            {
                                'title': 'AntdTransfer 穿梭框'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于以直观的方式在两栏中移动选项，帮助用户完成选择行为。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 10)
                                ],
                                targetKeys=[2, 3, 4]
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
fac.AntdTransfer(
    dataSource=[
        {
            'key': i,
            'title': f'选项{i}'
        }
        for i in range(1, 10)
    ],
    targetKeys=[2, 3, 4]
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
                            fac.AntdSpace(
                                [
                                    fac.AntdSpace(
                                        [
                                            fac.AntdDivider(
                                                f'height="{height}"',
                                                innerTextOrientation='left'
                                            ),
                                            fac.AntdTransfer(
                                                dataSource=[
                                                    {
                                                        'key': i,
                                                        'title': f'选项{i}'
                                                    }
                                                    for i in range(1, 10)
                                                ],
                                                targetKeys=[2, 3, 4],
                                                height=height
                                            )
                                        ],
                                        direction='vertical',
                                        style={
                                            'width': '100%'
                                        }
                                    )
                                    for height in [
                                        '300px', '10rem', '30vh'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '自定义穿梭框高度',
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
    [
        fac.AntdSpace(
            [
                fac.AntdDivider(
                    f'height="{height}"',
                    innerTextOrientation='left'
                ),
                fac.AntdTransfer(
                    dataSource=[
                        {
                            'key': i,
                            'title': f'选项{i}'
                        }
                        for i in range(1, 10)
                    ],
                    targetKeys=[2, 3, 4],
                    height=height
                )
            ],
            direction='vertical',
            style={
                'width': '100%'
            }
        )
        for height in [
            '300px', '10rem', '30vh'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
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
                        id='自定义穿梭框高度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 50)
                                ],
                                targetKeys=[2, 3, 4],
                                pagination={
                                    'pageSize': 5
                                }
                            ),

                            fac.AntdDivider(
                                '翻页展示',
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
fac.AntdTransfer(
    dataSource=[
        {
            'key': i,
            'title': f'选项{i}'
        }
        for i in range(1, 50)
    ],
    targetKeys=[2, 3, 4],
    pagination={
        'pageSize': 5
    }
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
                        id='翻页展示',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 10)
                                ],
                                targetKeys=[2, 3, 4],
                                operations=['放入', '移出']
                            ),

                            fac.AntdDivider(
                                '自定义移项按钮内容',
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
fac.AntdTransfer(
    dataSource=[
        {
            'key': i,
            'title': f'选项{i}'
        }
        for i in range(1, 10)
    ],
    targetKeys=[2, 3, 4],
    operations=['放入', '移出']
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
                        id='自定义移项按钮内容',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 10)
                                ],
                                targetKeys=[2, 3, 4],
                                showSearch=True
                            ),

                            fac.AntdDivider(
                                '添加搜索框',
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
fac.AntdTransfer(
    dataSource=[
        {
            'key': i,
            'title': f'选项{i}'
        }
        for i in range(1, 10)
    ],
    targetKeys=[2, 3, 4],
    showSearch=True
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
                        id='添加搜索框',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        id='transfer-multiple-mode-search-demo-switch-mode',
                                        options=[
                                            {
                                                'label': mode,
                                                'value': mode
                                            }
                                            for mode in [
                                                'case-insensitive',
                                                'case-sensitive',
                                                'regex'
                                            ]
                                        ],
                                        defaultValue='case-insensitive',
                                        optionType='button'
                                    ),
                                    fac.AntdTransfer(
                                        id='transfer-multiple-mode-search-demo',
                                        dataSource=[
                                            {
                                                'key': i,
                                                'title': f'选项{i}'
                                            }
                                            for i in list('AbCdEf')
                                        ],
                                        targetKeys=[],
                                        showSearch=True
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '多模式搜索',
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
    [
        fac.AntdRadioGroup(
            id='transfer-multiple-mode-search-demo-switch-mode',
            options=[
                {
                    'label': mode,
                    'value': mode
                }
                for mode in [
                    'case-insensitive',
                    'case-sensitive',
                    'regex'
                ]
            ],
            defaultValue='case-insensitive',
            optionType='button'
        ),
        fac.AntdTransfer(
            id='transfer-multiple-mode-search-demo',
            dataSource=[
                {
                    'key': i,
                    'title': f'选项{i}'
                }
                for i in list('AbCdEf')
            ],
            targetKeys=[],
            showSearch=True
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

@app.callback(
    Output('transfer-multiple-mode-search-demo', 'optionFilterMode'),
    Input('transfer-multiple-mode-search-demo-switch-mode', 'value')
)
def transfer_multiple_mode_search_demo(value):

    return value
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
                        id='多模式搜索',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 10)
                                ],
                                targetKeys=[2, 3, 4],
                                titles=['左侧区域', '右侧区域']
                            ),

                            fac.AntdDivider(
                                '设置两侧标题',
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
fac.AntdTransfer(
    dataSource=[
        {
            'key': i,
            'title': f'选项{i}'
        }
        for i in range(1, 10)
    ],
    targetKeys=[2, 3, 4],
    titles=['左侧区域', '右侧区域']
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
                        id='设置两侧标题',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 10)
                                ],
                                targetKeys=[2, 3, 4],
                                disabled=True
                            ),

                            fac.AntdDivider(
                                '禁用状态',
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
fac.AntdTransfer(
    dataSource=[
        {
            'key': i,
            'title': f'选项{i}'
        }
        for i in range(1, 10)
    ],
    targetKeys=[2, 3, 4],
    disabled=True
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTransfer(
                                        dataSource=[
                                            {
                                                'key': i,
                                                'title': f'选项{i}'
                                            }
                                            for i in range(1, 10)
                                        ],
                                        targetKeys=[2, 3, 4],
                                        status='warning'
                                    ),

                                    fac.AntdTransfer(
                                        dataSource=[
                                            {
                                                'key': i,
                                                'title': f'选项{i}'
                                            }
                                            for i in range(1, 10)
                                        ],
                                        targetKeys=[2, 3, 4],
                                        status='error'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '强制状态渲染',
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
    [
        fac.AntdTransfer(
            dataSource=[
                {
                    'key': i,
                    'title': f'选项{i}'
                }
                for i in range(1, 10)
            ],
            targetKeys=[2, 3, 4],
            status='warning'
        ),

        fac.AntdTransfer(
            dataSource=[
                {
                    'key': i,
                    'title': f'选项{i}'
                }
                for i in range(1, 10)
            ],
            targetKeys=[2, 3, 4],
            status='error'
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
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
                        id='强制状态渲染',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTransfer(
                                id='transfer-demo',
                                dataSource=[
                                    {
                                        'key': i,
                                        'title': f'选项{i}'
                                    }
                                    for i in range(1, 10)
                                ],
                                targetKeys=[2, 3, 4]
                            ),

                            fac.AntdSpace(
                                id='transfer-demo-output',
                                direction='vertical'
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
fac.AntdTransfer(
    id='transfer-demo',
    dataSource=[
        {
            'key': i,
            'title': f'选项{i}'
        }
        for i in range(1, 10)
    ],
    targetKeys=[2, 3, 4]
),

fac.AntdSpace(
    id='transfer-demo-output',
    direction='vertical'
)

...

@app.callback(
    Output('transfer-demo-output', 'children'),
    [Input('transfer-demo', 'targetKeys'),
     Input('transfer-demo', 'moveDirection'),
     Input('transfer-demo', 'moveKeys')]
)
def transfer_demo(targetKeys, moveDirection, moveKeys):

    return [
        fac.AntdText(f'targetKeys: {targetKeys}'),
        fac.AntdText(f'moveDirection: {moveDirection}'),
        fac.AntdText(f'moveKeys: {moveKeys}')
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
                        {'title': '自定义穿梭框高度', 'href': '#自定义穿梭框高度'},
                        {'title': '翻页展示', 'href': '#翻页展示'},
                        {'title': '自定义移项按钮内容', 'href': '#自定义移项按钮内容'},
                        {'title': '添加搜索框', 'href': '#添加搜索框'},
                        {'title': '多模式搜索', 'href': '#多模式搜索'},
                        {'title': '设置两侧标题', 'href': '#设置两侧标题'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '强制状态渲染', 'href': '#强制状态渲染'},
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
                component_name='AntdTransfer',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
