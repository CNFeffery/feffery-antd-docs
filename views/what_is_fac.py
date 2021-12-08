from dash import html
import feffery_antd_components as fac

from server import app

docs_content = html.Div(
    [
        html.Div(
            [

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('feffery-antd-components: Ant Design在Dash中的最佳实现',
                                     strong=True,
                                     style={'fontSize': '30px'}),
                        fac.AntdText('🐣', style={'fontSize': '30px'})
                    ],
                    id='🐣'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　feffery-antd-components', strong=True),
                        fac.AntdText('（简称'),
                        fac.AntdText('fac', strong=True),
                        fac.AntdText('），基于著名的React UI组件库'),
                        fac.AntdText('ant design', strong=True),
                        fac.AntdText('进行二次开发，将'),
                        fac.AntdText('ant design', strong=True),
                        fac.AntdText('中的诸多实用组件及特性引入'),
                        fac.AntdText('Dash', italic=True),
                        fac.AntdText('，帮助开发者使用'),
                        fac.AntdText('极低', strong=True),
                        fac.AntdText('的纯'),
                        fac.AntdText('Python', strong=True),
                        fac.AntdText('代码量，即可快速开发出现代化的交互式web应用，将你有关web应用的美好憧憬✨高效地实现。'),
                    ]
                ),

                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url('imgs/react-logo.svg'),
                            style={'height': '150px'}
                        ),
                        fac.AntdText(
                            '+',
                            style={'fontSize': '30px', 'color': 'rgba(170, 170, 170, 1)', 'padding': '0 15px 0 15px'}
                        ),
                        html.Img(
                            src=app.get_asset_url('imgs/antd-logo.svg'),
                            style={'height': '150px'}
                        ),
                        fac.AntdText(
                            '+',
                            style={'fontSize': '30px', 'color': 'rgba(170, 170, 170, 1)', 'padding': '0 15px 0 15px'}
                        ),
                        html.Img(
                            src=app.get_asset_url('imgs/dash-logo.png'),
                            style={'height': '140px'}
                        ),
                        fac.AntdText(
                            '=',
                            style={'fontSize': '30px', 'color': 'rgba(170, 170, 170, 1)', 'padding': '0 15px 0 15px'}
                        ),
                        html.Img(
                            src=app.get_asset_url('imgs/feffery-antd-components-logo-planB.svg'),
                            style={'height': '180px'}
                        )
                    ],
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
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
                        html.Li('🎁 功能丰富，在antd的基础上设计出更多增广功能', style={'listStyleType': 'circle'}),
                        html.Li('😋 使用简单，开发者上手难度低，无需javascript代码即可实现复杂交互', style={'listStyleType': 'circle'}),
                        html.Li('💎 文档详实，针对每个组件的主要功能及用法予以丰富案例介绍', style={'listStyleType': 'circle'})
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
                                    fac.AntdTag(content='0.0.1rc7'),
                                    html.Img(
                                        src='https://img.shields.io/pypi/v/feffery-antd-components.svg?color=dark-green',
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

                fac.AntdText('pip install feffery-antd-components==0.0.1rc7', keyboard=True, copyable=True),

                fac.AntdTitle('最新开发版本：', level=5),

                fac.AntdText('pip install git+https://github.com/CNFeffery/feffery-antd-components.git',
                             keyboard=True,
                             copyable=True),

                html.Br(),

                fac.AntdText('国内github镜像加速下载方式：'),

                html.Br(),

                fac.AntdText('pip install git+https://hub.fastgit.org/CNFeffery/feffery-antd-components.git',
                             keyboard=True,
                             copyable=True),

                fac.AntdDivider(),

                fac.AntdParagraph(
                    [
                        fac.AntdText('💪', style={'fontSize': '26px'}),
                        fac.AntdText('赞助支持',
                                     strong=True,
                                     style={'fontSize': '26px'}),
                    ],
                    id='赞助支持'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　fac', strong=True),
                        fac.AntdText(
                            '是我为了方便日常工作需要，逐渐积累优化从而开发并开源出的一个完整的框架，'
                            '它给予了我很多工作上的便捷，帮助我完成了很多以前无法实现，或实现起来较麻烦的功能和想法，'
                            '希望也可以帮助到你。'
                        )
                    ]
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　作为一个开源项目，'
                            '任何人都可以以任何形式，免费使用它，来打造你心中理想的'
                            'web应用，如果你有意愿为我分担有关服务器等开销，亦或是赞助鼓励我对于'
                        ),
                        fac.AntdText('fac', strong=True),
                        fac.AntdText('过去已做出以及未来将要做出的贡献，可以微信扫一扫下方“赞助二维码”随意赞助，感谢支持。')
                    ]
                ),

                fac.AntdCollapse(
                    html.Div(
                        html.Img(
                            src=app.get_asset_url('imgs/weixin-pay.png'),
                            style={
                                'height': '400px'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'justifyContent': 'center'
                        }
                    ),
                    title='赞助二维码',
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
                    {'title': '💪赞助支持', 'href': '#赞助支持'},
                ],
                containerId='docs-content',
                targetOffset=200,
                align='left'
            ),
            style={
                'flex': 'none',
                'margin': '20px',
                'width': '120px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
