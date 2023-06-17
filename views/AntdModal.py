from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdModal
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
                                'title': 'AntdModal 对话框'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染弹出式对话框。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例对话框',
                                id='modal-basic-demo-open',
                                type='primary'
                            ),

                            fac.AntdModal(
                                '示例内容',
                                id='modal-basic-demo',
                                title='对话框示例'
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
    '触发示例对话框',
    id='modal-basic-demo-open',
    type='primary'
),

fac.AntdModal(
    '示例内容',
    id='modal-basic-demo',
    title='对话框示例'
)

...

@app.callback(
    Output('modal-basic-demo', 'visible'),
    Input('modal-basic-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_basic_demo(nClicks):

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
                            fac.AntdButton(
                                '触发示例对话框',
                                id='modal-footer-demo-open',
                                type='primary'
                            ),

                            fac.AntdModal(
                                '示例内容',
                                id='modal-footer-demo',
                                title='对话框示例',
                                renderFooter=True
                            ),

                            fac.AntdDivider(
                                '渲染底部操作区',
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
    '触发示例对话框',
    id='modal-footer-demo-open',
    type='primary'
),

fac.AntdModal(
    '示例内容',
    id='modal-footer-demo',
    title='对话框示例',
    renderFooter=True
)

...

@app.callback(
    Output('modal-footer-demo', 'visible'),
    Input('modal-footer-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_footer_demo(nClicks):

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
                        id='渲染底部操作区',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例对话框',
                                id='modal-custom-button-demo-open',
                                type='primary'
                            ),

                            fac.AntdModal(
                                '示例内容',
                                id='modal-custom-button-demo',
                                title='对话框示例',
                                renderFooter=True,
                                okText='Ok',
                                cancelText='Cancel',
                                cancelButtonProps={
                                    'danger': True
                                }
                            ),

                            fac.AntdDivider(
                                '自定义操作按钮',
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
    '触发示例对话框',
    id='modal-custom-button-demo-open',
    type='primary'
),

fac.AntdModal(
    '示例内容',
    id='modal-custom-button-demo',
    title='对话框示例',
    renderFooter=True,
    okText='Ok',
    cancelText='Cancel',
    cancelButtonProps={
        'danger': True
    }
)

...

@app.callback(
    Output('modal-custom-button-demo', 'visible'),
    Input('modal-custom-button-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_custom_button_demo(nClicks):

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
                        id='自定义操作按钮',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例对话框',
                                id='modal-width-demo-open',
                                type='primary'
                            ),

                            fac.AntdModal(
                                '示例内容',
                                id='modal-width-demo',
                                title='对话框示例',
                                width='75vw'
                            ),

                            fac.AntdDivider(
                                '自定义宽度',
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
    '触发示例对话框',
    id='modal-width-demo-open',
    type='primary'
),

fac.AntdModal(
    '示例内容',
    id='modal-width-demo',
    title='对话框示例',
    width='75vw'
),

fac.AntdDivider(
    '自定义宽度',
    lineColor='#f0f0f0',
    innerTextOrientation='left'
)

...

@app.callback(
    Output('modal-width-demo', 'visible'),
    Input('modal-width-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_width_demo(nClicks):

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
                        id='自定义宽度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例对话框',
                                id='modal-centered-demo-open',
                                type='primary'
                            ),

                            fac.AntdModal(
                                '示例内容',
                                id='modal-centered-demo',
                                title='对话框示例',
                                centered=True
                            ),

                            fac.AntdDivider(
                                '垂直居中',
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
    '触发示例对话框',
    id='modal-centered-demo-open',
    type='primary'
),

fac.AntdModal(
    '示例内容',
    id='modal-centered-demo',
    title='对话框示例',
    centered=True
)

...

@app.callback(
    Output('modal-centered-demo', 'visible'),
    Input('modal-centered-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_centered_demo(nClicks):

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
                        id='垂直居中',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例对话框',
                                id='modal-loading-demo-open',
                                type='primary'
                            ),

                            fac.AntdModal(
                                '示例内容',
                                id='modal-loading-demo',
                                title='对话框示例',
                                confirmAutoSpin=True,
                                loadingOkText='运算中',
                                okClickClose=False,
                                renderFooter=True
                            ),

                            fac.AntdDivider(
                                '利用加载中状态',
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
    '触发示例对话框',
    id='modal-loading-demo-open',
    type='primary'
),

fac.AntdModal(
    '示例内容',
    id='modal-loading-demo',
    title='对话框示例',
    confirmAutoSpin=True,
    loadingOkText='运算中',
    okClickClose=False,
    renderFooter=True
)

...

import time

...

@app.callback(
    Output('modal-loading-demo', 'visible'),
    Input('modal-loading-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def modal_loading_demo(nClicks):

    return True


@app.callback(
    Output('modal-loading-demo', 'confirmLoading'),
    Input('modal-loading-demo', 'okCounts'),
    prevent_initial_call=True
)
def modal_loading_reset(okCounts):

    time.sleep(2)

    return False
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
                        id='利用加载中状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例对话框',
                                id='modal-callback-demo-open',
                                type='primary'
                            ),

                            fac.AntdModal(
                                '示例内容',
                                id='modal-callback-demo',
                                title='对话框示例',
                                renderFooter=True
                            ),

                            html.Pre(
                                id='modal-callback-demo-output'
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
fac.AntdButton(
    '触发示例对话框',
    id='modal-callback-demo-open',
    type='primary'
),

fac.AntdModal(
    '示例内容',
    id='modal-callback-demo',
    title='对话框示例',
    renderFooter=True
),

html.Pre(
    id='modal-callback-demo-output'
)

...

import json

...

@app.callback(
    Output('modal-callback-demo-output', 'children'),
    [Input('modal-callback-demo', 'okCounts'),
     Input('modal-callback-demo', 'cancelCounts'),
     Input('modal-callback-demo', 'closeCounts')],
    prevent_initial_call=True
)
def handle_modal_callback_demo(okCounts, cancelCounts, closeCounts):

    return json.dumps(
        dict(
            okCounts=okCounts,
            cancelCounts=cancelCounts,
            closeCounts=closeCounts
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
                        {'title': '渲染底部操作区', 'href': '#渲染底部操作区'},
                        {'title': '自定义操作按钮', 'href': '#自定义操作按钮'},
                        {'title': '自定义宽度', 'href': '#自定义宽度'},
                        {'title': '垂直居中', 'href': '#垂直居中'},
                        {'title': '利用加载中状态', 'href': '#利用加载中状态'},
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
                component_name='AntdModal',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
