from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdPopconfirm
from .side_props import render_side_props_layout

docs_content = html.Div(
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
                            'title': '反馈'
                        },
                        {
                            'title': 'AntdPopconfirm 气泡确认框'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于实现二次确认功能，相较于对话框更加简便。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdPopconfirm(
                            fac.AntdButton(
                                '触发'
                            ),
                            title='确认继续'
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '触发'
    ),
    title='确认继续'
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
                                fac.AntdPopconfirm(
                                    fac.AntdButton(
                                        placement
                                    ),
                                    title=f'placement="{placement}"',
                                    placement=placement
                                )
                                for placement in [
                                    'top', 'left', 'right', 'bottom',
                                    'topLeft', 'topRight', 'bottomLeft',
                                    'bottomRight', 'leftTop', 'leftBottom',
                                    'rightTop', 'rightBottom'
                                ]
                            ],
                            size='small',
                            wrap=True
                        ),

                        fac.AntdDivider(
                            '不同的展开方向',
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
        fac.AntdPopconfirm(
            fac.AntdButton(
                placement
            ),
            title=f'placement="{placement}"',
            placement=placement
        )
        for placement in [
            'top', 'left', 'right', 'bottom',
            'topLeft', 'topRight', 'bottomLeft',
            'bottomRight', 'leftTop', 'leftBottom',
            'rightTop', 'rightBottom'
        ]
    ],
    size='small',
    wrap=True
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
                    id='不同的展开方向',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPopconfirm(
                            fac.AntdButton(
                                '触发'
                            ),
                            title='气泡确认框',
                            okText='Ok',
                            cancelText='Cancel',
                            cancelButtonProps={
                                'danger': True,
                                'type': 'primary'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义按钮',
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '触发'
    ),
    title='气泡确认框',
    okText='Ok',
    cancelText='Cancel',
    cancelButtonProps={
        'danger': True,
        'type': 'primary'
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
                    id='自定义按钮',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPopconfirm(
                            fac.AntdButton(
                                '点击触发'
                            ),
                            title='trigger="click"',
                            trigger='click'
                        ),

                        fac.AntdDivider(
                            '点击触发',
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '点击触发'
    ),
    title='trigger="click"',
    trigger='click'
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
                    id='点击触发',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPopconfirm(
                            fac.AntdButton(
                                '触发'
                            ),
                            id='popconfirm-demo',
                            title='回调示例'
                        ),

                        html.Pre(
                            id='popconfirm-demo-output'
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '触发'
    ),
    id='popconfirm-demo',
    title='回调示例'
),

html.Pre(
    id='popconfirm-demo-output'
)

...

import json

...

@app.callback(
    Output('popconfirm-demo-output', 'children'),
    [Input('popconfirm-demo', 'confirmCounts'),
     Input('popconfirm-demo', 'cancelCounts')],
    prevent_initial_call=True
)
def popconfirm_demo(confirmCounts, cancelCounts):

    return json.dumps(
        dict(
            confirmCounts=confirmCounts,
            cancelCounts=cancelCounts
        ),
        indent=4,
        ensure_ascii=False
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
                    {'title': '不同的展开方向', 'href': '#不同的展开方向'},
                    {'title': '自定义按钮', 'href': '#自定义按钮'},
                    {'title': '点击触发', 'href': '#点击触发'},
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
            component_name='AntdPopconfirm'
        )
    ],
    style={
        'display': 'flex'
    }
)
