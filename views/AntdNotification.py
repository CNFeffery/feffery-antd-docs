from dash import html
from dash import dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app

docs_content = html.Div(
    [
        html.H2(
            'AntdNotification(children, id, className, style, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '基础使用', 'href': '#基础使用'},
                        {'title': '不同的状态', 'href': '#不同的状态'},
                        {'title': '不同的弹出位置', 'href': '#不同的弹出位置'},
                        {'title': '持续显示时长的设置', 'href': '#持续显示时长的设置'},
                    ]
                },
            ],
            containerId='docs-content',
            targetOffset=200
        ),
        html.Span(
            '主要参数说明',
            id='主要参数说明',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        dcc.Markdown(open('documents/AntdNotification.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

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

                fac.AntdSpin(
                    [
                        fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo1', type='primary'),
                        html.Div(id='notification-container-demo1')
                    ],
                    text='回调中'
                ),

                fac.AntdDivider(
                    '基础使用',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　AntdNotification', strong=True),
                        fac.AntdText('的使用方式较为特殊，它属于'),
                        fac.AntdText('昙花一现', strong=True),
                        fac.AntdText('式的组件，不需要事先在'),
                        fac.AntdText('app.layout', strong=True),
                        fac.AntdText('中进行定义，推荐的使用方式是预先定义容纳它的容器，'
                                     '后续回调中直接将'),
                        fac.AntdText('fac.AntdNotification(...)', italic=True),
                        fac.AntdText('对象作为回调输出返回对应容器即可，譬如本例中由按钮触发通知提示框的弹出显示')
                    ]
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                ```Python
                fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo1', type='primary'),
                html.Div(id='notification-container-demo1')
                ...
                @app.callback(
                    Output('notification-container-demo1', 'children'),
                    Input('notification-trigger-button-demo1', 'nClicks'),
                    prevent_initial_call=True
                )
                def notification_demo1(nClicks):
                    return fac.AntdNotification(
                        message='通知提示框测试',
                        description='这是一段辅助说明文字内容'
                    )
                ```
                '''),
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

                fac.AntdSpin(
                    [
                        fac.AntdSelect(
                            placeholder='选择不同的状态',
                            options=[
                                {
                                    'label': 'default',
                                    'value': 'default'
                                },
                                {
                                    'label': 'success',
                                    'value': 'success'
                                },
                                {
                                    'label': 'error',
                                    'value': 'error'
                                },
                                {
                                    'label': 'info',
                                    'value': 'info'
                                },
                                {
                                    'label': 'warning',
                                    'value': 'warning'
                                }
                            ],
                            id='notification-type-select-demo2',
                            style={
                                'width': '200px'
                            }
                        ),
                        fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo2', type='primary'),
                        html.Div(id='notification-container-demo2')
                    ],
                    text='回调中'
                ),

                fac.AntdDivider(
                    '不同的状态',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='选择不同的状态',
                    options=[
                        {
                            'label': 'default',
                            'value': 'default'
                        },
                        {
                            'label': 'success',
                            'value': 'success'
                        },
                        {
                            'label': 'error',
                            'value': 'error'
                        },
                        {
                            'label': 'info',
                            'value': 'info'
                        },
                        {
                            'label': 'warning',
                            'value': 'warning'
                        }
                    ],
                    id='notification-type-select-demo2',
                    style={
                        'width': '200px'
                    }
                ),
                fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo2', type='primary'),
                html.Div(id='notification-container-demo2')
                ...
                @app.callback(
                    Output('notification-container-demo2', 'children'),
                    Input('notification-trigger-button-demo2', 'nClicks'),
                    State('notification-type-select-demo2', 'value'),
                    prevent_initial_call=True
                )
                def notification_demo2(nClicks, value):
                    if value:
                        return fac.AntdNotification(
                            message='通知提示框测试',
                            description='这是一段辅助说明文字内容',
                            type=value
                        )
                ```
                '''),
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
            id='不同的状态',
            className='div-highlight'
        ),

        html.Div(
            [

                fac.AntdSpin(
                    [
                        fac.AntdSelect(
                            placeholder='选择不同的弹出位置',
                            options=[
                                {
                                    'label': 'topLeft',
                                    'value': 'topLeft'
                                },
                                {
                                    'label': 'topRight',
                                    'value': 'topRight'
                                },
                                {
                                    'label': 'bottomLeft',
                                    'value': 'bottomLeft'
                                },
                                {
                                    'label': 'bottomRight',
                                    'value': 'bottomRight'
                                }
                            ],
                            id='notification-placement-select-demo3',
                            style={
                                'width': '200px'
                            }
                        ),
                        fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo3', type='primary'),
                        html.Div(id='notification-container-demo3')
                    ],
                    text='回调中'
                ),

                fac.AntdDivider(
                    '不同的弹出位置',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='选择不同的弹出位置',
                    options=[
                        {
                            'label': 'topLeft',
                            'value': 'topLeft'
                        },
                        {
                            'label': 'topRight',
                            'value': 'topRight'
                        },
                        {
                            'label': 'bottomLeft',
                            'value': 'bottomLeft'
                        },
                        {
                            'label': 'bottomRight',
                            'value': 'bottomRight'
                        }
                    ],
                    id='notification-placement-select-demo3',
                    style={
                        'width': '200px'
                    }
                ),
                fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo3', type='primary'),
                html.Div(id='notification-container-demo3')
                ...
                @app.callback(
                    Output('notification-container-demo3', 'children'),
                    Input('notification-trigger-button-demo3', 'nClicks'),
                    State('notification-placement-select-demo3', 'value'),
                    prevent_initial_call=True
                )
                def notification_demo3(nClicks, value):
                    if value:
                        return fac.AntdNotification(
                            message='通知提示框测试',
                            description='这是一段辅助说明文字内容',
                            placement=value
                        )
                ```
                '''),
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
            id='不同的弹出位置',
            className='div-highlight'
        ),

        html.Div(
            [

                fac.AntdSpin(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSlider(
                                    id='notification-slider-demo4',
                                    tooltipVisible=False,
                                    min=1,
                                    max=10,
                                    step=1,
                                    defaultValue=5,
                                    marks={
                                        **{
                                            i: f'{i}秒'
                                            for i in range(1, 10)
                                        },
                                        **{
                                            10: 'None'
                                        }
                                    },
                                    style={
                                        'width': '400px'
                                    }
                                ),
                                fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo4', type='primary')
                            ],
                            size='large'
                        ),
                        html.Div(id='notification-container-demo4')
                    ],
                    text='回调中'
                ),

                fac.AntdDivider(
                    '持续显示时长的设置',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                ```Python
                fac.AntdSpace(
                    [
                        fac.AntdSlider(
                            id='notification-slider-demo4',
                            tooltipVisible=False,
                            min=1,
                            max=10,
                            step=1,
                            defaultValue=5,
                            marks={
                                **{
                                    i: f'{i}秒'
                                    for i in range(1, 10)
                                },
                                **{
                                    10: 'None'
                                }
                            },
                            style={
                                'width': '400px'
                            }
                        ),
                        fac.AntdButton('触发通知提示框', id='notification-trigger-button-demo4', type='primary')
                    ],
                    size='large'
                ),
                html.Div(id='notification-container-demo4')
                ...
                @app.callback(
                    Output('notification-container-demo4', 'children'),
                    Input('notification-trigger-button-demo4', 'nClicks'),
                    State('notification-slider-demo4', 'value'),
                    prevent_initial_call=True
                )
                def notification_demo4(nClicks, value):
                    if value:
                        return fac.AntdNotification(
                            message=f'持续时长{value}秒' if value != 10 else '持续时长∞秒',
                            description='这是一段辅助说明文字内容',
                            duration=value if value != 10 else None
                        )
                ```
                '''),
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
            id='持续显示时长的设置',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)


@app.callback(
    Output('notification-container-demo1', 'children'),
    Input('notification-trigger-button-demo1', 'nClicks'),
    prevent_initial_call=True
)
def notification_demo1(nClicks):
    return fac.AntdNotification(
        message='通知提示框测试',
        description='这是一段辅助说明文字内容'
    )


@app.callback(
    Output('notification-container-demo2', 'children'),
    Input('notification-trigger-button-demo2', 'nClicks'),
    State('notification-type-select-demo2', 'value'),
    prevent_initial_call=True
)
def notification_demo2(nClicks, value):
    if value:
        return fac.AntdNotification(
            message='通知提示框测试',
            description='这是一段辅助说明文字内容',
            type=value
        )


@app.callback(
    Output('notification-container-demo3', 'children'),
    Input('notification-trigger-button-demo3', 'nClicks'),
    State('notification-placement-select-demo3', 'value'),
    prevent_initial_call=True
)
def notification_demo3(nClicks, value):
    if value:
        return fac.AntdNotification(
            message='通知提示框测试',
            description='这是一段辅助说明文字内容',
            placement=value
        )


@app.callback(
    Output('notification-container-demo4', 'children'),
    Input('notification-trigger-button-demo4', 'nClicks'),
    State('notification-slider-demo4', 'value'),
    prevent_initial_call=True
)
def notification_demo4(nClicks, value):
    return fac.AntdNotification(
        message=f'持续时长{value}秒' if value != 10 else '持续时长∞秒',
        description='这是一段辅助说明文字内容',
        duration=value if value != 10 else None
    )
