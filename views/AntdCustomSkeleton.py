from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdCustomSkeleton

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCustomSkeleton(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCustomSkeleton.md', encoding='utf-8').read()
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
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '触发2秒自定义骨骼屏动画', id='skeleton-custom-demo-input',
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
                            '基于占位图组件自由搭建骨骼屏',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　最常用的方式是将你需要充当回调加载时骨骼屏内容的元素传入参数'),
                                fac.AntdText('skeletonContent', strong=True),
                                fac.AntdText('中')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdButton(
            '触发2秒自定义骨骼屏动画', id='skeleton-custom-demo-input',
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
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基于占位图组件自由搭建骨骼屏',
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
                            {'title': '基于占位图组件自由搭建骨骼屏', 'href': '#基于占位图组件自由搭建骨骼屏'}
                        ]
                    },
                ],
                offsetTop=0
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
