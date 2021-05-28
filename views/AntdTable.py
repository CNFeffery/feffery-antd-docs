import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import pandas as pd
import numpy as np
from faker import Faker

import callbacks.AntdTable

faker = Faker(locale='zh_CN')

docs_content = html.Div(
    [
        html.H2(
            'AntdTable(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '基础的表格', 'href': '#基础的表格'},
                        {'title': '手动分配百分比宽度', 'href': '#手动分配百分比宽度'},
                        {'title': '绝对像素宽度溢出的情况', 'href': '#绝对像素宽度溢出的情况'},
                        {'title': '限定maxHeight以固定表头', 'href': '#限定maxHeight以固定表头'},
                        {'title': '宽度溢出时固定左侧或右侧指定列', 'href': '#宽度溢出时固定左侧或右侧指定列'},
                        {'title': '指定部分列可编辑', 'href': '#指定部分列可编辑'},
                        {'title': '几种不同的再渲染模式', 'href': '#几种不同的再渲染模式'},
                        {'title': '分页相关设置', 'href': '#分页相关设置'},
                        {'title': '常规单列排序', 'href': '#常规单列排序'},
                        {'title': '多列组合排序', 'href': '#多列组合排序'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ]
                },
            ]
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

        dcc.Markdown(open('documents/AntdTable.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Span(
            '使用示例：',
            id='使用示例',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        html.Hr(),

        html.Div(
            [
                html.Strong(
                    '基础的表格：',
                    id='基础的表格',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例'
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ]
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例'
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ]
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '手动分配百分比宽度：',
                    id='手动分配百分比宽度',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': '30%'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': '30%'
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': '20%'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': '10%'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': '10%'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': '30%'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': '30%'
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': '20%'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': '10%'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': '10%'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '绝对像素宽度溢出的情况：',
                    id='绝对像素宽度溢出的情况',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': 400
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': 400
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': 400
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': 400
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': 400
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': 400
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': 400
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': 400
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': 400
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': 400
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '限定maxHeight以固定表头：',
                    id='限定maxHeight以固定表头',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': 400
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': 400
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': 400
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': 400
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': 400
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True,
                    maxHeight=200
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': 400
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': 400
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': 400
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': 400
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': 400
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True,
                    maxHeight=200
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '宽度溢出时固定左侧或右侧指定列：',
                    id='宽度溢出时固定左侧或右侧指定列',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': 400,
                            'fixed': 'left'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': 400
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': 400
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': 400
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': 400,
                            'fixed': 'right'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True,
                    maxHeight=200
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例',
                            'width': 400,
                            'fixed': 'left'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'width': 400
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例',
                            'width': 400
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例',
                            'width': 400
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'width': 400,
                            'fixed': 'right'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ],
                    bordered=True,
                    maxHeight=200
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '指定部分列可编辑：',
                    id='指定部分列可编辑',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'editable': True
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'editable': True
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ]
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例',
                            'editable': True
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例',
                            'editable': True
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(10)
                    ]
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '几种不同的再渲染模式：',
                    id='几种不同的再渲染模式',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': 'ellipsis内容省略示例',
                            'dataIndex': 'ellipsis内容省略示例',
                            'renderOptions': {'renderType': 'ellipsis'},
                            'width': 200
                        },
                        {
                            'title': '超链接示例',
                            'dataIndex': '超链接示例',
                            'renderOptions': {
                                'renderType': 'link',
                                'renderLinkText': '点击跳转'
                            }
                        },
                        {
                            'title': 'mini-line示例',
                            'dataIndex': 'mini-line示例',
                            'renderOptions': {
                                'renderType': 'mini-line'
                            }
                        },
                        {
                            'title': 'mini-bar示例',
                            'dataIndex': 'mini-bar示例',
                            'renderOptions': {
                                'renderType': 'mini-bar'
                            }
                        },
                        {
                            'title': 'mini-progress示例',
                            'dataIndex': 'mini-progress示例',
                            'renderOptions': {
                                'renderType': 'mini-progress'
                            }
                        },
                        {
                            'title': 'mini-area示例',
                            'dataIndex': 'mini-area示例',
                            'renderOptions': {
                                'renderType': 'mini-area'
                            }
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            'ellipsis内容省略示例': '这是一段废话，用来演示超长内容再渲染巴拉巴拉巴拉巴拉',
                            '超链接示例': 'https://github.com/CNFeffery/feffery-antd-components',
                            'mini-line示例': np.random.randint(1, 20, 10),
                            'mini-bar示例': np.random.randint(1, 20, 10),
                            'mini-progress示例': np.random.rand(),
                            'mini-area示例': np.random.randint(1, 20, 10),
                        }
                        for i in range(5)
                    ],
                    bordered=True
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': 'ellipsis内容省略示例',
                            'dataIndex': 'ellipsis内容省略示例',
                            'renderOptions': {'renderType': 'ellipsis'},
                            'width': 200
                        },
                        {
                            'title': '超链接示例',
                            'dataIndex': '超链接示例',
                            'renderOptions': {
                                'renderType': 'link',
                                'renderLinkText': '点击跳转'
                            }
                        },
                        {
                            'title': 'mini-line示例',
                            'dataIndex': 'mini-line示例',
                            'renderOptions': {
                                'renderType': 'mini-line'
                            }
                        },
                        {
                            'title': 'mini-bar示例',
                            'dataIndex': 'mini-bar示例',
                            'renderOptions': {
                                'renderType': 'mini-bar'
                            }
                        },
                        {
                            'title': 'mini-progress示例',
                            'dataIndex': 'mini-progress示例',
                            'renderOptions': {
                                'renderType': 'mini-progress'
                            }
                        },
                        {
                            'title': 'mini-area示例',
                            'dataIndex': 'mini-area示例',
                            'renderOptions': {
                                'renderType': 'mini-area'
                            }
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            'ellipsis内容省略示例': '这是一段废话，用来演示超长内容再渲染巴拉巴拉巴拉巴拉',
                            '超链接示例': 'https://github.com/CNFeffery/feffery-antd-components',
                            'mini-line示例': np.random.randint(1, 20, 10),
                            'mini-bar示例': np.random.randint(1, 20, 10),
                            'mini-progress示例': np.random.rand(),
                            'mini-area示例': np.random.randint(1, 20, 10),
                        }
                        for i in range(5)
                    ],
                    bordered=True
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '分页相关设置：',
                    id='分页相关设置',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例'
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(100)
                    ],
                    pagination={
                        'pageSize': 10,
                        'current': 5,
                        'pageSizeOptions': [5, 10, 15, 20, 25],
                        'showTotalPrefix': '本次共取得伪造数据 ',
                        'showTotalSuffix': ' 条！😋'
                    }
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': '国家名示例',
                            'dataIndex': '国家名示例'
                        },
                        {
                            'title': '省份名示例',
                            'dataIndex': '省份名示例'
                        },
                        {
                            'title': '城市名示例',
                            'dataIndex': '城市名示例'
                        },
                        {
                            'title': '日期示例',
                            'dataIndex': '日期示例'
                        },
                        {
                            'title': '邮编示例',
                            'dataIndex': '邮编示例'
                        }
                    ],
                    data=[
                        {
                            'key': i,
                            '国家名示例': faker.country(),
                            '省份名示例': faker.province(),
                            '城市名示例': faker.city_name(),
                            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                            '邮编示例': faker.postcode()
                        }
                        for i in range(100)
                    ],
                    pagination={
                        'pageSize': 10,
                        'current': 5,
                        'pageSizeOptions': [5, 10, 15, 20, 25],
                        'showTotalPrefix': '本次共取得伪造数据 ',
                        'showTotalSuffix': ' 条！😋'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '常规单列排序：',
                    id='常规单列排序',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}'
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {
                            f'字段{i}': np.random.randint(1, 5)
                            for i in range(1, 6)
                        }
                        for _ in range(10)
                    ],
                    sortOptions={
                        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5']
                    }
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}'
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {
                            f'字段{i}': np.random.randint(1, 5)
                            for i in range(1, 6)
                        }
                        for _ in range(10)
                    ],
                    sortOptions={
                        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5']
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '多列组合排序：',
                    id='多列组合排序',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}'
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {
                            f'字段{i}': np.random.randint(1, 5)
                            for i in range(1, 6)
                        }
                        for _ in range(10)
                    ],
                    sortOptions={
                        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                        'multiple': True
                    }
                )
                ```
                '''),

                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}'
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {
                            f'字段{i}': np.random.randint(1, 5)
                            for i in range(1, 6)
                        }
                        for _ in range(10)
                    ],
                    sortOptions={
                        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                        'multiple': True
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '回调示例：',
                    id='回调示例',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTable(
                    id='table-demo',
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}',
                            'editable': True
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {
                            f'字段{i}': np.random.randint(1, 5)
                            for i in range(1, 6)
                        }
                        for _ in range(10)
                    ],
                    sortOptions={
                        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                        'multiple': True
                    },
                    pagination={
                        'pageSize': 5
                    }
                ),
                html.P('currentData:'),
                html.Pre(id='table-demo-output1'),
                html.P('recentlyChangedRow:'),
                html.Pre(id='table-demo-output2')
                ...
                @app.callback(
                    [Output('table-demo-output1', 'children'),
                     Output('table-demo-output2', 'children')],
                    [Input('table-demo', 'currentData'),
                     Input('table-demo', 'recentlyChangedRow')],
                    prevent_initial_call=True
                )
                def date_picker_callback_demo(currentData, recentlyChangedRow):
                
                    return str(currentData), str(recentlyChangedRow)
                ```
                '''),

                fac.AntdTable(
                    id='table-demo',
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}',
                            'editable': True
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {
                            f'字段{i}': np.random.randint(1, 5)
                            for i in range(1, 6)
                        }
                        for _ in range(10)
                    ],
                    sortOptions={
                        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                        'multiple': True
                    },
                    pagination={
                        'pageSize': 5
                    }
                ),
                html.P('currentData:'),
                html.Pre(id='table-demo-output1'),
                html.P('recentlyChangedRow:'),
                html.Pre(id='table-demo-output2')
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
