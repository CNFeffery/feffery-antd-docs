from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdPopupCard
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
                                'title': 'AntdPopupCard 弹出式卡片'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于以弹出式卡片的形式展现内容。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '点击触发',
                                id='popup-card-basic-demo-trigger'
                            ),

                            fac.AntdPopupCard(
                                fac.AntdParagraph(
                                    '内容示例'*20
                                ),
                                id='popup-card-basic-demo',
                                title='弹出式卡片示例',
                                visible=False
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
fac.AntdButton(
    '点击触发',
    id='popup-card-basic-demo-trigger'
),

fac.AntdPopupCard(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    id='popup-card-basic-demo',
    title='弹出式卡片示例',
    visible=False
)

...

@app.callback(
    Output('popup-card-basic-demo', 'visible'),
    Input('popup-card-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_basic_demo(nClicks):

    return True
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
                                    fac.AntdSelect(
                                        id='popup-card-transition-type-demo-select',
                                        defaultValue='fade',
                                        allowClear=False,
                                        options=[
                                            {
                                                'label': transitionType,
                                                'value': transitionType
                                            }
                                            for transitionType in [
                                                'none', 'fade', 'zoom', 'zoom-big',
                                                'zoom-big-fast', 'slide-up', 'slide-down',
                                                'slide-left', 'slide-right', 'move-up',
                                                'move-down', 'move-left', 'move-right'
                                            ]
                                        ],
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdButton(
                                        '点击触发',
                                        id='popup-card-transition-type-demo-trigger'
                                    )
                                ]
                            ),

                            fac.AntdPopupCard(
                                fac.AntdParagraph(
                                    '内容示例'*20
                                ),
                                id='popup-card-transition-type-demo',
                                title='弹出式卡片示例',
                                visible=False
                            ),

                            fac.AntdDivider(
                                '使用不同的显隐动画',
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
        fac.AntdSelect(
            id='popup-card-transition-type-demo-select',
            defaultValue='fade',
            allowClear=False,
            options=[
                {
                    'label': transitionType,
                    'value': transitionType
                }
                for transitionType in [
                    'none', 'fade', 'zoom', 'zoom-big',
                    'zoom-big-fast', 'slide-up', 'slide-down',
                    'slide-left', 'slide-right', 'move-up',
                    'move-down', 'move-left', 'move-right'
                ]
            ],
            style={
                'width': 200
            }
        ),
        fac.AntdButton(
            '点击触发',
            id='popup-card-transition-type-demo-trigger'
        )
    ]
),

fac.AntdPopupCard(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    id='popup-card-transition-type-demo',
    title='弹出式卡片示例',
    visible=False
)

...

@app.callback(
    Output('popup-card-transition-type-demo', 'transitionType'),
    Input('popup-card-transition-type-demo-select', 'value')
)
def popup_card_transition_type_demo(value):

    return value


@app.callback(
    Output('popup-card-transition-type-demo', 'visible'),
    Input('popup-card-transition-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_transition_type_demo_visible(nClicks):

    return True
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
                        id='使用不同的显隐动画',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        id='popup-card-close-icon-type-demo-select',
                                        defaultValue='default',
                                        allowClear=False,
                                        options=[
                                            {
                                                'label': closeIconType,
                                                'value': closeIconType
                                            }
                                            for closeIconType in [
                                                'default', 'outlined', 'two-tone'
                                            ]
                                        ],
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdButton(
                                        '点击触发',
                                        id='popup-card-close-icon-type-demo-trigger'
                                    )
                                ]
                            ),

                            fac.AntdPopupCard(
                                fac.AntdParagraph(
                                    '内容示例'*20
                                ),
                                id='popup-card-close-icon-type-demo',
                                title='弹出式卡片示例',
                                visible=False
                            ),

                            fac.AntdDivider(
                                '使用不同的关闭按钮',
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
        fac.AntdSelect(
            id='popup-card-close-icon-type-demo-select',
            defaultValue='default',
            allowClear=False,
            options=[
                {
                    'label': closeIconType,
                    'value': closeIconType
                }
                for closeIconType in [
                    'default', 'outlined', 'two-tone'
                ]
            ],
            style={
                'width': 200
            }
        ),
        fac.AntdButton(
            '点击触发',
            id='popup-card-close-icon-type-demo-trigger'
        )
    ]
),

fac.AntdPopupCard(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    id='popup-card-close-icon-type-demo',
    title='弹出式卡片示例',
    visible=False
)

...

@app.callback(
    Output('popup-card-close-icon-type-demo', 'closeIconType'),
    Input('popup-card-close-icon-type-demo-select', 'value')
)
def popup_card_close_icon_type_demo(value):

    return value


@app.callback(
    Output('popup-card-close-icon-type-demo', 'visible'),
    Input('popup-card-close-icon-type-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_close_icon_type_demo_visible(nClicks):

    return True
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
                        id='使用不同的关闭按钮',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '点击触发',
                                id='popup-card-draggable-demo-trigger'
                            ),

                            fac.AntdPopupCard(
                                fac.AntdParagraph(
                                    '内容示例'*20
                                ),
                                id='popup-card-draggable-demo',
                                title='弹出式卡片示例',
                                visible=False,
                                draggable=True
                            ),

                            fac.AntdDivider(
                                '可拖拽',
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
fac.AntdButton(
    '点击触发',
    id='popup-card-draggable-demo-trigger'
),

fac.AntdPopupCard(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    id='popup-card-draggable-demo',
    title='弹出式卡片示例',
    visible=False,
    draggable=True
)

...

@app.callback(
    Output('popup-card-draggable-demo', 'visible'),
    Input('popup-card-draggable-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_draggable_demo(nClicks):

    return True
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
                        id='可拖拽',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '点击触发',
                                id='popup-card-custom-position-demo-trigger'
                            ),

                            fac.AntdPopupCard(
                                fac.AntdParagraph(
                                    '内容示例'*20
                                ),
                                id='popup-card-custom-position-demo',
                                title='弹出式卡片示例',
                                visible=False,
                                style={
                                    'bottom': 25,
                                    'left': 25,
                                    'position': 'fixed',
                                    'top': 'auto'  # 用于覆盖默认的top: 100px设定
                                }
                            ),

                            fac.AntdDivider(
                                '初始化弹出位置',
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
fac.AntdButton(
    '点击触发',
    id='popup-card-custom-position-demo-trigger'
),

fac.AntdPopupCard(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    id='popup-card-custom-position-demo',
    title='弹出式卡片示例',
    visible=False,
    style={
        'bottom': 25,
        'left': 25,
        'position': 'fixed',
        'top': 'auto'  # 用于覆盖默认的top: 100px设定
    }
)

...

@app.callback(
    Output('popup-card-custom-position-demo', 'visible'),
    Input('popup-card-custom-position-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def popup_card_custom_position_demo(nClicks):

    return True
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
                        id='初始化弹出位置',
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
                        {'title': '使用不同的显隐动画', 'href': '#使用不同的显隐动画'},
                        {'title': '使用不同的关闭按钮', 'href': '#使用不同的关闭按钮'},
                        {'title': '可拖拽', 'href': '#可拖拽'},
                        {'title': '初始化弹出位置', 'href': '#初始化弹出位置'},
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
                component_name='AntdPopupCard',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
