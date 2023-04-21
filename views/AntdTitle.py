from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

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
                            'title': '通用'
                        },
                        {
                            'title': '排版相关'
                        },
                        {
                            'title': 'AntdTitle 标题'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于渲染具有丰富样式和功能的标题。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdParagraph(
                            [
                                fac.AntdTitle('一级标题', level=1),
                                fac.AntdTitle('二级标题', level=2),
                                fac.AntdTitle('三级标题', level=3),
                                fac.AntdTitle('四级标题', level=4),
                                fac.AntdTitle('五级标题', level=5)
                            ]
                        ),

                        fac.AntdDivider(
                            '不同的标题级别',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('AntdTitle', strong=True),
                                fac.AntdText('拥有'),
                                fac.AntdText('AntdText', strong=True),
                                fac.AntdText('的所有常规渲染模式，参数同样适用，这里就不再赘述，仅展示不同'),
                                fac.AntdText('level', strong=True),
                                fac.AntdText('参数下的效果'),
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
fac.AntdParagraph(
    [
        fac.AntdTitle('一级标题', level=1),
        fac.AntdTitle('二级标题', level=2),
        fac.AntdTitle('三级标题', level=3),
        fac.AntdTitle('四级标题', level=4),
        fac.AntdTitle('五级标题', level=5)
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
                    id='不同的标题级别',
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
                    {'title': '不同的标题级别', 'href': '#不同的标题级别'},
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
            component_name='AntdTitle'
        )
    ],
    style={
        'display': 'flex'
    }
)
