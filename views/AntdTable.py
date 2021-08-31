import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

import time
import dash
import pandas as pd
import numpy as np
from faker import Faker

from server import app

import callbacks.AntdTable

faker = Faker(locale='zh_CN')

server_side_df = pd.DataFrame({
    '组合排序示例1': np.random.randint(0, 100, 1000),
    '组合排序示例2': np.random.randint(0, 100, 1000),
    'checkbox筛选示例': np.random.permutation(list('abcde' * 200)),
    'keyword筛选示例': np.random.permutation(list('uvwxy' * 200))
})

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
                        {'title': '使用字段筛选功能', 'href': '#使用字段筛选功能'},
                        {'title': '妥善使用popupContainerId参数', 'href': '#妥善使用popupContainerId参数'},
                        {'title': '回调示例', 'href': '#回调示例'},
                        {'title': '服务端数据渲染模式示例', 'href': '#服务端数据渲染模式示例'},
                    ]
                },
            ],
            containerId='docs-content',
            targetOffset=200
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
                ),

                fac.AntdDivider(
                    '基础的表格',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='基础的表格',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '手动分配百分比宽度',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='手动分配百分比宽度',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '绝对像素宽度溢出的情况',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='绝对像素宽度溢出的情况',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '限定maxHeight以固定表头',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='限定maxHeight以固定表头',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '宽度溢出时固定左侧或右侧指定列',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='宽度溢出时固定左侧或右侧指定列',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '指定部分列可编辑',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='指定部分列可编辑',
            className='div-highlight'
        ),

        html.Div(
            [
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
                            # 注意，mini-progress模式接受的输入应当在0到1之间
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
                        },
                        {
                            'title': '标签模式示例',
                            'dataIndex': '标签模式示例',
                            'renderOptions': {
                                'renderType': 'tags'
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
                            '标签模式示例': [
                                {
                                    'tag': f'标签{i}示例1'
                                },
                                {
                                    'tag': f'标签{i}示例2', 'color': f'rgba(77, 182, 172, {0.5 + i * 0.1})'
                                }
                            ],
                        }
                        for i in range(5)
                    ],
                    bordered=True
                ),

                fac.AntdDivider(
                    '几种不同的再渲染模式',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
                                            # 注意，mini-progress模式接受的输入应当在0到1之间
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
                                        },
                                        {
                                            'title': '标签模式示例',
                                            'dataIndex': '标签模式示例',
                                            'renderOptions': {
                                                'renderType': 'tags'
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
                                            '标签模式示例': [
                                                {
                                                    'tag': f'标签{i}示例1'
                                                },
                                                {
                                                    'tag': f'标签{i}示例2', 'color': f'rgba(77, 182, 172, {0.5 + i * 0.1})'
                                                }
                                            ],
                                        }
                                        for i in range(5)
                                    ],
                                    bordered=True
                                )
                                ```
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
            id='几种不同的再渲染模式',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '分页相关设置',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='分页相关设置',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '常规单列排序',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='常规单列排序',
            className='div-highlight'
        ),

        html.Div(
            [
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
                ),

                fac.AntdDivider(
                    '多列组合排序',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
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
            id='多列组合排序',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdTable(
                    columns=[
                        {
                            'title': '默认的checkbox模式',
                            'dataIndex': f'默认的checkbox模式'
                        },
                        {
                            'title': '自定义选项的checkbox模式',
                            'dataIndex': '自定义选项的checkbox模式'
                        },
                        {
                            'title': 'keyword模式',
                            'dataIndex': 'keyword模式'
                        }
                    ],
                    data=[
                        {
                            '默认的checkbox模式': i,
                            '自定义选项的checkbox模式': i,
                            'keyword模式': i
                        }
                        for i in range(5)
                    ],
                    filterOptions={
                        '默认的checkbox模式': {},
                        '自定义选项的checkbox模式': {
                            'filterMode': 'checkbox',
                            'filterCustomItems': [1, 2, 3]
                        },
                        'keyword模式': {
                            'filterMode': 'keyword'
                        }
                    },
                    popupContainerId='docs-content'
                ),

                fac.AntdDivider(
                    '使用字段筛选功能',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdTable(
                                    columns=[
                                        {
                                            'title': '默认的checkbox模式',
                                            'dataIndex': f'默认的checkbox模式'
                                        },
                                        {
                                            'title': '自定义选项的checkbox模式',
                                            'dataIndex': '自定义选项的checkbox模式'
                                        },
                                        {
                                            'title': 'keyword模式',
                                            'dataIndex': 'keyword模式'
                                        }
                                    ],
                                    data=[
                                        {
                                            '默认的checkbox模式': i,
                                            '自定义选项的checkbox模式': i,
                                            'keyword模式': i
                                        }
                                        for i in range(5)
                                    ],
                                    filterOptions={
                                        '默认的checkbox模式': {},
                                        '自定义选项的checkbox模式': {
                                            'filterMode': 'checkbox',
                                            'filterCustomItems': [1, 2, 3]
                                        },
                                        'keyword模式': {
                                            'filterMode': 'keyword'
                                        }
                                    },
                                    popupContainerId='docs-content'
                                )
                                ```
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
            id='使用字段筛选功能',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdTitle('左例（未设置） 右例（设置popupContainerId参数）', level=5),
                html.Div(
                    [
                        html.Div(
                            [
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
                                    filterOptions={
                                        '字段1': {
                                            'filterMode': 'keyword'
                                        },
                                        '字段3': {
                                            'filterMode': 'checkbox',
                                            'filterCustomItems': [1, 2, 3]
                                        }
                                    }
                                ),
                                html.Div(
                                    style={
                                        'height': '400px'
                                    }
                                )
                            ],
                            style={
                                'flex': '1',
                                'padding': '20px',
                                'maxHeight': '200px',
                                'overflowY': 'auto'
                            }
                        ),
                        html.Div(
                            [
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
                                    filterOptions={
                                        '字段1': {
                                            'filterMode': 'keyword'
                                        },
                                        '字段3': {
                                            'filterMode': 'checkbox',
                                            'filterCustomItems': [1, 2, 3]
                                        }
                                    },
                                    popupContainerId='popupContainerId-container-demo'
                                ),
                                html.Div(
                                    style={
                                        'height': '400px'
                                    }
                                )
                            ],
                            id='popupContainerId-container-demo',
                            style={
                                'flex': '1',
                                'padding': '20px',
                                'maxHeight': '200px',
                                'overflowY': 'auto',
                                'position': 'relative'
                            }
                        )
                    ],
                    style={
                        'display': 'flex'
                    }
                ),

                fac.AntdDivider(
                    '妥善使用popupContainerId参数',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　当设置了筛选等具有点击弹出悬浮组件的功能时，这些悬浮组件默认绑定的参考容器为根节点',
                        ),
                        fac.AntdText(
                            'body',
                            italic=True
                        ),
                        fac.AntdText(
                            '，因此当我们的'
                        ),
                        fac.AntdText(
                            'AntdTable',
                            strong=True
                        ),
                        fac.AntdText(
                            '组件位于具有局部滚动条的容器中时，点击展开悬浮层后滚动页面会出现悬浮层不跟随移动的情况，因此需要参考本例，利用popupContainerId参数为'
                        ),
                        fac.AntdText(
                            'AntdTable',
                            strong=True
                        ),
                        fac.AntdText(
                            '绑定position为relative的容器对应的id'
                        )
                    ]
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdTitle('左例（未设置） 右例（设置popupContainerId参数）', level=5),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
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
                                                        filterOptions={
                                                            '字段1': {
                                                                'filterMode': 'keyword'
                                                            },
                                                            '字段3': {
                                                                'filterMode': 'checkbox',
                                                                'filterCustomItems': [1, 2, 3]
                                                            }
                                                        }
                                                    ),
                                                    html.Div(
                                                        style={
                                                            'height': '400px'
                                                        }
                                                    )
                                                ],
                                                style={
                                                    'flex': '1',
                                                    'padding': '20px',
                                                    'maxHeight': '200px',
                                                    'overflowY': 'auto'
                                                }
                                            ),
                                            html.Div(
                                                [
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
                                                        filterOptions={
                                                            '字段1': {
                                                                'filterMode': 'keyword'
                                                            },
                                                            '字段3': {
                                                                'filterMode': 'checkbox',
                                                                'filterCustomItems': [1, 2, 3]
                                                            }
                                                        },
                                                        popupContainerId='popupContainerId-container-demo'
                                                    ),
                                                    html.Div(
                                                        style={
                                                            'height': '400px'
                                                        }
                                                    )
                                                ],
                                                id='popupContainerId-container-demo',
                                                style={
                                                    'flex': '1',
                                                    'padding': '20px',
                                                    'maxHeight': '200px',
                                                    'overflowY': 'auto',
                                                    'position': 'relative'
                                                }
                                            )
                                        ],
                                        style={
                                            'display': 'flex'
                                        }
                                    )
                                ```
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
            id='妥善使用popupContainerId参数',
            className='div-highlight'
        ),

        html.Div(
            [
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
                        for _ in range(20)
                    ],
                    sortOptions={
                        'sortDataIndexes': ['字段2', '字段4', '字段5'],
                        'multiple': True
                    },
                    filterOptions={
                        '字段1': {
                            'filterMode': 'checkbox'
                        },
                        '字段3': {
                            'filterMode': 'keyword'
                        }
                    },
                    pagination={
                        'pageSize': 5
                    },
                    popupContainerId='docs-content'
                ),
                fac.AntdSpin(
                    html.Div(id='table-demo-output'),
                    text='回调中'
                ),

                fac.AntdDivider(
                    '回调示例',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　这个例子中展示了'
                        ),
                        fac.AntdText('AntdTable', strong=True),
                        fac.AntdText('中所有的交互事件被用户触发时所记录的参数变化情况')
                    ]
                ),

                fac.AntdCollapse(
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
                                        for _ in range(20)
                                    ],
                                    sortOptions={
                                        'sortDataIndexes': ['字段2', '字段4', '字段5'],
                                        'multiple': True
                                    },
                                    filterOptions={
                                        '字段1': {
                                            'filterMode': 'checkbox'
                                        },
                                        '字段3': {
                                            'filterMode': 'keyword'
                                        }
                                    },
                                    pagination={
                                        'pageSize': 5
                                    },
                                    popupContainerId='docs-content'
                                ),
                                fac.AntdSpin(
                                    html.Div(id='table-demo-output'),
                                    text='回调中'
                                )
                                ...
                                @app.callback(
                                    Output('table-demo-output', 'children'),
                                    [Input('table-demo', 'currentData'),
                                     Input('table-demo', 'recentlyChangedRow'),
                                     Input('table-demo', 'sorter'),
                                     Input('table-demo', 'filter'),
                                     Input('table-demo', 'pagination')],
                                    prevent_initial_call=True
                                )
                                def table_callback_demo(currentData,
                                                        recentlyChangedRow,
                                                        sorter,
                                                        filter,
                                                        pagination):
                                
                                    ctx = dash.callback_context
                                
                                    return [
                                        fac.AntdTitle('本次回调由{}所触发'.format(ctx.triggered[0]['prop_id'].split('.')[-1]), level=3),
                                        fac.AntdDivider(),
                                
                                        fac.AntdTitle('currentData：', level=5),
                                        html.Pre(str(currentData)),
                                
                                        fac.AntdTitle('recentlyChangedRow：', level=5),
                                        html.Pre(str(recentlyChangedRow)),
                                
                                        fac.AntdTitle('sorter：', level=5),
                                        html.Pre(str(sorter)),
                                
                                        fac.AntdTitle('filter：', level=5),
                                        html.Pre(str(filter)),
                                
                                        fac.AntdTitle('pagination：', level=5),
                                        html.Pre(str(pagination))
                                    ]

                                ```
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
            id='回调示例',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdSpin(
                    fac.AntdTable(
                        id='table-server-side-demo',
                        mode='server-side',
                        columns=[
                            {
                                'title': '组合排序示例1',
                                'dataIndex': '组合排序示例1'
                            },
                            {
                                'title': '组合排序示例2',
                                'dataIndex': '组合排序示例2'
                            },
                            {
                                'title': 'checkbox筛选示例',
                                'dataIndex': 'checkbox筛选示例'
                            },
                            {
                                'title': 'keyword筛选示例',
                                'dataIndex': 'keyword筛选示例'
                            }
                        ],
                        data=server_side_df.head(5).to_dict('records'),
                        sortOptions={
                            'sortDataIndexes': ['组合排序示例1', '组合排序示例2'],
                            'multiple': True
                        },
                        filterOptions={
                            'checkbox筛选示例': {
                                'filterMode': 'checkbox',
                                'filterCustomItems': list('abcde')
                            },
                            'keyword筛选示例': {
                                'filterMode': 'keyword'
                            }
                        },
                        pagination={
                            'current': 1,
                            'total': server_side_df.shape[0],
                            'pageSize': 5,
                            'pageSizeOptions': [5, 10]
                        },
                        popupContainerId='docs-content'
                    ),
                    text='回调中'
                ),

                fac.AntdDivider(
                    '服务端数据渲染模式示例',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '　　这个例子中展示了'
                        ),
                        fac.AntdText('AntdTable', strong=True),
                        fac.AntdText('在设置参数'),
                        fac.AntdText('mode="server-side"', strong=True),
                        fac.AntdText(
                            '时激活了服务端渲染模式，在此模式下，当用户触发了翻页、排序及筛选等交互操作时，'
                            '不会自动在前端执行操作，而是需要开发者在后端构造相应的回调函数接受这些交互操作的反馈参数，'
                            '从而编写相应的逻辑，对'
                        ),
                        fac.AntdText('AntdTable', strong=True),
                        fac.AntdText(
                            '的data、pagination等参数进行输出，从而达到前端“发送操作指令”，'
                            '后端操纵源数据并传回前端进行渲染的目的，保证了任意时刻下，前端只需要存放及渲染对应筛选及排序条件下当前页的少量数据'
                        )
                    ]
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                
                                server_side_df = pd.DataFrame({
                                    '组合排序示例1': np.random.randint(0, 100, 1000),
                                    '组合排序示例2': np.random.randint(0, 100, 1000),
                                    'checkbox筛选示例': np.random.permutation(list('abcde' * 200)),
                                    'keyword筛选示例': np.random.permutation(list('uvwxy' * 200))
                                })
                                
                                fac.AntdSpin(
                                    fac.AntdTable(
                                        id='table-server-side-demo',
                                        mode='server-side',
                                        columns=[
                                            {
                                                'title': '组合排序示例1',
                                                'dataIndex': '组合排序示例1'
                                            },
                                            {
                                                'title': '组合排序示例2',
                                                'dataIndex': '组合排序示例2'
                                            },
                                            {
                                                'title': 'checkbox筛选示例',
                                                'dataIndex': 'checkbox筛选示例'
                                            },
                                            {
                                                'title': 'keyword筛选示例',
                                                'dataIndex': 'keyword筛选示例'
                                            }
                                        ],
                                        data=server_side_df.head(5).to_dict('records'),
                                        sortOptions={
                                            'sortDataIndexes': ['组合排序示例1', '组合排序示例2'],
                                            'multiple': True
                                        },
                                        filterOptions={
                                            'checkbox筛选示例': {
                                                'filterMode': 'checkbox',
                                                'filterCustomItems': list('abcde')
                                            },
                                            'keyword筛选示例': {
                                                'filterMode': 'keyword'
                                            }
                                        },
                                        pagination={
                                            'current': 1,
                                            'total': server_side_df.shape[0],
                                            'pageSize': 5,
                                            'pageSizeOptions': [5, 10]
                                        },
                                        popupContainerId='docs-content'
                                    ),
                                    text='回调中'
                                )
                                ...
                                @app.callback(
                                    [Output('table-server-side-demo', 'data'),
                                     Output('table-server-side-demo', 'pagination')],
                                    [Input('table-server-side-demo', 'pagination'),
                                     Input('table-server-side-demo', 'sorter'),
                                     Input('table-server-side-demo', 'filter')],
                                    State('table-server-side-demo', 'filterOptions'),
                                    prevent_initial_call=True
                                )
                                def table_server_side_callback_demo(pagination,
                                                                    sorter,
                                                                    filter,
                                                                    filterOptions):
                                
                                    ctx = dash.callback_context
                                
                                    # 构造临时副本数据框
                                    batch_df = server_side_df.copy()
                                
                                    # 检查是否存在未清除的筛选操作，若有，则进行离线筛选操作
                                    if filter:
                                
                                        for key, value in filter.items():
                                            # 若对应字段当前存在筛选条件
                                            if value:
                                                if 'filterMode' in filterOptions[key].keys():
                                
                                                    if filterOptions[key]['filterMode'] == 'checkbox':
                                                        batch_df = batch_df.loc[batch_df[key].isin(value), :]
                                                    elif filterOptions[key]['filterMode'] == 'keyword':
                                                        batch_df = batch_df.loc[batch_df[key].astype('str').str.contains(value[0]), :]
                                
                                                else:
                                                    batch_df = batch_df.loc[batch_df[key].isin(value), :]
                                
                                    # 检查是否存在未清除的排序操作，若有，则进行离线排序操作
                                    if sorter and sorter['columns'].__len__() != 0:
                                        # 将sorter参数中的信息转义为迎合pandas中参数ascending的bool值
                                        ascending = list(map(lambda order: True if order == 'ascend' else False, sorter['orders']))
                                
                                        # 若没有字段参与排序，则直接返回batch_df的对应页数据帧，从而结束本次回调
                                        if ascending.__len__() == 0:
                                            return batch_df.iloc[(pagination['current'] - 1) * pagination['pageSize']
                                                                 :
                                                                 pagination['current'] * pagination['pageSize'], :].to_dict('records')
                                
                                        # 对batch_df按照抽取出的条件进行排序
                                        (
                                            batch_df
                                                .sort_values(
                                                sorter['columns'],
                                                ascending=ascending,
                                                inplace=True
                                            )
                                        )
                                
                                    # 若本次回调由筛选或排序操作触发，按照当前的条件组合更新pagination参数
                                    if ctx.triggered[0]['prop_id'] in ['table-server-side-demo.sorter', 'table-server-side-demo.filter']:
                                        pagination = {
                                            **pagination,
                                            **{
                                                'current': 1,
                                                'pageSize': 5,
                                                'total': batch_df.shape[0]
                                            }
                                        }
                                
                                        # 在前面的条件组合基础上，输出对应页的数据帧
                                        start_index = (pagination['current'] - 1) * pagination['pageSize']
                                        end_index = pagination['current'] * pagination['pageSize']
                                
                                        # 更新data与pagination参数
                                        return (
                                            batch_df.iloc[start_index:end_index, :].to_dict('records'),
                                            pagination
                                        )
                                
                                    # 若本次回调由翻页操作触发，则只返回data，pagination返回dash.no_update（因为pagination在前端用户操作时已修改，这里避免产生环形回调）
                                    elif ctx.triggered[0]['prop_id'] == 'table-server-side-demo.pagination':
                                
                                        # 在前面的条件组合基础上，输出对应页的数据帧
                                        start_index = (pagination['current'] - 1) * pagination['pageSize']
                                        end_index = pagination['current'] * pagination['pageSize']
                                
                                        # 更新data与pagination参数
                                        return (
                                            batch_df.iloc[start_index:end_index, :].to_dict('records'),
                                            dash.no_update
                                        )
                                
                                    return dash.no_update
                                ```
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
            id='服务端数据渲染模式示例',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)


@app.callback(
    [Output('table-server-side-demo', 'data'),
     Output('table-server-side-demo', 'pagination')],
    [Input('table-server-side-demo', 'pagination'),
     Input('table-server-side-demo', 'sorter'),
     Input('table-server-side-demo', 'filter')],
    State('table-server-side-demo', 'filterOptions'),
    prevent_initial_call=True
)
def table_server_side_callback_demo(pagination,
                                    sorter,
                                    filter,
                                    filterOptions):
    '''
    AntdTable服务端渲染模式回调示例
    :param pagination: 翻页操作的响应参数
    :param sorter: 排序操作的响应参数
    :param filter: 筛选操作的响应参数
    :param filterOptions: 筛选配置参数
    :return: 对应输入组合条件下的数据帧及更新后的pagination参数
    '''

    time.sleep(0.5)

    ctx = dash.callback_context

    # 构造临时副本数据框
    batch_df = server_side_df.copy()

    # 检查是否存在未清除的筛选操作，若有，则进行离线筛选操作
    if filter:

        for key, value in filter.items():
            # 若对应字段当前存在筛选条件
            if value:
                if 'filterMode' in filterOptions[key].keys():

                    if filterOptions[key]['filterMode'] == 'checkbox':
                        batch_df = batch_df.loc[batch_df[key].isin(value), :]
                    elif filterOptions[key]['filterMode'] == 'keyword':
                        batch_df = batch_df.loc[batch_df[key].astype('str').str.contains(value[0]), :]

                else:
                    batch_df = batch_df.loc[batch_df[key].isin(value), :]

    # 检查是否存在未清除的排序操作，若有，则进行离线排序操作
    if sorter and sorter['columns'].__len__() != 0:
        # 将sorter参数中的信息转义为迎合pandas中参数ascending的bool值
        ascending = list(map(lambda order: True if order == 'ascend' else False, sorter['orders']))

        # 若没有字段参与排序，则直接返回batch_df的对应页数据帧，从而结束本次回调
        if ascending.__len__() == 0:
            return batch_df.iloc[(pagination['current'] - 1) * pagination['pageSize']
                                 :
                                 pagination['current'] * pagination['pageSize'], :].to_dict('records')

        # 对batch_df按照抽取出的条件进行排序
        (
            batch_df
                .sort_values(
                sorter['columns'],
                ascending=ascending,
                inplace=True
            )
        )

    # 若本次回调由筛选或排序操作触发，按照当前的条件组合更新pagination参数
    if ctx.triggered[0]['prop_id'] in ['table-server-side-demo.sorter', 'table-server-side-demo.filter']:
        pagination = {
            **pagination,
            **{
                'current': 1,
                'pageSize': 5,
                'total': batch_df.shape[0]
            }
        }

        # 在前面的条件组合基础上，输出对应页的数据帧
        start_index = (pagination['current'] - 1) * pagination['pageSize']
        end_index = pagination['current'] * pagination['pageSize']

        # 更新data与pagination参数
        return (
            batch_df.iloc[start_index:end_index, :].to_dict('records'),
            pagination
        )

    # 若本次回调由翻页操作触发，则只返回data，pagination返回dash.no_update（因为pagination在前端用户操作时已修改，这里避免产生环形回调）
    elif ctx.triggered[0]['prop_id'] == 'table-server-side-demo.pagination':

        # 在前面的条件组合基础上，输出对应页的数据帧
        start_index = (pagination['current'] - 1) * pagination['pageSize']
        end_index = pagination['current'] * pagination['pageSize']

        # 更新data与pagination参数
        return (
            batch_df.iloc[start_index:end_index, :].to_dict('records'),
            dash.no_update
        )

    return dash.no_update
