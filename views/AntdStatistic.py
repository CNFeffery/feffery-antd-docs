from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdStatistic
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
                                'title': 'AntdStatistic 统计数值'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于构建漂亮的统计数值展示。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdStatistic(
                                        title='数值型统计数值示例',
                                        value=1321321.3213
                                    ),

                                    fac.AntdStatistic(
                                        title='字符型统计数值示例',
                                        value='99.65%'
                                    )
                                ],
                                direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdStatistic(
            title='数值型统计数值示例',
            value=1321321.3213
        ),

        fac.AntdStatistic(
            title='字符型统计数值示例',
            value='99.65%'
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
                        id='基础使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdStatistic(
                                title='数值型统计数值示例',
                                value=1321321.3213,
                                showGroupSeparator=False
                            ),

                            fac.AntdDivider(
                                '隐藏千分位分割符',
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
fac.AntdStatistic(
    title='数值型统计数值示例',
    value=1321321.3213,
    showGroupSeparator=False
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
                        id='隐藏千分位分割符',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdStatistic(
                                title='数值型统计数值示例',
                                value=1321321.3213,
                                precision=2
                            ),

                            fac.AntdDivider(
                                '限制精度',
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
fac.AntdStatistic(
    title='数值型统计数值示例',
    value=1321321.3213,
    precision=2
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
                        id='限制精度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdStatistic(
                                title='数值统计示例',
                                value=98.67,
                                prefix=fac.AntdIcon(
                                    icon='antd-account-book'
                                ),
                                suffix='万元'
                            ),

                            fac.AntdDivider(
                                '添加前后缀',
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
fac.AntdStatistic(
    title='数值统计示例',
    value=98.67,
    prefix=fac.AntdIcon(
        icon='antd-account-book'
    ),
    suffix='万元'
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
                        id='添加前后缀',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdStatistic(
                                title='数值统计示例',
                                value=98.67,
                                titleTooltip='这是信息提示示例'
                            ),

                            fac.AntdDivider(
                                '为标题添加额外信息提示',
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
fac.AntdStatistic(
    title='数值统计示例',
    value=98.67,
    titleTooltip='这是信息提示示例'
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
                        id='为标题添加额外信息提示',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdStatistic(
                                value=fuc.FefferyCountUp(
                                    end=13456.78,
                                    duration=3,
                                    decimals=2
                                ),
                                title='配合数字递增'
                            ),

                            fac.AntdDivider(
                                '配合数字递增组件',
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
import feffery_utils_components as fuc

...

fac.AntdStatistic(
    value=fuc.FefferyCountUp(
        end=13456.78,
        duration=3,
        decimals=2
    ),
    title='配合数字递增'
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
                        id='配合数字递增组件',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdStatistic(
                                id='statistic-demo',
                                precision=2,
                                title='XX股份实时股价',
                                value=675.32,
                                valueStyle={
                                    'color': '#cf1322'
                                },
                                prefix=fac.AntdIcon(
                                    icon='antd-rise'
                                )
                            ),

                            dcc.Interval(
                                id='statistic-interval-demo',
                                n_intervals=0
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
import numpy as np

...

fac.AntdStatistic(
    id='statistic-demo',
    precision=2,
    title='XX股份实时股价',
    value=675.32,
    valueStyle={
        'color': '#cf1322'
    },
    prefix=fac.AntdIcon(
        icon='antd-rise'
    )
),

dcc.Interval(
    id='statistic-interval-demo',
    n_intervals=0
)

...

@app.callback(
    [Output('statistic-demo', 'value'),
     Output('statistic-demo', 'prefix'),
     Output('statistic-demo', 'valueStyle')],
    Input('statistic-interval-demo', 'n_intervals'),
    State('statistic-demo', 'value')
)
def statistic_demo_callback(n_intervals, value):
    new_value = value + np.random.randn()

    if new_value >= value:
        return [
            new_value,
            fac.AntdIcon(
                icon='antd-rise'
            ),
            {
                'color': '#cf1322'
            }
        ]

    else:
        return [
            new_value,
            fac.AntdIcon(
                icon='antd-fall'
            ),
            {
                'color': '#3f8600'
            }
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
                        {'title': '隐藏千分位分割符', 'href': '#隐藏千分位分割符'},
                        {'title': '限制精度', 'href': '#限制精度'},
                        {'title': '添加前后缀', 'href': '#添加前后缀'},
                        {'title': '为标题添加额外信息提示', 'href': '#为标题添加额外信息提示'},
                        {'title': '配合数字递增组件', 'href': '#配合数字递增组件'},
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
                component_name='AntdStatistic',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
