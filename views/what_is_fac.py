from dash import html
from datetime import datetime
import feffery_antd_components as fac
import feffery_utils_components as fuc

from server import app

docs_content = html.Div(
    [
        html.Div(
            [

                fac.AntdBackTop(
                    duration=0.6
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            'feffery-utils-components: Dash实用工具组件库',
                            strong=True,
                            style={'fontSize': '30px'}
                        ),
                        fac.AntdText('🐣', style={'fontSize': '30px'})
                    ],
                    id='🐣'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('文档最近更新：', strong=True),
                        fac.AntdText(datetime.today().strftime(
                            '%Y-%m-%d'), code=True)
                    ]
                ),

                fac.AntdDivider(),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　feffery-utils-components', strong=True),
                        fac.AntdText('（简称'),
                        fac.AntdText('fuc', strong=True),
                        fac.AntdText('），基于'),
                        fac.AntdText('react', strong=True),
                        fac.AntdText('生态，将众多碎片化的实用功能移植封装为简单易用的'),
                        fac.AntdText('Dash', strong=True),
                        fac.AntdText('组件，从而辅助构建更强大的应用。'),
                    ]
                ),

                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url('imgs/fuc-logo.svg'),
                            style={'height': '300px'}
                        )
                    ],
                    style={
                        'textAlign': 'center'
                    }
                ),

                fac.AntdDivider(),

                fac.AntdParagraph(
                    [
                        fac.AntdText('🤩', style={'fontSize': '26px'}),
                        fac.AntdText('特性',
                                     strong=True,
                                     style={'fontSize': '26px'}),
                    ],
                    id='特性'
                ),

                html.Ul(
                    [
                        html.Li('💪 功能丰富，涉及日常应用开发所需的方方面面',
                                style={'listStyleType': 'circle'}),
                        html.Li('😋 使用简单，功能参数直观明了',
                                style={'listStyleType': 'circle'}),
                        html.Li('⚡ 迭代迅速，持续维护更新组件功能',
                                style={'listStyleType': 'circle'})
                    ]
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('🛫', style={'fontSize': '26px'}),
                        fac.AntdText('版本',
                                     strong=True,
                                     style={'fontSize': '26px'}),
                    ],
                    id='版本'
                ),

                html.Ul(
                    [
                        html.Li(
                            fac.AntdParagraph(
                                [
                                    fac.AntdText('pypi最新稳定版本：'),
                                    fac.AntdTag(content=fuc.__version__),
                                    html.Img(
                                        src='https://img.shields.io/pypi/v/feffery-utils-components.svg?color=dark-green',
                                        style={
                                            'height': '19px',
                                            'transform': 'translateY(-1px)'
                                        }
                                    )
                                ]
                            ),
                            style={'listStyleType': 'circle'}
                        )
                    ]
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('📦', style={'fontSize': '26px'}),
                        fac.AntdText('安装',
                                     strong=True,
                                     style={'fontSize': '26px'}),
                    ],
                    id='安装'
                ),

                fac.AntdTitle('最新稳定版本：', level=5),

                fac.AntdText(
                    f'pip install feffery-utils-components=={fuc.__version__}',
                    keyboard=True,
                    copyable=True
                ),

                fac.AntdTitle('最新开发版本：', level=5),

                fac.AntdText(
                    'pip install git+https://github.com/CNFeffery/feffery-utils-components.git',
                    keyboard=True,
                    copyable=True
                ),

                html.Br(),

                fac.AntdText('国内github镜像加速下载方式：'),

                html.Br(),

                fac.AntdText(
                    'pip install git+https://github.91chi.fun/https://github.com/CNFeffery/feffery-utils-components.git',
                    keyboard=True,
                    copyable=True
                ),

                fac.AntdDivider(),

                fac.AntdParagraph(
                    [
                        fac.AntdText('🎩', style={'fontSize': '26px'}),
                        fac.AntdText('加入交流群',
                                     strong=True,
                                     style={'fontSize': '26px'}),
                    ],
                    id='加入交流群'
                ),

                fac.AntdCollapse(
                    html.Div(
                        fac.AntdImage(
                            src=app.get_asset_url('imgs/feffery-添加好友二维码.jpg'),
                            style={
                                'width': '300px',
                                'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                'borderRadius': '5px'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center'
                        }
                    ),
                    title='微信扫码加我好友，备注【dash学习】',
                    is_open=True,
                    ghost=True
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('👉', style={'fontSize': '26px'}),
                        fac.AntdText('玩转dash公众号',
                                     strong=True,
                                     style={'fontSize': '26px'}),
                    ],
                    id='玩转dash公众号'
                ),

                fac.AntdCollapse(
                    html.Div(
                        fac.AntdImage(
                            src=app.get_asset_url('imgs/玩转dash公众号.jpg'),
                            style={
                                'height': '300px',
                                'width': '300px',
                                'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                'borderRadius': '5px'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center'
                        }
                    ),
                    title='扫码关注我的知识分享公众号【玩转dash】',
                    is_open=True,
                    ghost=True
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('🌏', style={'fontSize': '26px'}),
                        fac.AntdText('玩转dash知识星球',
                                     strong=True,
                                     style={'fontSize': '26px'}),
                    ],
                    id='玩转dash知识星球'
                ),

                fac.AntdCollapse(
                    html.Div(
                        fac.AntdImage(
                            src=app.get_asset_url('imgs/玩转dash星球二维码.jpg'),
                            style={
                                'width': '300px',
                                'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                'borderRadius': '5px'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center'
                        }
                    ),
                    title='更多高级知识及案例欢迎加入知识星球【玩转dash】',
                    is_open=True,
                    ghost=True
                ),

                html.Div(
                    style={
                        'height': '200px'
                    }
                )

            ],
            style={
                'flex': 'auto'
            }
        ),

        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '🐣简介', 'href': '#🐣'},
                    {'title': '🤩特性', 'href': '#特性'},
                    {'title': '🛫版本', 'href': '#版本'},
                    {'title': '📦安装', 'href': '#安装'},
                    {'title': '🎩加入交流群', 'href': '#加入交流群'},
                    {'title': '👉玩转dash公众号', 'href': '#玩转dash公众号'},
                    {'title': '🌏玩转dash知识星球', 'href': '#玩转dash知识星球'}
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none'
            }
        )
    ],
    style={
        'display': 'flex',
        'padding': '25px'
    }
)
