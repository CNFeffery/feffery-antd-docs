from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdDrawer
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
                                'title': 'AntdDrawer 抽屉'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于构建全屏弹出式额外内容区域。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '打开示例抽屉',
                                id='drawer-basic-demo-open',
                                type='primary'
                            ),

                            fac.AntdDrawer(
                                '示例内容',
                                title='基础抽屉示例',
                                id='drawer-basic-demo'
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
    '打开示例抽屉',
    id='drawer-basic-demo-open',
    type='primary'
),

fac.AntdDrawer(
    '示例内容',
    title='基础抽屉示例',
    id='drawer-basic-demo'
)

...

@app.callback(
    Output('drawer-basic-demo', 'visible'),
    Input('drawer-basic-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_basic_demo(nCLicks):

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
                                    fac.AntdRadioGroup(
                                        id='drawer-placement-demo-placement',
                                        options=[
                                            {
                                                'label': placement,
                                                'value': placement
                                            }
                                            for placement in [
                                                'left', 'top', 'right', 'bottom'
                                            ]
                                        ],
                                        defaultValue='right'
                                    ),
                                    fac.AntdButton(
                                        '打开示例抽屉',
                                        id='drawer-placement-demo-open',
                                        type='primary'
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDrawer(
                                '示例内容',
                                id='drawer-placement-demo'
                            ),

                            fac.AntdDivider(
                                '不同的展开方位',
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
            id='drawer-placement-demo-placement',
            options=[
                {
                    'label': placement,
                    'value': placement
                }
                for placement in [
                    'left', 'top', 'right', 'bottom'
                ]
            ],
            defaultValue='right'
        ),
        fac.AntdButton(
            '打开示例抽屉',
            id='drawer-placement-demo-open',
            type='primary'
        )
    ],
    direction='vertical'
),

fac.AntdDrawer(
    '示例内容',
    id='drawer-placement-demo'
)

...

@app.callback(
    [Output('drawer-placement-demo', 'title'),
     Output('drawer-placement-demo', 'placement')],
    Input('drawer-placement-demo-placement', 'value')
)
def update_drawer_placement_and_title_dmeo(value):

    return [
        f'placement="{value}"',
        value
    ]


@app.callback(
    Output('drawer-placement-demo', 'visible'),
    Input('drawer-placement-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def draw_placement_demo(nClicks):

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
                        id='不同的展开方位',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '打开示例抽屉',
                                id='drawer-extra-demo-open',
                                type='primary'
                            ),

                            fac.AntdDrawer(
                                '示例内容',
                                id='drawer-extra-demo',
                                title='抽屉示例',
                                width='50vw',
                                extra=fac.AntdSpace(
                                    [
                                        fac.AntdButton(
                                            '操作1',
                                            type='primary'
                                        ),
                                        fac.AntdButton(
                                            '操作2',
                                            type='primary',
                                            danger=True
                                        )
                                    ],
                                    size='small'
                                )
                            ),

                            fac.AntdDivider(
                                '定义额外操作区元素',
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
    '打开示例抽屉',
    id='drawer-extra-demo-open',
    type='primary'
),

fac.AntdDrawer(
    '示例内容',
    id='drawer-extra-demo',
    title='抽屉示例',
    width='50vw',
    extra=fac.AntdSpace(
        [
            fac.AntdButton(
                '操作1',
                type='primary'
            ),
            fac.AntdButton(
                '操作2',
                type='primary',
                danger=True
            )
        ],
        size='small'
    )
)

...

@app.callback(
    Output('drawer-extra-demo', 'visible'),
    Input('drawer-extra-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_extra_demo(nClicks):

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
                        id='定义额外操作区元素',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    fac.AntdButton(
                                        '打开示例抽屉',
                                        id='drawer-local-demo-open',
                                        type='primary'
                                    ),
                                    fac.AntdDrawer(
                                        '示例内容',
                                        id='drawer-local-demo',
                                        title='局部容器抽屉示例',
                                        containerId='drawer-local-container'
                                    )
                                ],
                                id='drawer-local-container',
                                style={
                                    'height': 400,
                                    'border': '1px solid #e9ecef',
                                    'position': 'relative',
                                    'padding': 25,
                                    'overflowX': 'hidden'
                                }
                            ),

                            fac.AntdDivider(
                                '在局部容器中使用',
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
html.Div(
    [
        fac.AntdButton(
            '打开示例抽屉',
            id='drawer-local-demo-open',
            type='primary'
        ),
        fac.AntdDrawer(
            '示例内容',
            id='drawer-local-demo',
            title='局部容器抽屉示例',
            containerId='drawer-local-container'
        )
    ],
    id='drawer-local-container',
    style={
        'height': 400,
        'border': '1px solid #e9ecef',
        'position': 'relative',
        'padding': 25,
        'overflowX': 'hidden'
    }
)

...

@app.callback(
    Output('drawer-local-demo', 'visible'),
    Input('drawer-local-demo-open', 'nClicks'),
    prevent_initial_call=True
)
def drawer_local_demo(nClicks):

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
                        id='在局部容器中使用',
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
                        {'title': '不同的展开方位', 'href': '#不同的展开方位'},
                        {'title': '定义额外操作区元素', 'href': '#定义额外操作区元素'},
                        {'title': '在局部容器中使用', 'href': '#在局部容器中使用'},
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
                component_name='AntdDrawer',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
