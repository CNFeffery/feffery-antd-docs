from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdSegmented

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdSegmented(id, className, style, *args, **kwargs)',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5'
                    }
                ),

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
                ),

                html.Span(
                    '主要参数说明：',
                    id='主要参数说明',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5',
                        'fontWeight': 'bold',
                        'fontSize': '1.2rem'
                    }
                ),

                fmc.FefferyMarkdown(
                    markdownStr=open('documents/AntdSegmented.md', encoding='utf-8').read()
                ),

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
                        fac.AntdSegmented(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ],
                            defaultValue='选项1'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ],
    defaultValue='选项1'
)'''
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
                        fac.AntdSegmented(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ],
                            defaultValue='选项1',
                            block=True
                        ),

                        fac.AntdDivider(
                            '撑满父容器宽度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ],
    defaultValue='选项1',
    block=True
)'''
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
                    id='撑满父容器宽度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSegmented(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}',
                                    'disabled': i % 2 == 0
                                }
                                for i in range(5)
                            ],
                            defaultValue='选项1'
                        ),

                        fac.AntdDivider(
                            '禁用部分选项',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}',
            'disabled': i % 2 == 0
        }
        for i in range(5)
    ],
    defaultValue='选项1'
)'''
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
                    id='禁用部分选项',
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
                                            'value': f'选项{i}'
                                        }
                                        for i in range(5)
                                    ],
                                    defaultValue='选项1',
                                    size='small'
                                ),
                                fac.AntdSegmented(
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        }
                                        for i in range(5)
                                    ],
                                    defaultValue='选项1'
                                ),
                                fac.AntdSegmented(
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        }
                                        for i in range(5)
                                    ],
                                    defaultValue='选项1',
                                    size='large'
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
                            fuc.FefferySyntaxHighlighter(
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
                    'value': f'选项{i}'
                }
                for i in range(5)
            ],
            defaultValue='选项1',
            size='small'
        ),
        fac.AntdSegmented(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(5)
            ],
            defaultValue='选项1'
        ),
        fac.AntdSegmented(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(5)
            ],
            defaultValue='选项1',
            size='large'
        )
    ],
    direction='vertical'
)'''
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
                        fac.AntdSegmented(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ],
                            id='segmented-demo',
                            defaultValue='选项1'
                        ),

                        fac.AntdSpin(
                            fac.AntdText(
                                id='segmented-demo-output'
                            ),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSegmented(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ],
    id='segmented-demo',
    defaultValue='选项1'
),

fac.AntdSpin(
    fac.AntdText(
        id='segmented-demo-output'
    ),
    text='回调中'
)
...
@app.callback(
    Output('segmented-demo-output', 'children'),
    Input('segmented-demo', 'value')
)
def segmented_callback_demo(value):
    return f'value: {value}'
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
                'flex': 'auto'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '主要参数说明', 'href': '#主要参数说明'},
                    {
                        'title': '使用示例',
                        'href': '#使用示例',
                        'children': [
                            {'title': '基础使用', 'href': '#基础使用'},
                            {'title': '撑满父容器宽度', 'href': '#撑满父容器宽度'},
                            {'title': '禁用部分选项', 'href': '#禁用部分选项'},
                            {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    },
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
