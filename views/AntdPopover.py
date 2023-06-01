from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdPopover
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
                            'title': '数据展示'
                        },
                        {
                            'title': 'AntdPopover 气泡卡片'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于为指定元素添加额外说明信息。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdPopover(
                            fac.AntdButton(
                                '锚点元素'
                            ),
                            title='气泡卡片示例',
                            content='内容示例'
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
fac.AntdPopover(
    fac.AntdButton(
        '锚点元素'
    ),
    title='气泡卡片示例',
    content='内容示例'
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
                                fac.AntdPopover(
                                    fac.AntdButton(
                                        placement
                                    ),
                                    title='气泡卡片示例',
                                    content=f'placement="{placement}"',
                                    placement=placement
                                )
                                for placement in [
                                    'top', 'left', 'right', 'bottom',
                                    'topLeft', 'topRight', 'bottomLeft',
                                    'bottomRight', 'leftTop', 'leftBottom',
                                    'rightTop', 'rightBottom'
                                ]
                            ],
                            wrap=True
                        ),

                        fac.AntdDivider(
                            '不同的悬浮层展开方向',
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
        fac.AntdPopover(
            fac.AntdButton(
                placement
            ),
            title='气泡卡片示例',
            content=f'placement="{placement}"',
            placement=placement
        )
        for placement in [
            'top', 'left', 'right', 'bottom',
            'topLeft', 'topRight', 'bottomLeft',
            'bottomRight', 'leftTop', 'leftBottom',
            'rightTop', 'rightBottom'
        ]
    ],
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
                    id='不同的悬浮层展开方向',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fuc.FefferyHexColorPicker(
                                    id='popover-color-demo-input',
                                    showAlpha=True,
                                    color='#f6f7f866'
                                ),

                                fac.AntdPopover(
                                    fac.AntdButton(
                                        '锚点示例'
                                    ),
                                    id='popover-color-demo',
                                    title='气泡卡片示例'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '自定义背景色',
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
        fuc.FefferyHexColorPicker(
            id='popover-color-demo-input',
            showAlpha=True,
            color='#f6f7f866'
        ),

        fac.AntdPopover(
            fac.AntdButton(
                '锚点示例'
            ),
            id='popover-color-demo',
            title='气泡卡片示例'
        )
    ]
)

...

@app.callback(
    [Output('popover-color-demo', 'color'),
     Output('popover-color-demo', 'content')],
    Input('popover-color-demo-input', 'color')
)
def popover_color_demo(color):

    return [
        color,
        fac.AntdParagraph(
            [
                '当前color: ',
                fac.AntdText(
                    color,
                    copyable=True
                )
            ]
        )
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
                    id='自定义背景色',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPopover(
                            fac.AntdButton(
                                '锚点示例'
                            ),
                            title='气泡卡片示例',
                            content='内容示例'*50,
                            overlayStyle={
                                'width': 250
                            },
                            overlayInnerStyle={
                                'maxHeight': 150,
                                'overflowY': 'auto'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义样式',
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
fac.AntdPopover(
    fac.AntdButton(
        '锚点示例'
    ),
    title='气泡卡片示例',
    content='内容示例'*50,
    overlayStyle={
        'width': 250
    },
    overlayInnerStyle={
        'maxHeight': 150,
        'overflowY': 'auto'
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
                    id='自定义样式',
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
                    {'title': '不同的悬浮层展开方向', 'href': '#不同的悬浮层展开方向'},
                    {'title': '自定义背景色', 'href': '#自定义背景色'},
                    {'title': '自定义样式', 'href': '#自定义样式'},
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
            component_name='AntdPopover'
        )
    ],
    style={
        'display': 'flex'
    }
)
