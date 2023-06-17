from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdNotification
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
                                'title': '反馈'
                            },
                            {
                                'title': 'AntdNotification 通知提醒框'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染弹出式通知提醒框。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发通知提醒框',
                                id='notification-basic-demo-new'
                            ),

                            html.Div(
                                id='notification-basic-demo'
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '通知提醒框的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的通知提醒框的新增'
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
fac.AntdButton(
    '触发通知提醒框',
    id='notification-basic-demo-new'
),

html.Div(
    id='notification-basic-demo'
)

...

@app.callback(
    Output('notification-basic-demo', 'children'),
    Input('notification-basic-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def notification_basic_demo(nClicks):

    return fac.AntdNotification(
        message='通知提醒框示例',
        description='内容示例'
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
                                    fac.AntdRadioGroup(
                                        id='notification-placement-demo-placement',
                                        options=[
                                            {
                                                'label': placement,
                                                'value': placement
                                            }
                                            for placement in [
                                                'topLeft', 'topRight', 'bottomLeft', 'bottomRight'
                                            ]
                                        ],
                                        defaultValue='topRight'
                                    ),
                                    fac.AntdButton(
                                        '触发通知提醒框',
                                        id='notification-placement-demo-new',
                                        type='primary'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            html.Div(
                                id='notification-placement-demo'
                            ),

                            fac.AntdDivider(
                                '不同的弹出位置',
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
            id='notification-placement-demo-placement',
            options=[
                {
                    'label': placement,
                    'value': placement
                }
                for placement in [
                    'topLeft', 'topRight', 'bottomLeft', 'bottomRight'
                ]
            ],
            defaultValue='topRight'
        ),
        fac.AntdButton(
            '触发通知提醒框',
            id='notification-placement-demo-new',
            type='primary'
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
),

html.Div(
    id='notification-placement-demo'
)

...

@app.callback(
    Output('notification-placement-demo', 'children'),
    Input('notification-placement-demo-new', 'nClicks'),
    State('notification-placement-demo-placement', 'value'),
    prevent_initial_call=True
)
def notification_placement_demo(nClicks, value):

    return fac.AntdNotification(
        message='通知提醒框示例',
        description='内容示例',
        placement=value
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
                        id='不同的弹出位置',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        id='notification-type-demo-type',
                                        options=[
                                            {
                                                'label': type_,
                                                'value': type_
                                            }
                                            for type_ in [
                                                'default', 'info', 'success', 'warning', 'error'
                                            ]
                                        ],
                                        defaultValue='default'
                                    ),
                                    fac.AntdButton(
                                        '触发通知提醒框',
                                        id='notification-type-demo-new',
                                        type='primary'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            html.Div(
                                id='notification-type-demo'
                            ),

                            fac.AntdDivider(
                                '不同的状态类型',
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
            id='notification-type-demo-type',
            options=[
                {
                    'label': type_,
                    'value': type_
                }
                for type_ in [
                    'default', 'info', 'success', 'warning', 'error'
                ]
            ],
            defaultValue='default'
        ),
        fac.AntdButton(
            '触发通知提醒框',
            id='notification-type-demo-new',
            type='primary'
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
),

html.Div(
    id='notification-type-demo'
)

...

@app.callback(
    Output('notification-type-demo', 'children'),
    Input('notification-type-demo-new', 'nClicks'),
    State('notification-type-demo-type', 'value'),
    prevent_initial_call=True
)
def notification_type_demo(nClicks, value):

    return fac.AntdNotification(
        message='通知提醒框示例',
        description='内容示例',
        type=value
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
                        id='不同的状态类型',
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
                        {'title': '不同的弹出位置', 'href': '#不同的弹出位置'},
                        {'title': '不同的状态类型', 'href': '#不同的状态类型'},
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
                component_name='AntdNotification',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
