from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdSegmentedColoring
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
                            'title': '数据录入'
                        },
                        {
                            'title': 'AntdSegmentedColoring 分段着色'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于配合数据可视化进行分段着色控制，或作为静态的图例进行展示。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSegmentedColoring(
                            min=-10,
                            max=10,
                            breakpoints=[0, 1, 2, 3, 4, 5],
                            colors=[
                                "#deecf9",
                                "#71afe5",
                                "#2b88d8",
                                "#0078d4",
                                "#106ebe"
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
fac.AntdSegmentedColoring(
    min=-10,
    max=10,
    breakpoints=[0, 1, 2, 3, 4, 5],
    colors=[
        "#deecf9",
        "#71afe5",
        "#2b88d8",
        "#0078d4",
        "#106ebe"
    ]
)
'''
                            ),
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
                        fac.AntdSpace(
                            [
                                fac.AntdSegmentedColoring(
                                    min=-10,
                                    max=10,
                                    breakpoints=[0, 1, 2, 3, 4, 5],
                                    colors=["#deecf9", "#71afe5",
                                            "#2b88d8", "#0078d4",
                                            "#106ebe"]
                                ),
                                fac.AntdSegmentedColoring(
                                    size='small',
                                    min=-10,
                                    max=10,
                                    breakpoints=[0, 1, 2, 3, 4, 5],
                                    colors=["#deecf9", "#71afe5",
                                            "#2b88d8", "#0078d4",
                                            "#106ebe"]
                                ),
                                fac.AntdSegmentedColoring(
                                    size='large',
                                    min=-10,
                                    max=10,
                                    breakpoints=[0, 1, 2, 3, 4, 5],
                                    colors=["#deecf9", "#71afe5",
                                            "#2b88d8", "#0078d4",
                                            "#106ebe"]
                                )
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
        fac.AntdSegmentedColoring(
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=["#deecf9", "#71afe5",
                    "#2b88d8", "#0078d4",
                    "#106ebe"]
        ),
        fac.AntdSegmentedColoring(
            size='small',
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=["#deecf9", "#71afe5",
                    "#2b88d8", "#0078d4",
                    "#106ebe"]
        ),
        fac.AntdSegmentedColoring(
            size='large',
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=["#deecf9", "#71afe5",
                    "#2b88d8", "#0078d4",
                    "#106ebe"]
        )
    ],
    direction='vertical'
)
'''
                            ),
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
                    id='不同的尺寸规格',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdSwitch(
                                        id='segmented-coloring-demo1-bordered',
                                        checked=True
                                    ),
                                    label='bordered'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdSwitch(
                                        id='segmented-coloring-demo1-controls',
                                        checked=True
                                    ),
                                    label='controls'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdSwitch(
                                        id='segmented-coloring-demo1-disabled',
                                        checked=False
                                    ),
                                    label='disabled'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdSwitch(
                                        id='segmented-coloring-demo1-readOnly',
                                        checked=False
                                    ),
                                    label='readOnly'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdSwitch(
                                        id='segmented-coloring-demo1-colorBlockPosition',
                                        checked=True,
                                        checkedChildren='right',
                                        unCheckedChildren='left'
                                    ),
                                    label='colorBlockPosition'
                                )
                            ]
                        ),

                        fac.AntdSegmentedColoring(
                            id='segmented-coloring-demo1',
                            size='small',
                            min=-10,
                            max=10,
                            breakpoints=[0, 1, 2, 3, 4, 5],
                            colors=["#deecf9", "#71afe5",
                                    "#2b88d8", "#0078d4", "#106ebe"]
                        ),

                        fac.AntdDivider(
                            '常用外观类参数',
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
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='segmented-coloring-demo1-bordered',
                checked=True
            ),
            label='bordered'
        ),
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='segmented-coloring-demo1-controls',
                checked=True
            ),
            label='controls'
        ),
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='segmented-coloring-demo1-disabled',
                checked=False
            ),
            label='disabled'
        ),
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='segmented-coloring-demo1-readOnly',
                checked=False
            ),
            label='readOnly'
        ),
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='segmented-coloring-demo1-colorBlockPosition',
                checked=True,
                checkedChildren='right',
                unCheckedChildren='left'
            ),
            label='colorBlockPosition'
        )
    ]
),

fac.AntdSegmentedColoring(
    id='segmented-coloring-demo1',
    size='small',
    min=-10,
    max=10,
    breakpoints=[0, 1, 2, 3, 4, 5],
    colors=["#deecf9", "#71afe5",
            "#2b88d8", "#0078d4", "#106ebe"]
)

...

@app.callback(
    [Output('segmented-coloring-demo1', 'bordered'),
     Output('segmented-coloring-demo1', 'controls'),
     Output('segmented-coloring-demo1', 'disabled'),
     Output('segmented-coloring-demo1', 'readOnly'),
     Output('segmented-coloring-demo1', 'colorBlockPosition')],
    [Input('segmented-coloring-demo1-bordered', 'checked'),
     Input('segmented-coloring-demo1-controls', 'checked'),
     Input('segmented-coloring-demo1-disabled', 'checked'),
     Input('segmented-coloring-demo1-readOnly', 'checked'),
     Input('segmented-coloring-demo1-colorBlockPosition', 'checked')]
)
def segmented_coloring_demo1(*checked_list):
    return [
        *checked_list[:4],
        'right' if checked_list[4] else 'left'
    ]
'''
                            ),
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
                    id='常用外观类参数',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSegmentedColoring(
                            id='segmented-coloring-demo2',
                            size='small',
                            min=-10,
                            max=10,
                            breakpoints=[0, 1, 2, 3, 4, 5],
                            colors=["#deecf9", "#71afe5",
                                    "#2b88d8", "#0078d4",
                                    "#106ebe"]
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('breakpoints: ', strong=True),
                                fac.AntdText(
                                    id='segmented-coloring-demo2-output'
                                )
                            ]
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
fac.AntdSegmentedColoring(
    id='segmented-coloring-demo2',
    size='small',
    min=-10,
    max=10,
    breakpoints=[0, 1, 2, 3, 4, 5],
    colors=["#deecf9", "#71afe5",
            "#2b88d8", "#0078d4",
            "#106ebe"]
),

fac.AntdParagraph(
    [
        fac.AntdText('breakpoints: ', strong=True),
        fac.AntdText(
            id='segmented-coloring-demo2-output'
        )
    ]
)

...

@app.callback(
    Output('segmented-coloring-demo2-output', 'children'),
    Input('segmented-coloring-demo2', 'breakpoints')
)
def segmented_coloring_demo2_callback(breakpoints):
    return str(breakpoints)
'''
                            ),
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
                    {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
                    {'title': '常用外观类参数', 'href': '#常用外观类参数'},
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
            component_name='AntdSegmentedColoring'
        )
    ],
    style={
        'display': 'flex'
    }
)
