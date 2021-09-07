import dash_html_components as html
import feffery_antd_components as fac

from server import app

docs_content = html.Div(
    [
        fac.AntdTitle('feffery-antd-components: Ant Design在Dash中的最佳实现', level=2),

        fac.AntdParagraph(
            [
                fac.AntdText('　　feffery-antd-components', strong=True),
                fac.AntdText('（简称'),
                fac.AntdText('fac', strong=True),
                fac.AntdText('），基于著名的React UI组件库'),
                fac.AntdText('antd', strong=True),
                fac.AntdText('进行二次开发，将'),
                fac.AntdText('antd', strong=True),
                fac.AntdText('中的诸多实用组件及特性引入'),
                fac.AntdText('Dash', italic=True),
                fac.AntdText('，开发者使用'),
                fac.AntdText('极低', strong=True),
                fac.AntdText('的纯'),
                fac.AntdText('Python', strong=True),
                fac.AntdText('代码量，即可快速开发出现代化的web应用，将你有关web应用的创意想法✨高效地实现。'),
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
                    style={'height': '150px'}
                ),
                fac.AntdText(
                    '=',
                    style={'fontSize': '30px', 'color': 'rgba(170, 170, 170, 1)', 'padding': '0 15px 0 15px'}
                ),
                html.Img(
                    src=app.get_asset_url('imgs/feffery-antd-components-logo-planB.svg'),
                    style={'height': '190px'}
                )
            ],
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        ),

        fac.AntdDivider(),

        fac.AntdTitle('🤩特性', level=3),

        html.Ul(
            [
                html.Li('🎁 功能丰富，在antd的基础上设计出更多增广功能', style={'listStyleType': 'circle'}),
                html.Li('😋 使用简单，开发者上手难度低，无需javascript代码即可实现复杂交互', style={'listStyleType': 'circle'}),
                html.Li('💎 文档详实，针对每个组件的主要功能及用法予以丰富案例介绍', style={'listStyleType': 'circle'})
            ]
        ),

        fac.AntdTitle('版本', level=3),

        html.Ul(
            [
                html.Li(
                    fac.AntdParagraph(
                        [
                            fac.AntdText('pypi最新稳定版本：'),
                            fac.AntdTag(content='0.0.1rc2'),
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

        fac.AntdTitle('安装', level=3),

        fac.AntdTitle('最新稳定版本：', level=5),

        fac.AntdText('pip install feffery-antd-components==0.0.1rc2', keyboard=True),

        fac.AntdTitle('最新开发版本：', level=5),

        fac.AntdText('pip install git+https://github.com/CNFeffery/feffery-antd-components.git', keyboard=True),

        html.Br(),

        fac.AntdText('国内github镜像加速下载方式：'),

        html.Br(),

        fac.AntdText('pip install git+https://hub.fastgit.org/CNFeffery/feffery-antd-components.git', keyboard=True),

        fac.AntdTitle('赞助支持', level=3),

        fac.AntdParagraph(
            [
                fac.AntdText('　　fac', strong=True),
                fac.AntdText(
                    '是我为了方便日常工作需要而在业余时间渐渐开发出的开源项目，'
                    '它给予了我很多工作上的便捷，帮助我完成了很多以前难以实现的想法，'
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
                fac.AntdText('过去已做出以及未来将要做出的贡献，可以点击下方“显示赞助二维码”随意赞助，感谢支持。')
            ]
        ),

        fac.AntdCollapse(
            html.Div(
                html.Img(
                    src=app.get_asset_url('imgs/weixin-pay.png'),
                    style={
                        'height': '350px'
                    }
                ),
                style={
                    'display': 'flex',
                    'justifyContent': 'center'
                }
            ),
            title='显示赞助二维码',
            is_open=False,
            ghost=True
        ),

        html.Div(
            style={
                'height': '200px'
            }
        )

    ]
)
