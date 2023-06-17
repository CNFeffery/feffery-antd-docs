from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdCustomSkeleton
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
                                'title': '反馈'
                            },
                            {
                                'title': '自定义骨骼屏'
                            },
                            {
                                'title': 'AntdCustomSkeleton 自定义骨骼屏'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于自由设计骨骼屏加载中内容。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '触发2秒自定义骨骼屏动画',
                                        id='skeleton-custom-demo-input',
                                        type='primary'
                                    ),

                                    fac.AntdCustomSkeleton(
                                        id='custom-skeleton-demo',
                                        skeletonContent=html.Div(
                                            [
                                                fac.AntdRow(
                                                    [
                                                        fac.AntdCol(
                                                            fac.AntdSkeletonButton(
                                                                block=True,
                                                                active=True
                                                            ),
                                                            span=6,
                                                            style={
                                                                'padding': '4px'
                                                            }
                                                        )
                                                    ] * 16
                                                ),
                                                fac.AntdSpace(
                                                    [
                                                        html.Div(
                                                            fac.AntdSkeletonButton(
                                                                active=True,
                                                                size='small',
                                                                block=True
                                                            ),
                                                            style={
                                                                'width': '80px'
                                                            }
                                                        ),
                                                        html.Div(
                                                            fac.AntdSkeletonButton(
                                                                active=True,
                                                                size='small',
                                                                block=True
                                                            ),
                                                            style={
                                                                'width': '60px'
                                                            }
                                                        )
                                                    ],
                                                    style={
                                                        'float': 'right',
                                                        'paddingRight': '4px',
                                                        'paddingTop': '15px'
                                                    }
                                                )
                                            ]
                                        )
                                    ),
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
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
        fac.AntdButton(
            '触发2秒自定义骨骼屏动画',
            id='skeleton-custom-demo-input',
            type='primary'
        ),

        fac.AntdCustomSkeleton(
            id='custom-skeleton-demo',
            skeletonContent=html.Div(
                [
                    fac.AntdRow(
                        [
                            fac.AntdCol(
                                fac.AntdSkeletonButton(
                                    block=True,
                                    active=True
                                ),
                                span=6,
                                style={
                                    'padding': '4px'
                                }
                            )
                        ] * 16
                    ),
                    fac.AntdSpace(
                        [
                            html.Div(
                                fac.AntdSkeletonButton(
                                    active=True,
                                    size='small',
                                    block=True
                                ),
                                style={
                                    'width': '80px'
                                }
                            ),
                            html.Div(
                                fac.AntdSkeletonButton(
                                    active=True,
                                    size='small',
                                    block=True
                                ),
                                style={
                                    'width': '60px'
                                }
                            )
                        ],
                        style={
                            'float': 'right',
                            'paddingRight': '4px',
                            'paddingTop': '15px'
                        }
                    )
                ]
            )
        ),
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

from faker import Faker
import feffery_antd_components as fac

faker = Faker(locale='zh_CN')

@app.callback(
    Output('custom-skeleton-demo', 'children'),
    Input('skeleton-custom-demo-input', 'nClicks')
)
def skeleton_custom_callback_demo(nClicks):
    import time
    time.sleep(2)

    return fac.AntdTable(
        columns=[
            {
                'title': '国家名示例',
                'dataIndex': '国家名示例',
                'width': '25%'
            },
            {
                'title': '省份名示例',
                'dataIndex': '省份名示例',
                'width': '25%'
            },
            {
                'title': '城市名示例',
                'dataIndex': '城市名示例',
                'width': '25%'
            },
            {
                'title': '日期示例',
                'dataIndex': '日期示例',
                'width': '25%'
            }
        ],
        bordered=True,
        data=[
            {
                'key': i,
                '国家名示例': faker.country(),
                '省份名示例': faker.province(),
                '城市名示例': faker.city_name(),
                '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None)
            }
            for i in range(3)
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
                component_name='AntdCustomSkeleton',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
