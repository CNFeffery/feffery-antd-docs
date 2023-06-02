from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdIcon
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
                            'title': '通用'
                        },
                        {
                            'title': 'AntdIcon 图标'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在各种场景下渲染具有提示意义的图标。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdRadioGroup(
                            id='icon-category',
                            options=[
                                {
                                    'label': 'Antd Design精选',
                                    'value': 'antd'
                                },
                                {
                                    'label': 'Material Design精选',
                                    'value': 'md'
                                },
                                {
                                    'label': 'Flat Color精选',
                                    'value': 'fc'
                                },
                                {
                                    'label': 'Devicons精选',
                                    'value': 'di'
                                },
                                {
                                    'label': 'BoxIcons精选',
                                    'value': 'bi'
                                },
                                {
                                    'label': 'Bootstrap精选',
                                    'value': 'bs'
                                },
                                {
                                    'label': 'Game Icons精选',
                                    'value': 'gi'
                                },
                                {
                                    'label': 'IcoMoon Free精选',
                                    'value': 'im'
                                }
                            ],
                            optionType='button',
                            defaultValue='antd',
                            size='small'
                        ),

                        fac.AntdSpin(
                            fac.AntdRow(
                                id='icon-demo',
                                style={
                                    'minHeight': '50px'
                                }
                            )
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
fac.AntdRadioGroup(
    id='icon-category',
    options=[
        {
            'label': 'Antd Design精选',
            'value': 'antd'
        },
        {
            'label': 'Material Design精选',
            'value': 'md'
        },
        {
            'label': 'Flat Color精选',
            'value': 'fc'
        },
        {
            'label': 'Devicons精选',
            'value': 'di'
        },
        {
            'label': 'BoxIcons精选',
            'value': 'bi'
        },
        {
            'label': 'Bootstrap精选',
            'value': 'bs'
        },
        {
            'label': 'Game Icons精选',
            'value': 'gi'
        },
        {
            'label': 'IcoMoon Free精选',
            'value': 'im'
        }
    ],
    optionType='button',
    defaultValue='antd',
    size='small'
),

fac.AntdSpin(
    fac.AntdRow(
        id='icon-demo',
        style={
            'minHeight': '50px'
        }
    )
)

...

@app.callback(
    Output('icon-demo', 'children'),
    Input('icon-category', 'value')
)
def icon_demo_render_callback(value):
    return [
        fac.AntdCol(
            fac.AntdSpace(
                [
                    fac.AntdIcon(
                        icon=icon,
                        style={
                            'fontSize': '28px'
                        }
                    ),
                    fac.AntdText(
                        icon,
                        copyable=True,
                        style={
                            'borderBottom': '1px dashed #e1dfdd'
                        }
                    )
                ],
                direction='vertical',
                size='small',
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'marginBottom': '5px'
                }
            ),
            span=8
        )
        for icon in Config.icon_map_dict[value]
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            '常规点击',
                            innerTextOrientation='left'
                        ),
                        fac.AntdSpace(
                            [
                                fac.AntdIcon(
                                    id='icon-click-demo',
                                    icon='antd-delete',
                                    style={
                                        'cursor': 'pointer'
                                    }
                                ),
                                fac.AntdText(
                                    id='icon-click-demo-output',
                                    style={
                                        'userSelect': 'none'
                                    }
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '500ms防抖点击',
                            innerTextOrientation='left'
                        ),
                        fac.AntdSpace(
                            [
                                fac.AntdIcon(
                                    id='icon-debounce-click-demo',
                                    icon='antd-delete',
                                    debounceWait=500,
                                    style={
                                        'cursor': 'pointer'
                                    }
                                ),
                                fac.AntdText(
                                    id='icon-debounce-click-demo-output',
                                    style={
                                        'userSelect': 'none'
                                    }
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('AntdIcon', strong=True),
                                fac.AntdText(
                                    '也可以类似按钮组件那样监听点击事件（同样支持防抖）'
                                )
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider(
    '常规点击',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdIcon(
            id='icon-click-demo',
            icon='antd-delete',
            style={
                'cursor': 'pointer'
            }
        ),
        fac.AntdText(
            id='icon-click-demo-output',
            style={
                'userSelect': 'none'
            }
        )
    ]
),

fac.AntdDivider(
    '500ms防抖点击',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdIcon(
            id='icon-debounce-click-demo',
            icon='antd-delete',
            debounceWait=500,
            style={
                'cursor': 'pointer'
            }
        ),
        fac.AntdText(
            id='icon-debounce-click-demo-output',
            style={
                'userSelect': 'none'
            }
        )
    ]
)

...

@app.callback(
    Output('icon-click-demo-output', 'children'),
    Input('icon-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def icon_click_demo(nClicks):

    return f'nClicks: {nClicks}'


@app.callback(
    Output('icon-debounce-click-demo-output', 'children'),
    Input('icon-debounce-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def icon_debounce_click_demo(nClicks):

    return f'nClicks: {nClicks}'
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
            component_name='AntdIcon'
        )
    ],
    style={
        'display': 'flex'
    }
)
