import re
from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac
from dash.dependencies import Input, Output

from config import Config
from server import app

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdIcon(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdIcon.md', encoding='utf-8').read()
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

                        fac.AntdRadioGroup(
                            id='icon-category',
                            options=[
                                {
                                    'label': 'Antd Design精选',
                                    'value': 'antd'
                                },
                                {
                                    'label': 'Material Design精选',
                                    'value': 'md'
                                },
                                {
                                    'label': 'Flat Color精选',
                                    'value': 'fc'
                                },
                                {
                                    'label': 'Devicons精选',
                                    'value': 'di'
                                },
                                {
                                    'label': 'BoxIcons精选',
                                    'value': 'bi'
                                },
                                {
                                    'label': 'Bootstrap精选',
                                    'value': 'bs'
                                },
                                {
                                    'label': 'Game Icons精选',
                                    'value': 'gi'
                                }
                            ],
                            optionType='button',
                            defaultValue='antd'
                        ),

                        fac.AntdSpin(
                            fac.AntdRow(
                                id='icon-demo',
                                style={
                                    'minHeight': '50px'
                                }
                            )
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdIcon', strong=True),
                                fac.AntdText('可配合'),
                                fac.AntdText('AntdButton', strong=True),
                                fac.AntdText('、'),
                                fac.AntdText('AntdMenu', strong=True),
                                fac.AntdText('等组件使用，阅读相关文档时请留意对应图标使用示例')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdRadioGroup(
    id='icon-category',
    options=[
        {
            'label': 'Antd Design精选',
            'value': 'antd'
        },
        {
            'label': 'Material Design精选',
            'value': 'md'
        },
        {
            'label': 'Flat Color精选',
            'value': 'fc'
        },
        {
            'label': 'Devicons精选',
            'value': 'di'
        },
        {
            'label': 'BoxIcons精选',
            'value': 'bi'
        },
        {
            'label': 'Bootstrap精选',
            'value': 'bs'
        },
        {
            'label': 'Game Icons精选',
            'value': 'gi'
        }
    ],
    optionType='button',
    defaultValue='antd'
),

fac.AntdSpin(
    fac.AntdRow(
        id='icon-demo',
        style={
            'minHeight': '50px'
        }
    )
)
...
@app.callback(
    Output('icon-demo', 'children'),
    Input('icon-category', 'value')
)
def icon_demo_render_callback(value):
    # 注：Config.all_icons来自config.py
    if value == 'antd':
        return [
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdIcon(
                            icon=icon,
                            style={
                                'fontSize': '28px',
                                'marginRight': '5px'
                            }
                        ),
                        fac.AntdText(
                            icon,
                            copyable=True
                        )
                    ]
                ),
                span=6
            )
            for icon in Config.all_icons if re.findall('^md|^fc|^di|^bi|^bs|^gi', icon) == []
        ]

    else:

        return [
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdIcon(
                            icon=icon,
                            style={
                                'fontSize': '28px',
                                'marginRight': '5px'
                            }
                        ),
                        fac.AntdText(
                            icon,
                            copyable=True
                        )
                    ]
                ),
                span=6
            )
            for icon in Config.all_icons if re.findall(f'^{value}', icon) == [value]
        ]
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
                            {'title': '基础使用', 'href': '#基础使用'}
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
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


@app.callback(
    Output('icon-demo', 'children'),
    Input('icon-category', 'value')
)
def icon_demo_render_callback(value):
    if value == 'antd':
        return [
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdIcon(
                            icon=icon,
                            style={
                                'fontSize': '28px',
                                'marginRight': '5px'
                            }
                        ),
                        fac.AntdText(
                            icon,
                            copyable=True
                        )
                    ]
                ),
                span=6
            )
            for icon in Config.all_icons if re.findall('^md|^fc|^di|^bi|^bs|^gi', icon) == []
        ]

    else:

        return [
            fac.AntdCol(
                html.Div(
                    [
                        fac.AntdIcon(
                            icon=icon,
                            style={
                                'fontSize': '28px',
                                'marginRight': '5px'
                            }
                        ),
                        fac.AntdText(
                            icon,
                            copyable=True
                        )
                    ]
                ),
                span=6
            )
            for icon in Config.all_icons if re.findall(f'^{value}', icon) == [value]
        ]
