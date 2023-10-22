from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdRadioGroup
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
                                'title': '数据录入'
                            },
                            {
                                'title': 'AntdRadioGroup 单选框'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于供用户在一组选项中进行唯一项选择。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdRadioGroup(
                                options=[
                                    {
                                        'label': f'选项{c}',
                                        'value': c
                                    }
                                    for c in list('abcdef')
                                ],
                                defaultValue='a'
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
    options=[
        {
            'label': f'选项{c}',
            'value': c
        }
        for c in list('abcdef')
    ],
    defaultValue='a'
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
                            fac.AntdRadioGroup(
                                options=[
                                    {
                                        'label': f'选项{c}',
                                        'value': c
                                    }
                                    for c in list('abcdef')
                                ],
                                defaultValue='a',
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '竖直排列',
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
    options=[
        {
            'label': f'选项{c}',
            'value': c
        }
        for c in list('abcdef')
    ],
    defaultValue='a',
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
                        id='竖直排列',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': f'选项{c}',
                                                'value': c
                                            }
                                            for c in list('abcdef')
                                        ],
                                        defaultValue='a',
                                        optionType='button'
                                    ),

                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': f'选项{c}',
                                                'value': c
                                            }
                                            for c in list('abcdef')
                                        ],
                                        defaultValue='a',
                                        optionType='button',
                                        buttonStyle='solid'
                                    )
                                ],
                                direction='vertical'
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
        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='a',
            optionType='button'
        ),

        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='a',
            optionType='button',
            buttonStyle='solid'
        )
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
                        id='按钮模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': f'选项{c}',
                                                'value': c
                                            }
                                            for c in list('abcdef')
                                        ],
                                        defaultValue='a',
                                        disabled=True
                                    ),

                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': f'选项{c}',
                                                'value': c
                                            }
                                            for c in list('abcdef')
                                        ],
                                        defaultValue='a',
                                        optionType='button',
                                        disabled=True
                                    )
                                ],
                                direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='a',
            disabled=True
        ),

        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='a',
            optionType='button',
            disabled=True
        )
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': f'选项{c}',
                                                'value': c
                                            }
                                            for c in list('abcdef')
                                        ],
                                        defaultValue='c',
                                        readOnly=True
                                    ),

                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': f'选项{c}',
                                                'value': c
                                            }
                                            for c in list('abcdef')
                                        ],
                                        defaultValue='c',
                                        optionType='button',
                                        readOnly=True
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '只读状态',
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
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='c',
            readOnly=True
        ),

        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='c',
            optionType='button',
            readOnly=True
        )
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
                        id='只读状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        options=[
                                            {
                                                'label': f'选项{c}',
                                                'value': c
                                            }
                                            for c in list('abcdef')
                                        ],
                                        defaultValue='a',
                                        optionType='button',
                                        size=size
                                    )
                                    for size in [
                                        'small', 'middle', 'large'
                                    ]
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
        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='a',
            optionType='button',
            size=size
        )
        for size in [
            'small', 'middle', 'large'
        ]
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
                            fac.AntdRadioGroup(
                                id='radio-group-demo',
                                options=[
                                    {
                                        'label': f'选项{c}',
                                        'value': c
                                    }
                                    for c in list('abcdef')
                                ],
                                defaultValue='a'
                            ),

                            fac.AntdParagraph(
                                id='radio-group-demo-output'
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
fac.AntdRadioGroup(
    id='radio-group-demo',
    options=[
        {
            'label': f'选项{c}',
            'value': c
        }
        for c in list('abcdef')
    ],
    defaultValue='a'
),

fac.AntdParagraph(
    id='radio-group-demo-output'
)

...

@app.callback(
    Output('radio-group-demo-output', 'children'),
    Input('radio-group-demo', 'value')
)
def radio_group_demo(value):

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
                        {'title': '竖直排列', 'href': '#竖直排列'},
                        {'title': '按钮模式', 'href': '#按钮模式'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '只读状态', 'href': '#只读状态'},
                        {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
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
                component_name='AntdRadioGroup',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
