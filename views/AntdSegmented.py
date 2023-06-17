from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdSegmented
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
                                'title': 'AntdSegmented 分段控制器'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　通常置于板块顶端用来供用户切换页面内容使用')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSegmented(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': i
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultValue=2
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
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': i
        }
        for i in range(1, 6)
    ],
    defaultValue=2
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
                            fac.AntdSegmented(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': i,
                                        'icon': icon
                                    }
                                    for i, icon in enumerate(
                                        [
                                            'antd-carry-out',
                                            'antd-branches',
                                            'antd-team',
                                            'antd-send',
                                            'antd-setting'
                                        ]
                                    )
                                ],
                                defaultValue=0
                            ),

                            fac.AntdDivider(
                                '为选项添加前缀图标',
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
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': i,
            'icon': icon
        }
        for i, icon in enumerate(
            [
                'antd-carry-out',
                'antd-branches',
                'antd-team',
                'antd-send',
                'antd-setting'
            ]
        )
    ],
    defaultValue=0
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
                        id='为选项添加前缀图标',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSegmented(
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': i
                                            }
                                            for i in range(1, 6)
                                        ],
                                        defaultValue=2,
                                        size=size
                                    )
                                    for size in ['small', 'middle', 'large']
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '不同的尺寸规格',
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
        fac.AntdSegmented(
            options=[
                {
                    'label': f'选项{i}',
                    'value': i
                }
                for i in range(1, 6)
            ],
            defaultValue=2,
            size=size
        )
        for size in ['small', 'middle', 'large']
    ],
    direction='vertical'
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
                        id='不同的尺寸规格',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSegmented(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': i
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultValue=1,
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
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': i
        }
        for i in range(1, 6)
    ],
    defaultValue=1,
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
                            fac.AntdSegmented(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': i
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultValue=1,
                                block=True
                            ),

                            fac.AntdDivider(
                                '撑满父级元素宽度',
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
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': i
        }
        for i in range(1, 6)
    ],
    defaultValue=1,
    block=True
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
                        id='撑满父级元素宽度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSegmented(
                                        id='segmented-demo',
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': i
                                            }
                                            for i in range(1, 6)
                                        ],
                                        defaultValue=2
                                    ),
                                    fac.AntdText(
                                        id='segmented-demo-output'
                                    )
                                ],
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
fac.AntdSpace(
    [
        fac.AntdSegmented(
            id='segmented-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': i
                }
                for i in range(1, 6)
            ],
            defaultValue=2
        ),
        fac.AntdText(
            id='segmented-demo-output'
        )
    ],
    direction='vertical'
)

...

@app.callback(
    Output('segmented-demo-output', 'children'),
    Input('segmented-demo', 'value')
)
def segmented_demo(value):

    return f'value: {value}'
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
                        {'title': '为选项添加前缀图标', 'href': '#为选项添加前缀图标'},
                        {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '撑满父级元素宽度', 'href': '#撑满父级元素宽度'},
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
                component_name='AntdSegmented',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
