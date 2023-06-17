from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdDropdown
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
                                'title': '导航'
                            },
                            {
                                'title': 'AntdDropdown 下拉菜单'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于展示具有若干选项或链接的向下弹出的列表。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdDropdown(
                                title='触发点',
                                menuItems=[
                                    {
                                        'title': '选项1'
                                    },
                                    {
                                        'title': '选项2'
                                    },
                                    {
                                        'isDivider': True
                                    },
                                    {
                                        'title': '选项3-1'
                                    },
                                    {
                                        'title': '选项3-2'
                                    }
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
fac.AntdDropdown(
    title='触发点',
    menuItems=[
        {
            'title': '选项1'
        },
        {
            'title': '选项2'
        },
        {
            'isDivider': True
        },
        {
            'title': '选项3-1'
        },
        {
            'title': '选项3-2'
        }
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
                            fac.AntdSpace(
                                [
                                    fac.AntdDropdown(
                                        title='触发点',
                                        buttonMode=True,
                                        menuItems=[
                                            {
                                                'title': '子页面1'
                                            },
                                            {
                                                'title': '子页面2'
                                            },
                                            {
                                                'isDivider': True
                                            },
                                            {
                                                'title': '子页面3-1'
                                            },
                                            {
                                                'title': '子页面3-2'
                                            }
                                        ]
                                    ),

                                    fac.AntdDropdown(
                                        title='触发点',
                                        buttonMode=True,
                                        buttonProps={
                                            'size': 'large',
                                            'type': 'dashed'
                                        },
                                        menuItems=[
                                            {
                                                'title': '子页面1'
                                            },
                                            {
                                                'title': '子页面2'
                                            },
                                            {
                                                'isDivider': True
                                            },
                                            {
                                                'title': '子页面3-1'
                                            },
                                            {
                                                'title': '子页面3-2'
                                            }
                                        ]
                                    ),

                                    fac.AntdDropdown(
                                        title='触发点',
                                        buttonMode=True,
                                        buttonProps={
                                            'size': 'small',
                                            'type': 'primary',
                                            'danger': True
                                        },
                                        menuItems=[
                                            {
                                                'title': '子页面1'
                                            },
                                            {
                                                'title': '子页面2'
                                            },
                                            {
                                                'isDivider': True
                                            },
                                            {
                                                'title': '子页面3-1'
                                            },
                                            {
                                                'title': '子页面3-2'
                                            }
                                        ]
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '按钮模式',
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
        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            menuItems=[
                {
                    'title': '子页面1'
                },
                {
                    'title': '子页面2'
                },
                {
                    'isDivider': True
                },
                {
                    'title': '子页面3-1'
                },
                {
                    'title': '子页面3-2'
                }
            ]
        ),

        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            buttonProps={
                'size': 'large',
                'type': 'dashed'
            },
            menuItems=[
                {
                    'title': '子页面1'
                },
                {
                    'title': '子页面2'
                },
                {
                    'isDivider': True
                },
                {
                    'title': '子页面3-1'
                },
                {
                    'title': '子页面3-2'
                }
            ]
        ),

        fac.AntdDropdown(
            title='触发点',
            buttonMode=True,
            buttonProps={
                'size': 'small',
                'type': 'primary',
                'danger': True
            },
            menuItems=[
                {
                    'title': '子页面1'
                },
                {
                    'title': '子页面2'
                },
                {
                    'isDivider': True
                },
                {
                    'title': '子页面3-1'
                },
                {
                    'title': '子页面3-2'
                }
            ]
        )
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
                        id='按钮模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDropdown(
                                title='触发点',
                                buttonMode=True,
                                buttonProps={
                                    'style': {
                                        'color': 'white',
                                        'width': 150,
                                        'background': 'linear-gradient(135deg,#8a2be2,#ffa500,#f8f8ff)'
                                    }
                                },
                                menuItems=[
                                    {
                                        'title': '子页面1'
                                    },
                                    {
                                        'title': '子页面2'
                                    },
                                    {
                                        'isDivider': True
                                    },
                                    {
                                        'title': '子页面3-1'
                                    },
                                    {
                                        'title': '子页面3-2'
                                    }
                                ]
                            ),

                            fac.AntdDivider(
                                '自定义按钮样式',
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
fac.AntdDropdown(
    title='触发点',
    buttonMode=True,
    buttonProps={
        'style': {
            'color': 'white',
            'width': 150,
            'background': 'linear-gradient(135deg,#8a2be2,#ffa500,#f8f8ff)'
        }
    },
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
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
                        id='自定义按钮样式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fuc.FefferyDiv(
                                '请在此区域内任意位置点击鼠标右键',
                                id='dropdown-free-position-demo-trigger',
                                enableListenContextMenu=True,
                                style={
                                    'borderRadius': 6,
                                    'background': '#adb5bd',
                                    'height': 400,
                                    'color': 'white',
                                    'display': 'flex',
                                    'justifyContent': 'center',
                                    'alignItems': 'center'
                                }
                            ),

                            html.Div(
                                id='dropdown-free-position-demo-container'),

                            fac.AntdDivider(
                                '自由位置模式',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '自由位置模式的最典型应用场景是配合',
                                    fac.AntdText(
                                        'fuc.FefferyDiv',
                                        code=True
                                    ),
                                    '的右键事件监听功能，实现监听区域内鼠标右键触发自定义右键菜单'
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
fuc.FefferyDiv(
    '请在此区域内任意位置点击鼠标右键',
    id='dropdown-free-position-demo-trigger',
    enableListenContextMenu=True,
    style={
        'borderRadius': 6,
        'background': '#adb5bd',
        'height': 400,
        'color': 'white',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    }
),

html.Div(id='dropdown-free-position-demo-container')

...

import uuid

...

@app.callback(
    Output('dropdown-free-position-demo-container', 'children'),
    Input('dropdown-free-position-demo-trigger', 'contextMenuEvent'),
    prevent_initial_call=True
)
def dropdown_free_position_demo(contextMenuEvent):

    if contextMenuEvent:

        return fac.AntdDropdown(
            key=str(uuid.uuid4()),
            visible=True,
            freePosition=True,
            freePositionStyle={
                'left': contextMenuEvent['clientX'],
                'top': contextMenuEvent['clientY']
            },
            menuItems=[
                {
                    'title': f'右键菜单选项{i}',
                    'key': f'右键菜单选项{i}'
                }
                for i in range(1, 6)
            ],
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
                        id='自由位置模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDropdown(
                                title='触发点',
                                trigger='click',
                                menuItems=[
                                    {
                                        'title': '子页面1'
                                    },
                                    {
                                        'title': '子页面2'
                                    },
                                    {
                                        'isDivider': True
                                    },
                                    {
                                        'title': '子页面3-1'
                                    },
                                    {
                                        'title': '子页面3-2'
                                    }
                                ]
                            ),

                            fac.AntdDivider(
                                '点击触发方式',
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
fac.AntdDropdown(
    title='触发点',
    trigger='click',
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
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
                        id='点击触发方式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDropdown(
                                title='触发点',
                                arrow=True,
                                menuItems=[
                                    {
                                        'title': '子页面1'
                                    },
                                    {
                                        'title': '子页面2'
                                    },
                                    {
                                        'isDivider': True
                                    },
                                    {
                                        'title': '子页面3-1'
                                    },
                                    {
                                        'title': '子页面3-2'
                                    }
                                ]
                            ),

                            fac.AntdDivider(
                                '添加箭头',
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
fac.AntdDropdown(
    title='触发点',
    arrow=True,
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
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
                        id='添加箭头',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdDropdown(
                                        title=placement,
                                        arrow=True,
                                        placement=placement,
                                        menuItems=[
                                            {
                                                'title': '子页面1'
                                            },
                                            {
                                                'title': '子页面2'
                                            },
                                            {
                                                'isDivider': True
                                            },
                                            {
                                                'title': '子页面3-1'
                                            },
                                            {
                                                'title': '子页面3-2'
                                            }
                                        ]
                                    )
                                    for placement in [
                                        'bottomLeft', 'bottomCenter', 'bottomRight',
                                        'topLeft', 'topCenter', 'topRight']
                                ],
                                size=20
                            ),

                            fac.AntdDivider(
                                '不同的弹出方位',
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
        fac.AntdDropdown(
            title=placement,
            arrow=True,
            placement=placement,
            menuItems=[
                {
                    'title': '子页面1'
                },
                {
                    'title': '子页面2'
                },
                {
                    'isDivider': True
                },
                {
                    'title': '子页面3-1'
                },
                {
                    'title': '子页面3-2'
                }
            ]
        )
        for placement in [
            'bottomLeft', 'bottomCenter', 'bottomRight',
            'topLeft', 'topCenter', 'topRight']
    ],
    size=20
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
                        id='不同的弹出方位',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDropdown(
                                id='dropdown-demo',
                                title='触发点',
                                arrow=True,
                                placement='topCenter',
                                menuItems=[
                                    {
                                        'title': '子页面1',
                                        'key': '子页面1',
                                    },
                                    {
                                        'title': '子页面2',
                                        'key': '子页面2',
                                    },
                                    {
                                        'isDivider': True
                                    },
                                    {
                                        'title': '子页面3-1',
                                        'key': '子页面3-1'
                                    },
                                    {
                                        'title': '子页面3-2',
                                        'key': '子页面3-2'
                                    }
                                ]
                            ),

                            html.Div(
                                id='dropdown-demo-output'
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
fac.AntdDropdown(
    id='dropdown-demo',
    title='触发点',
    arrow=True,
    placement='topCenter',
    menuItems=[
        {
            'title': '子页面1',
            'key': '子页面1',
        },
        {
            'title': '子页面2',
            'key': '子页面2',
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1',
            'key': '子页面3-1'
        },
        {
            'title': '子页面3-2',
            'key': '子页面3-2'
        }
    ]
),

html.Div(
    id='dropdown-demo-output'
)

...

@app.callback(
    Output('dropdown-demo-output', 'children'),
    [Input('dropdown-demo', 'clickedKey'),
     Input('dropdown-demo', 'nClicks')],
    prevent_initial_call=True
)
def dropdown_demo_callback(clickedKey, nClicks):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey),
        fac.AntdText('　nClicks: ', strong=True),
        fac.AntdText(nClicks)
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
                        {'title': '按钮模式', 'href': '#按钮模式'},
                        {'title': '自定义按钮样式', 'href': '#自定义按钮样式'},
                        {'title': '自由位置模式', 'href': '#自由位置模式'},
                        {'title': '点击触发方式', 'href': '#点击触发方式'},
                        {'title': '添加箭头', 'href': '#添加箭头'},
                        {'title': '不同的弹出方位', 'href': '#不同的弹出方位'},
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
                component_name='AntdDropdown',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
