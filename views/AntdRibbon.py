from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

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
                                'title': 'AntdRibbon 缎带'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为容器类元素添加点缀作用的缎带。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRibbon(
                                        fuc.FefferyDiv(
                                            shadow='always-shadow',
                                            style={
                                                'height': '200px',
                                                'width': '300px',
                                                'borderRadius': '10px'
                                            }
                                        ),
                                        text='缎带示例'
                                    ),
                                    fac.AntdRibbon(
                                        fuc.FefferyDiv(
                                            shadow='always-shadow',
                                            style={
                                                'height': '200px',
                                                'width': '300px',
                                                'borderRadius': '10px'
                                            }
                                        ),
                                        text='缎带示例',
                                        placement='start',
                                        color='#ff4d4f'
                                    )
                                ],
                                direction='vertical',
                                size='large'
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
        fac.AntdRibbon(
            fuc.FefferyDiv(
                shadow='always-shadow',
                style={
                    'height': '200px',
                    'width': '300px',
                    'borderRadius': '10px'
                }
            ),
            text='缎带示例'
        ),
        fac.AntdRibbon(
            fuc.FefferyDiv(
                shadow='always-shadow',
                style={
                    'height': '200px',
                    'width': '300px',
                    'borderRadius': '10px'
                }
            ),
            text='缎带示例',
            placement='start',
            color='#ff4d4f'
        )
    ],
    direction='vertical',
    size='large'
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
                component_name='AntdRibbon',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
