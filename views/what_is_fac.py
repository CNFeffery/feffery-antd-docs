from dash import html
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Component

from server import app

# 国际化
from i18n import translator, get_current_locale

latest_deploy_datetime = datetime.today().strftime('%Y-%m-%d')


def render() -> Component:
    """渲染“fac是什么”文档页"""

    current_locale = get_current_locale()

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(),
                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                translator.t(
                                    'feffery-antd-components: Ant Design在Dash中的最佳实现'
                                ),
                                strong=True,
                                style={'fontSize': '30px'},
                            ),
                            fac.AntdText('🐣', style={'fontSize': '30px'}),
                        ],
                        id='🐣',
                    ),
                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                translator.t('文档最近更新：'), strong=True
                            ),
                            fac.AntdText(latest_deploy_datetime, code=True),
                        ]
                    ),
                    fac.AntdDivider(),
                    fac.AntdParagraph(
                        (
                            [
                                fac.AntdText(
                                    '　　feffery-antd-components', strong=True
                                ),
                                fac.AntdText('（简称'),
                                fac.AntdText('fac', strong=True),
                                fac.AntdText('），基于著名的React UI组件库'),
                                fac.AntdText('ant design', strong=True),
                                fac.AntdText('进行大量二次开发，将'),
                                fac.AntdText('ant design', strong=True),
                                fac.AntdText('中的诸多实用组件及特性引入'),
                                fac.AntdText('Dash', italic=True),
                                fac.AntdText('，帮助开发者纯'),
                                fac.AntdText('Python', strong=True),
                                fac.AntdText(
                                    '构建现代化高质量且任意复杂程度的交互式web应用，帮助你将有关web应用的美好憧憬✨高效地实现。'
                                ),
                            ]
                            if current_locale == 'zh-cn'
                            else 'feffery-antd-components (fac), based on the famous React UI component library ant design, carries out a large number of secondary development, and introduces many practical components and features from ant design into Dash. Help developers build modern, high-quality and interactive web applications of any complexity in pure Python, and help you to realize the beautiful vision of web applications ✨ efficiently.'
                        )
                    ),
                    html.Div(
                        [
                            html.Img(
                                src=app.get_asset_url(
                                    'imgs/index/react-logo.svg'
                                ),
                                style={'height': '150px'},
                            ),
                            fac.AntdText(
                                '+',
                                style={
                                    'fontSize': '30px',
                                    'color': 'rgba(170, 170, 170, 1)',
                                    'padding': '0 15px 0 15px',
                                },
                            ),
                            html.Img(
                                src=app.get_asset_url(
                                    'imgs/index/antd-logo.svg'
                                ),
                                style={'height': '150px'},
                            ),
                            fac.AntdText(
                                '+',
                                style={
                                    'fontSize': '30px',
                                    'color': 'rgba(170, 170, 170, 1)',
                                    'padding': '0 15px 0 15px',
                                },
                            ),
                            html.Img(
                                src=app.get_asset_url(
                                    'imgs/index/dash-logo.png'
                                ),
                                style={'height': '140px'},
                            ),
                            fac.AntdText(
                                '=',
                                style={
                                    'fontSize': '30px',
                                    'color': 'rgba(170, 170, 170, 1)',
                                    'padding': '0 15px 0 15px',
                                },
                            ),
                            html.Img(
                                src=app.get_asset_url('imgs/fac-logo.svg'),
                                style={'height': '155px'},
                            ),
                        ],
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'paddingTop': 25,
                            'paddingBottom': 25,
                        },
                    ),
                    fac.AntdDivider(),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('🤩', style={'fontSize': '26px'}),
                            fac.AntdText(
                                translator.t('特性'),
                                strong=True,
                                style={'fontSize': '26px'},
                            ),
                        ],
                        id=translator.t('特性'),
                    ),
                    fac.AntdRow(
                        [
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/Python.svg',
                                                        style={
                                                            'height': '3rem',
                                                            'transform': 'translateY(12px)',
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '纯Python开发'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        translator.t(
                                                            '基于Dash框架，只需编写Python\n即可完成企业级应用开发全过程'
                                                        ),
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/MBE风格多色图标-组件.svg',
                                                        style={
                                                            'height': '4rem'
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '组件种类齐全'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        translator.t(
                                                            '内置上百种网页功能组件\n满足通用场景需求'
                                                        ),
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/表格.svg',
                                                        style={
                                                            'height': '2.5rem',
                                                            'transform': 'translateY(15px)',
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '丰富的表格功能'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        [
                                                            translator.t(
                                                                '内置功能强大的表格组件'
                                                            ),
                                                            html.A(
                                                                'AntdTable',
                                                                href='/AntdTable-basic',
                                                                target='_blank',
                                                            ),
                                                            translator.t(
                                                                '\n充分展示交互表格数据'
                                                            ),
                                                        ],
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/结构树.svg',
                                                        style={
                                                            'height': '2.5rem',
                                                            'transform': 'translateY(15px)',
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '强大的树形控件'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        [
                                                            translator.t(
                                                                '内置功能强大的树形控件'
                                                            ),
                                                            html.A(
                                                                'AntdTree',
                                                                href='/AntdTree',
                                                                target='_blank',
                                                            ),
                                                            translator.t(
                                                                '\n树形结构交互展示能力拉满'
                                                            ),
                                                        ],
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/MBE风格多色图标-时间.svg',
                                                        style={
                                                            'height': '4rem'
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '实用的日期选择器'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        [
                                                            translator.t(
                                                                '内置日期及日期范围选择组件\n'
                                                            ),
                                                            html.A(
                                                                'AntdDatePicker',
                                                                href='/AntdDatePicker',
                                                                target='_blank',
                                                            ),
                                                            translator.t('、'),
                                                            html.A(
                                                                'AntdDateRangePicker',
                                                                href='/AntdDateRangePicker',
                                                                target='_blank',
                                                            ),
                                                            translator.t(
                                                                '\n可灵活配置使用策略'
                                                            ),
                                                        ],
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/MBE风格多色图标-文档.svg',
                                                        style={
                                                            'height': '4rem'
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '便捷的表单功能'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        [
                                                            translator.t(
                                                                '基于内置表单整合组件\n'
                                                            ),
                                                            html.A(
                                                                'AntdForm',
                                                                href='/AntdForm',
                                                                target='_blank',
                                                            ),
                                                            translator.t('、'),
                                                            html.A(
                                                                'AntdFormItem',
                                                                href='/AntdFormItem',
                                                                target='_blank',
                                                            ),
                                                            translator.t(
                                                                '\n轻松构建整张表单'
                                                            ),
                                                        ],
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/翻译.svg',
                                                        style={
                                                            'height': '4rem'
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '支持中英双语言'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        translator.t(
                                                            '内置各组件文案信息支持在\n简体中文与英文之间进行设置切换'
                                                        ),
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                            fac.AntdCol(
                                html.Div(
                                    [
                                        fac.AntdSpace(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src='assets/imgs/index/应用.svg',
                                                        style={
                                                            'height': '3rem',
                                                            'transform': 'translateY(10px)',
                                                        },
                                                    ),
                                                    style={'height': '4rem'},
                                                ),
                                                fac.AntdText(
                                                    translator.t(
                                                        '联动更多组件库'
                                                    ),
                                                    style={
                                                        'fontSize': 20,
                                                        'whiteSpace': 'nowrap',
                                                    },
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        [
                                                            translator.t(
                                                                '高效联动feffery-components生态中\n'
                                                            ),
                                                            html.A(
                                                                'fuc',
                                                                href='https://fuc.feffery.tech/',
                                                                target='_blank',
                                                            ),
                                                            translator.t('、'),
                                                            html.A(
                                                                'fmc',
                                                                href='https://fmc.feffery.tech/',
                                                                target='_blank',
                                                            ),
                                                            translator.t(
                                                                '等组件库，实现更多功能'
                                                            ),
                                                        ],
                                                        style={
                                                            'color': '#697b8c',
                                                            'whiteSpace': 'pre',
                                                        },
                                                    ),
                                                    style={
                                                        'textAlign': 'center'
                                                    },
                                                ),
                                            ],
                                            direction='vertical',
                                            align='center',
                                            style={'width': 175},
                                        )
                                    ],
                                    className='hover-shadow-box',
                                    style={
                                        'height': 220,
                                        'borderRadius': 6,
                                        'position': 'relative',
                                        'display': 'flex',
                                        'alignItems': 'center',
                                        'justifyContent': 'center',
                                    },
                                ),
                                xs=24,
                                sm=24,
                                md=12,
                                lg=12,
                                xl=12,
                                xxl=6,
                            ),
                        ],
                        gutter=[25, 25],
                        style={'padding': '75px 0'},
                    ),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('🛫', style={'fontSize': '26px'}),
                            fac.AntdText(
                                translator.t('版本'),
                                strong=True,
                                style={'fontSize': '26px'},
                            ),
                        ],
                        id=translator.t('版本'),
                    ),
                    html.Ul(
                        [
                            html.Li(
                                fac.AntdParagraph(
                                    [
                                        fac.AntdText(
                                            translator.t('pypi最新稳定版本：')
                                        ),
                                        fac.AntdTag(content=fac.__version__),
                                        html.Img(
                                            src='https://img.shields.io/pypi/v/feffery-antd-components.svg?color=dark-green',
                                            style={
                                                'height': 20,
                                                'transform': 'translateY(5px)',
                                            },
                                        ),
                                    ]
                                ),
                                style={'listStyleType': 'circle'},
                            )
                        ]
                    ),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('📦', style={'fontSize': '26px'}),
                            fac.AntdText(
                                translator.t('安装'),
                                strong=True,
                                style={'fontSize': '26px'},
                            ),
                        ],
                        id=translator.t('安装'),
                    ),
                    fac.AntdTitle(translator.t('最新稳定版本：'), level=5),
                    fac.AntdText(
                        f'pip install feffery-antd-components=={fac.__version__}',
                        keyboard=True,
                        copyable=True,
                    ),
                    fac.AntdTitle(translator.t('最新预发布版本：'), level=5),
                    fac.AntdText(
                        'pip install feffery-antd-components --pre -U',
                        keyboard=True,
                        copyable=True,
                    ),
                    *(
                        [
                            fac.AntdDivider(),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '🎩', style={'fontSize': '26px'}
                                    ),
                                    fac.AntdText(
                                        '加入交流群',
                                        strong=True,
                                        style={'fontSize': '26px'},
                                    ),
                                ],
                                id='加入交流群',
                            ),
                            fac.AntdCollapse(
                                html.Div(
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/index/feffery-添加好友二维码.jpg'
                                        ),
                                        style={
                                            'width': '300px',
                                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                            'borderRadius': '5px',
                                        },
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                    },
                                ),
                                title='微信扫码添加好友，备注【dash学习】',
                                isOpen=True,
                                ghost=True,
                            ),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '👉', style={'fontSize': '26px'}
                                    ),
                                    fac.AntdText(
                                        '玩转dash公众号',
                                        strong=True,
                                        style={'fontSize': '26px'},
                                    ),
                                ],
                                id='玩转dash公众号',
                            ),
                            fac.AntdCollapse(
                                html.Div(
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/index/玩转dash公众号.png'
                                        ),
                                        style={
                                            'height': '300px',
                                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                            'borderRadius': '5px',
                                        },
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                    },
                                ),
                                title='扫码关注我的知识分享公众号【玩转dash】',
                                isOpen=True,
                                ghost=True,
                            ),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '🌏', style={'fontSize': '26px'}
                                    ),
                                    fac.AntdText(
                                        '玩转dash知识星球',
                                        strong=True,
                                        style={'fontSize': '26px'},
                                    ),
                                ],
                                id='玩转dash知识星球',
                            ),
                            fac.AntdCollapse(
                                html.Div(
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/index/玩转dash星球二维码.jpg'
                                        ),
                                        style={
                                            'width': '300px',
                                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                            'borderRadius': '5px',
                                        },
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                    },
                                ),
                                title='更多dash高级知识技巧及海量应用案例模板，欢迎加入我的知识星球【玩转dash】',
                                isOpen=True,
                                ghost=True,
                            ),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '💪', style={'fontSize': '26px'}
                                    ),
                                    fac.AntdText(
                                        '赞助支持',
                                        strong=True,
                                        style={'fontSize': '26px'},
                                    ),
                                ],
                                id='赞助支持',
                            ),
                            fac.AntdParagraph(
                                [
                                    fac.AntdText('　　fac', strong=True),
                                    fac.AntdText(
                                        '是我为了方便日常工作需要，逐渐积累优化从而开发并开源出的一个完整的框架，'
                                        '它给予了我很多工作上的便捷，帮助我完成了很多以前无法实现，或实现起来较麻烦的功能和想法，'
                                        '希望也可以帮助到你。'
                                    ),
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
                                    fac.AntdText(
                                        '过去已做出以及未来将要做出的贡献，可以微信扫一扫下方“赞助二维码”随意赞助，感谢支持。'
                                    ),
                                ]
                            ),
                            fac.AntdCollapse(
                                html.Div(
                                    fac.AntdImage(
                                        src=app.get_asset_url(
                                            'imgs/index/weixin-pay.png'
                                        ),
                                        style={
                                            'width': '300px',
                                            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                            'borderRadius': '5px',
                                        },
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                    },
                                ),
                                title='赞助二维码',
                                isOpen=True,
                                ghost=True,
                            ),
                        ]
                        if current_locale == 'zh-cn'
                        else []
                    ),
                    html.Div(style={'height': '200px'}),
                ],
                style={'flex': 'auto'},
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': '🐣' + translator.t('简介'), 'href': '#🐣'},
                        {
                            'title': '🤩' + translator.t('特性'),
                            'href': '#' + translator.t('特性'),
                        },
                        {
                            'title': '🛫' + translator.t('版本'),
                            'href': '#' + translator.t('版本'),
                        },
                        {
                            'title': '📦' + translator.t('安装'),
                            'href': '#' + translator.t('安装'),
                        },
                        *(
                            [
                                {
                                    'title': '🎩加入交流群',
                                    'href': '#加入交流群',
                                },
                                {
                                    'title': '👉玩转dash公众号',
                                    'href': '#玩转dash公众号',
                                },
                                {
                                    'title': '🌏玩转dash知识星球',
                                    'href': '#玩转dash知识星球',
                                },
                                {'title': '💪赞助支持', 'href': '#赞助支持'},
                            ]
                            if current_locale == 'zh-cn'
                            else []
                        ),
                    ],
                    offsetTop=65,
                ),
                style={'flex': 'none'},
            ),
        ],
        style={'display': 'flex', 'padding': 25},
    )
