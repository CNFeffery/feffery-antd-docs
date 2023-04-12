from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdCheckCardGroup
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
                            'title': '选择卡片'
                        },
                        {
                            'title': 'AntdCheckCardGroup 组合选择卡片'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于监听一组选择卡片的选择情况。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    f'选项{i}',
                                    value=i
                                )
                                for i in range(1, 6)
                            ],
                            defaultValue=3
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
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            f'选项{i}',
            value=i
        )
        for i in range(1, 6)
    ],
    defaultValue=3
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
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    f'选项{i}',
                                    value=i
                                )
                                for i in range(1, 6)
                            ],
                            defaultValue=[2, 3, 4],
                            multiple=True
                        ),

                        fac.AntdDivider(
                            '多选模式',
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
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            f'选项{i}',
            value=i
        )
        for i in range(1, 6)
    ],
    defaultValue=[2, 3, 4],
    multiple=True
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
                    id='多选模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fuc.FefferyStyle(
                            rawStyle='''
#check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 3px 8px;
}
'''
                        ),
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    f'选项{i}',
                                    value=i,
                                    style={
                                        'width': 'auto',
                                        'marginRight': 3,
                                        'marginBottom': 3,
                                        'borderRadius': 5
                                    }
                                )
                                for i in range(1, 26)
                            ],
                            id='check-card-group-custom-style-demo',
                            defaultValue=[4, 8, 9, 15],
                            multiple=True
                        ),

                        fac.AntdDivider(
                            '自定义选项样式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fuc.FefferyStyle(
    rawStyle='''
#check-card-group-custom-style-demo .ant-pro-checkcard-content {
    padding: 3px 8px;
}
'''
),
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            f'选项{i}',
            value=i,
            style={
                'width': 'auto',
                'marginRight': 3,
                'marginBottom': 3,
                'borderRadius': 5
            }
        )
        for i in range(1, 26)
    ],
    id='check-card-group-custom-style-demo',
    defaultValue=[4, 8, 9, 15],
    multiple=True
)
"""
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
                    id='自定义选项样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    f'选项{i}',
                                    value=i
                                )
                                for i in range(1, 6)
                            ],
                            id='check-card-group-demo',
                            size='small',
                            multiple=True,
                            defaultValue=[1, 2]
                        ),

                        fac.AntdParagraph(
                            id='check-card-group-demo-output'
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
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            f'选项{i}',
            value=i
        )
        for i in range(1, 6)
    ],
    id='check-card-group-demo',
    size='small',
    multiple=True,
    defaultValue=[1, 2]
),

fac.AntdParagraph(
    id='check-card-group-demo-output'
)

...

@app.callback(
    Output('check-card-group-demo-output', 'children'),
    Input('check-card-group-demo', 'value')
)
def check_card_group_demo(value):

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
                    {'title': '多选模式', 'href': '#多选模式'},
                    {'title': '自定义选项样式', 'href': '#自定义选项样式'},
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
            component_name='AntdCheckCardGroup'
        )
    ],
    style={
        'display': 'flex'
    }
)
