from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
from dash.dependencies import Input, Output, State

import json
import dash
import pandas as pd
import numpy as np
from faker import Faker

from server import app

import callbacks.AntdTable

faker = Faker(locale='zh_CN')

np.random.seed(42)
server_side_df = pd.DataFrame({
    '组合排序示例1': np.random.randint(0, 100, 1000),
    '组合排序示例2': np.random.randint(0, 100, 1000),
    'checkbox筛选示例': np.random.permutation(list('abcde' * 200)),
    'keyword筛选示例': np.random.permutation(list('uvwxy' * 200))
})

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTable(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdTable.md', encoding='utf-8').read()
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
                                for i in range(3)
                            ]
                        ),

                        fac.AntdDivider(
                            '基础的表格',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
        for i in range(3)
    ]
)'''
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
                                for i in range(3)
                            ],
                            bordered=True
                        ),

                        fac.AntdDivider(
                            '手动分配百分比宽度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
        for i in range(3)
    ],
    bordered=True
)'''
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
                                for i in range(3)
                            ],
                            maxWidth=2000,
                            bordered=True
                        ),

                        fac.AntdDivider(
                            '限定maxHeight开启横向滚动模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　当表格中各个字段设定的宽度值超出当前表格实际的宽度值时，可通过设置参数'),
                                fac.AntdText('maxWidth', code=True),
                                fac.AntdText('，从而实现当表格实际宽度小于这个设定值时自动开启横向滚动模式以保证各字段设定的宽度值生效')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
        for i in range(3)
    ],
    maxWidth=2000,
    bordered=True
),

fac.AntdDivider(
    '限定maxHeight开启横向滚动模式',
    lineColor='#f0f0f0',
    innerTextOrientation='left'
)'''
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
                    id='限定maxHeight开启横向滚动模式',
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
)'''
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
                                for i in range(3)
                            ],
                            bordered=True,
                            maxWidth=2000
                        ),

                        fac.AntdDivider(
                            '宽度溢出时固定左侧或右侧指定列',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
        for i in range(3)
    ],
    bordered=True,
    maxWidth=2000
)'''
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
                    id='宽度溢出时固定左侧或右侧指定列',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '国家名示例',
                                    'dataIndex': '国家名示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '省份名示例',
                                    'dataIndex': '省份名示例',
                                    'editable': True,
                                    'width': '20%'
                                },
                                {
                                    'title': '城市名示例',
                                    'dataIndex': '城市名示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '日期示例',
                                    'dataIndex': '日期示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '邮编示例',
                                    'dataIndex': '邮编示例',
                                    'editable': True,
                                    'width': '20%'
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
                                for i in range(3)
                            ],
                            bordered=True
                        ),

                        fac.AntdDivider(
                            '指定部分列可编辑',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '国家名示例',
            'dataIndex': '国家名示例',
            'width': '20%'
        },
        {
            'title': '省份名示例',
            'dataIndex': '省份名示例',
            'editable': True,
            'width': '20%'
        },
        {
            'title': '城市名示例',
            'dataIndex': '城市名示例',
            'width': '20%'
        },
        {
            'title': '日期示例',
            'dataIndex': '日期示例',
            'width': '20%'
        },
        {
            'title': '邮编示例',
            'dataIndex': '邮编示例',
            'editable': True,
            'width': '20%'
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
        for i in range(3)
    ],
    bordered=True
)'''
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
                                    'renderOptions': {'renderType': 'ellipsis'}
                                }
                            ],
                            data=[
                                {
                                    'key': i,
                                    'ellipsis内容省略示例': '这是一段废话，用来演示超长内容再渲染巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉'
                                }
                                for i in range(3)
                            ],
                            bordered=True,
                            style={
                                'width': '250px'
                            },
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '超长内容省略模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　设置'),
                                fac.AntdText("'renderOptions': {'renderType': 'ellipsis'}", code=True),
                                fac.AntdText('后，会开启'),
                                fac.AntdText('超长内容省略模式', strong=True),
                                fac.AntdText('，超出单元格默认宽度的文本内容会被省略截断，当鼠标悬浮在单元格上会出现记录完整内容的提示框')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': 'ellipsis内容省略示例',
            'dataIndex': 'ellipsis内容省略示例',
            'renderOptions': {'renderType': 'ellipsis'}
        }
    ],
    data=[
        {
            'key': i,
            'ellipsis内容省略示例': '这是一段废话，用来演示超长内容再渲染巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉'
        }
        for i in range(3)
    ],
    bordered=True,
    style={
        'width': '250px'
    },
    containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
)'''
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
                    id='超长内容省略模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '超链接示例',
                                    'dataIndex': '超链接示例',
                                    'renderOptions': {
                                        'renderType': 'link',
                                        'renderLinkText': '点击跳转'
                                    }
                                }
                            ],
                            data=[
                                {
                                    'key': i,
                                    '超链接示例': {
                                        'href': 'https://github.com/CNFeffery/feffery-antd-components'
                                    }
                                }
                                for i in range(3)
                            ],
                            bordered=True,
                            style={
                                'width': '250px'
                            }
                        ),

                        fac.AntdDivider(
                            '超链接模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '超链接示例',
            'dataIndex': '超链接示例',
            'renderOptions': {
                'renderType': 'link',
                'renderLinkText': '点击跳转'
            }
        }
    ],
    data=[
        {
            'key': i,
            '超链接示例': {
                'href': 'https://github.com/CNFeffery/feffery-antd-components'
            }
        }
        for i in range(3)
    ],
    bordered=True,
    style={
        'width': '250px'
    }
)'''
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
                    id='超链接模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': 'mini-line示例',
                                    'dataIndex': 'mini-line示例',
                                    'width': '20%',
                                    'renderOptions': {
                                        'renderType': 'mini-line'
                                    }
                                },
                                {
                                    'title': 'mini-bar示例',
                                    'dataIndex': 'mini-bar示例',
                                    'width': '20%',
                                    'renderOptions': {
                                        'renderType': 'mini-bar'
                                    }
                                },
                                {
                                    # 注意，mini-progress模式接受的输入应当在0到1之间
                                    'title': 'mini-progress示例',
                                    'dataIndex': 'mini-progress示例',
                                    'width': '20%',
                                    'renderOptions': {
                                        'renderType': 'mini-progress'
                                    }
                                },
                                {
                                    # 注意，mini-ring-progress模式接受的输入应当在0到1之间
                                    'title': 'mini-ring-progress示例',
                                    'dataIndex': 'mini-ring-progress示例',
                                    'width': '20%',
                                    'renderOptions': {
                                        'renderType': 'mini-ring-progress'
                                    }
                                },
                                {
                                    'title': 'mini-area示例',
                                    'dataIndex': 'mini-area示例',
                                    'width': '20%',
                                    'renderOptions': {
                                        'renderType': 'mini-area'
                                    }
                                }
                            ],
                            data=[
                                {
                                    'key': i,
                                    'mini-line示例': np.random.randint(1, 20, 10),
                                    'mini-bar示例': np.random.randint(1, 20, 10),
                                    'mini-progress示例': np.random.rand(),
                                    'mini-ring-progress示例': np.random.rand(),
                                    'mini-area示例': np.random.randint(1, 20, 10)
                                }
                                for i in range(3)
                            ],
                            miniChartHeight=60,
                            bordered=True,
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '迷你图模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　在这个例子中，为了保证'),
                                fac.AntdText('"mini-ring-progress"', code=True),
                                fac.AntdText('的显示正常，使用到参数'),
                                fac.AntdText('miniChartHeight', code=True),
                                fac.AntdText('人为抬高了迷你图单元格的像素高度，实际使用时请根据需要自行设置')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': 'mini-line示例',
            'dataIndex': 'mini-line示例',
            'width': '20%',
            'renderOptions': {
                'renderType': 'mini-line'
            }
        },
        {
            'title': 'mini-bar示例',
            'dataIndex': 'mini-bar示例',
            'width': '20%',
            'renderOptions': {
                'renderType': 'mini-bar'
            }
        },
        {
            # 注意，mini-progress模式接受的输入应当在0到1之间
            'title': 'mini-progress示例',
            'dataIndex': 'mini-progress示例',
            'width': '20%',
            'renderOptions': {
                'renderType': 'mini-progress'
            }
        },
        {
            # 注意，mini-ring-progress模式接受的输入应当在0到1之间
            'title': 'mini-ring-progress示例',
            'dataIndex': 'mini-ring-progress示例',
            'width': '20%',
            'renderOptions': {
                'renderType': 'mini-ring-progress'
            }
        },
        {
            'title': 'mini-area示例',
            'dataIndex': 'mini-area示例',
            'width': '20%',
            'renderOptions': {
                'renderType': 'mini-area'
            }
        }
    ],
    data=[
        {
            'key': i,
            'mini-line示例': np.random.randint(1, 20, 10),
            'mini-bar示例': np.random.randint(1, 20, 10),
            'mini-progress示例': np.random.rand(),
            'mini-ring-progress示例': np.random.rand(),
            'mini-area示例': np.random.randint(1, 20, 10)
        }
        for i in range(3)
    ],
    miniChartHeight=60,
    bordered=True,
    containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
)'''
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
                    id='迷你图模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
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
                                    '标签模式示例': [
                                        {
                                            'tag': f'标签{i}示例1'
                                        },
                                        {
                                            'tag': f'标签{i}示例2', 'color': f'rgba(77, 182, 172, {0.5 + i * 0.1})'
                                        }
                                    ],
                                }
                                for i in range(3)
                            ],
                            bordered=True,
                            style={
                                'width': '300px'
                            }
                        ),

                        fac.AntdDivider(
                            '标签模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
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
            '标签模式示例': [
                {
                    'tag': f'标签{i}示例1'
                },
                {
                    'tag': f'标签{i}示例2', 'color': f'rgba(77, 182, 172, {0.5 + i * 0.1})'
                }
            ],
        }
        for i in range(3)
    ],
    bordered=True,
    style={
        'width': '300px'
    }
)'''
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
                    id='标签模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '单按钮示例',
                                    'dataIndex': '单按钮示例',
                                    'renderOptions': {'renderType': 'button'},
                                    'width': '25%'
                                },
                                {
                                    'title': '多按钮示例',
                                    'dataIndex': '多按钮示例',
                                    'renderOptions': {'renderType': 'button'},
                                    'width': '50%'
                                },
                                {
                                    'title': '气泡确认按钮示例',
                                    'dataIndex': '气泡确认按钮示例',
                                    'renderOptions': {
                                        'renderType': 'button',
                                        'renderButtonPopConfirmProps': {
                                            'title': '确认操作',
                                            'okText': '继续',
                                            'cancelText': '再想想'
                                        }
                                    },
                                    'width': '25%'
                                }
                            ],
                            data=[
                                {
                                    'key': i,
                                    '单按钮示例': {
                                        'content': '按钮示例',
                                        'type': 'primary'
                                    },
                                    '多按钮示例': [
                                        {
                                            'content': '按钮示例1',
                                            'type': 'primary'
                                        },
                                        {
                                            'content': '按钮示例2',
                                            'danger': True
                                        }
                                    ],
                                    '气泡确认按钮示例': {
                                        'content': '气泡确认按钮示例',
                                        'type': 'primary'
                                    }
                                }
                                for i in range(3)
                            ],
                            bordered=True,
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '按钮模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '单按钮示例',
            'dataIndex': '单按钮示例',
            'renderOptions': {'renderType': 'button'},
            'width': '25%'
        },
        {
            'title': '多按钮示例',
            'dataIndex': '多按钮示例',
            'renderOptions': {'renderType': 'button'},
            'width': '50%'
        },
        {
            'title': '气泡确认按钮示例',
            'dataIndex': '气泡确认按钮示例',
            'renderOptions': {
                'renderType': 'button',
                'renderButtonPopConfirmProps': {
                    'title': '确认操作',
                    'okText': '继续',
                    'cancelText': '再想想'
                }
            },
            'width': '25%'
        }
    ],
    data=[
        {
            'key': i,
            '单按钮示例': {
                'content': '按钮示例',
                'type': 'primary'
            },
            '多按钮示例': [
                {
                    'content': '按钮示例1',
                    'type': 'primary'
                },
                {
                    'content': '按钮示例2',
                    'danger': True
                }
            ],
            '气泡确认按钮示例': {
                'content': '气泡确认按钮示例',
                'type': 'primary'
            }
        }
        for i in range(3)
    ],
    bordered=True,
    containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
)'''
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
                    id='按钮模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '可复制内容示例',
                                    'dataIndex': '可复制内容示例',
                                    'renderOptions': {'renderType': 'copyable'}
                                }
                            ],
                            data=[
                                {
                                    'key': i,
                                    '可复制内容示例': '可复制内容示例'
                                }
                                for i in range(3)
                            ],
                            style={
                                'width': '250px'
                            },
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '可复制模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '可复制内容示例',
            'dataIndex': '可复制内容示例',
            'renderOptions': {'renderType': 'copyable'}
        }
    ],
    data=[
        {
            'key': i,
            '可复制内容示例': '可复制内容示例'
        }
        for i in range(3)
    ],
    style={
        'width': '250px'
    },
    containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
)'''
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
                    id='可复制模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '状态徽标示例',
                                    'dataIndex': '状态徽标示例',
                                    'renderOptions': {'renderType': 'status-badge'}
                                }
                            ],
                            data=[
                                {
                                    'key': i,
                                    '状态徽标示例': {
                                        'status': status,
                                        'text': status + '状态示例'
                                    }
                                }
                                for i, status in enumerate(['success', 'processing', 'default', 'error', 'warning'])
                            ],
                            style={
                                'width': '250px'
                            }
                        ),

                        fac.AntdDivider(
                            '状态徽标模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '状态徽标示例',
            'dataIndex': '状态徽标示例',
            'renderOptions': {'renderType': 'status-badge'}
        }
    ],
    data=[
        {
            'key': i,
            '状态徽标示例': {
                'status': status,
                'text': status + '状态示例'
            }
        }
        for i, status in enumerate(['success', 'processing', 'default', 'error', 'warning'])
    ],
    style={
        'width': '250px'
    }
)'''
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
                    id='状态徽标模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '国家名示例',
                                    'dataIndex': '国家名示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '省份名示例',
                                    'dataIndex': '省份名示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '城市名示例',
                                    'dataIndex': '城市名示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '日期示例',
                                    'dataIndex': '日期示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '邮编示例',
                                    'dataIndex': '邮编示例',
                                    'width': '20%'
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
                            bordered=True,
                            pagination={
                                'pageSize': 10,
                                'current': 5,
                                'pageSizeOptions': [5, 10, 15, 20, 25],
                                'showTotalPrefix': '本次共取得示例数据 ',
                                'showTotalSuffix': ' 条！😋'
                            }
                        ),

                        fac.AntdDivider(
                            '分页相关设置',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '国家名示例',
            'dataIndex': '国家名示例',
            'width': '20%'
        },
        {
            'title': '省份名示例',
            'dataIndex': '省份名示例',
            'width': '20%'
        },
        {
            'title': '城市名示例',
            'dataIndex': '城市名示例',
            'width': '20%'
        },
        {
            'title': '日期示例',
            'dataIndex': '日期示例',
            'width': '20%'
        },
        {
            'title': '邮编示例',
            'dataIndex': '邮编示例',
            'width': '20%'
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
    bordered=True,
    pagination={
        'pageSize': 10,
        'current': 5,
        'pageSizeOptions': [5, 10, 15, 20, 25],
        'showTotalPrefix': '本次共取得示例数据 ',
        'showTotalSuffix': ' 条！😋'
    }
)'''
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
                                for _ in range(3)
                            ],
                            bordered=True,
                            sortOptions={
                                'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5']
                            },
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '常规单列排序',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
        for _ in range(3)
    ],
    bordered=True,
    sortOptions={
        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5']
    },
    containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
)'''
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
                            bordered=True,
                            sortOptions={
                                'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                                'multiple': True
                            },
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '多列组合排序',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
    bordered=True,
    sortOptions={
        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
        'multiple': True
    },
    containerId='docs-content' # 绑定局部滚动容器以确保悬浮层正常显示
)'''
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
                            bordered=True,
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
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '使用字段筛选功能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
    bordered=True,
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
    containerId='docs-content' # 绑定局部滚动容器以确保悬浮层正常显示
)'''
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
                    id='使用字段筛选功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '字段示例1',
                                    'dataIndex': '字段示例1'
                                },
                                {
                                    'title': '字段示例2',
                                    'dataIndex': '字段示例2'
                                },
                                {
                                    'title': '字段示例3',
                                    'dataIndex': '字段示例3'
                                }
                            ],
                            bordered=True,
                            data=[
                                {
                                    '字段示例1': i,
                                    '字段示例2': i,
                                    '字段示例3': i
                                }
                                for i in range(5)
                            ],
                            titlePopoverInfo={
                                '字段示例1': {
                                    'title': '字段说明',
                                    'content': '这是字段示例1的字段说明'
                                },
                                '字段示例3': {
                                    'title': '字段说明',
                                    'content': '这是字段示例3的字段说明'
                                }
                            },
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider(
                            '为表头添加字段说明信息',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '字段示例1',
            'dataIndex': '字段示例1'
        },
        {
            'title': '字段示例2',
            'dataIndex': '字段示例2'
        },
        {
            'title': '字段示例3',
            'dataIndex': '字段示例3'
        }
    ],
    bordered=True,
    data=[
        {
            '字段示例1': i,
            '字段示例2': i,
            '字段示例3': i
        }
        for i in range(5)
    ],
    titlePopoverInfo={
        '字段示例1': {
            'title': '字段说明',
            'content': '这是字段示例1的字段说明'
        },
        '字段示例3': {
            'title': '字段说明',
            'content': '这是字段示例3的字段说明'
        }
    },
    containerId='docs-content' # 绑定局部滚动容器以确保悬浮层正常显示
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
                    id='为表头添加字段说明信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider("rowSelectionType='checkbox'", innerTextOrientation='left'),
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '字段示例1',
                                    'dataIndex': '字段示例1'
                                },
                                {
                                    'title': '字段示例2',
                                    'dataIndex': '字段示例2'
                                },
                                {
                                    'title': '字段示例3',
                                    'dataIndex': '字段示例3'
                                }
                            ],
                            data=[
                                {
                                    '字段示例1': i,
                                    '字段示例2': i,
                                    '字段示例3': i
                                }
                                for i in range(5)
                            ],
                            bordered=True,
                            rowSelectionType='checkbox',
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),

                        fac.AntdDivider("rowSelectionType='radio'", innerTextOrientation='left'),
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '字段示例1',
                                    'dataIndex': '字段示例1'
                                },
                                {
                                    'title': '字段示例2',
                                    'dataIndex': '字段示例2'
                                },
                                {
                                    'title': '字段示例3',
                                    'dataIndex': '字段示例3'
                                }
                            ],
                            data=[
                                {
                                    '字段示例1': i,
                                    '字段示例2': i,
                                    '字段示例3': i
                                }
                                for i in range(5)
                            ],
                            bordered=True,
                            rowSelectionType='radio'
                        ),

                        fac.AntdDivider(
                            '添加行选择功能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdDivider("rowSelectionType='checkbox'", innerTextOrientation='left'),
fac.AntdTable(
    columns=[
        {
            'title': '字段示例1',
            'dataIndex': '字段示例1'
        },
        {
            'title': '字段示例2',
            'dataIndex': '字段示例2'
        },
        {
            'title': '字段示例3',
            'dataIndex': '字段示例3'
        }
    ],
    data=[
        {
            '字段示例1': i,
            '字段示例2': i,
            '字段示例3': i
        }
        for i in range(5)
    ],
    bordered=True,
    rowSelectionType='checkbox',
    containerId='docs-content' # 绑定局部滚动容器以确保悬浮层正常显示
),

fac.AntdDivider("rowSelectionType='radio'", innerTextOrientation='left'),
fac.AntdTable(
    columns=[
        {
            'title': '字段示例1',
            'dataIndex': '字段示例1'
        },
        {
            'title': '字段示例2',
            'dataIndex': '字段示例2'
        },
        {
            'title': '字段示例3',
            'dataIndex': '字段示例3'
        }
    ],
    data=[
        {
            '字段示例1': i,
            '字段示例2': i,
            '字段示例3': i
        }
        for i in range(5)
    ],
    bordered=True,
    rowSelectionType='radio'
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
                    id='添加行选择功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '日期示例',
                                    'dataIndex': '日期示例',
                                    'editable': True,
                                    'width': '50%'
                                },
                                {
                                    'title': '邮编示例',
                                    'dataIndex': '邮编示例',
                                    'editable': True,
                                    'width': '50%'
                                }
                            ],
                            data=[
                                {
                                    'key': i,
                                    '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
                                    '邮编示例': faker.postcode()
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            columnsFormatConstraint={
                                '日期示例': {
                                    'rule': '^\d{4}\-\d{2}\-\d{2}$',
                                    'content': '不符合日期输入格式要求！'
                                },
                                '邮编示例': {
                                    'rule': '^\d{6}$',
                                    'content': '不符合邮编输入格式要求！'
                                }
                            }
                        ),

                        fac.AntdDivider(
                            '添加编辑内容格式校验功能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　利用正则表达式来校验可编辑单元格的内容输入过程，可自定义校验失败提示文字')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTable(
    columns=[
        {
            'title': '日期示例',
            'dataIndex': '日期示例',
            'editable': True,
            'width': '50%'
        },
        {
            'title': '邮编示例',
            'dataIndex': '邮编示例',
            'editable': True,
            'width': '50%'
        }
    ],
    data=[
        {
            'key': i,
            '日期示例': faker.date(pattern="%Y-%m-%d", end_datetime=None),
            '邮编示例': faker.postcode()
        }
        for i in range(10)
    ],
    bordered=True,
    columnsFormatConstraint={
        '日期示例': {
            'rule': '^\d{4}\-\d{2}\-\d{2}$',
            'content': '不符合日期输入格式要求！'
        },
        '邮编示例': {
            'rule': '^\d{6}$',
            'content': '不符合邮编输入格式要求！'
        }
    }
)'''
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
                    id='添加编辑内容格式校验功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTitle('左例（未设置） 右例（设置containerId参数）', level=5),
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
                                        'maxHeight': '400px',
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
                                            containerId='containerId-container-demo'
                                        ),
                                        html.Div(
                                            style={
                                                'height': '400px'
                                            }
                                        )
                                    ],
                                    id='containerId-container-demo',
                                    style={
                                        'flex': '1',
                                        'padding': '20px',
                                        'maxHeight': '400px',
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
                            '妥善使用containerId参数',
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
                                    '组件位于具有局部滚动条的容器中时，点击展开悬浮层后滚动页面会出现悬浮层不跟随移动的情况，因此需要参考本例，利用containerId参数为'
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTitle('左例（未设置） 右例（设置containerId参数）', level=5),
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
                    containerId='containerId-container-demo'
                ),
                html.Div(
                    style={
                        'height': '400px'
                    }
                )
            ],
            id='containerId-container-demo',
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
)'''
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
                    id='妥善使用containerId参数',
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
                            bordered=True,
                            pagination={
                                'pageSize': 5
                            },
                            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                        ),
                        fac.AntdSpin(
                            html.Div(id='table-demo-output'),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '监听翻页、筛选及单元格内容编辑变动',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　这个例子中展示了'),
                                fac.AntdText('AntdTable', strong=True),
                                fac.AntdText('中所有的交互事件被用户触发时所记录的参数变化情况')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
    bordered=True,
    pagination={
        'pageSize': 5
    },
    containerId='docs-content' # 绑定局部滚动容器以确保悬浮层正常显示
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
    ]'''
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
                    id='监听翻页、筛选及单元格内容编辑变动',
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
                                bordered=True,
                                pagination={
                                    'current': 1,
                                    'total': server_side_df.shape[0],
                                    'pageSize': 5,
                                    'pageSizeOptions': [5, 10]
                                },
                                containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
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
        bordered=True,
        pagination={
            'current': 1,
            'total': server_side_df.shape[0],
            'pageSize': 5,
            'pageSizeOptions': [5, 10]
        },
        containerId='docs-content' # 绑定局部滚动容器以确保悬浮层正常显示
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

    return dash.no_update'''
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
                    id='服务端数据渲染模式示例',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            [
                                fac.AntdTable(
                                    id='table-button-click-demo',
                                    columns=[
                                        {
                                            'title': '单按钮示例',
                                            'dataIndex': '单按钮示例',
                                            'renderOptions': {'renderType': 'button'},
                                            'width': '25%'
                                        },
                                        {
                                            'title': '多按钮示例',
                                            'dataIndex': '多按钮示例',
                                            'renderOptions': {'renderType': 'button'},
                                            'width': '50%'
                                        },
                                        {
                                            'title': '气泡确认按钮示例',
                                            'dataIndex': '气泡确认按钮示例',
                                            'renderOptions': {
                                                'renderType': 'button',
                                                'renderButtonPopConfirmProps': {
                                                    'title': '确认操作',
                                                    'okText': '继续',
                                                    'cancelText': '再想想'
                                                }
                                            },
                                            'width': '25%'
                                        }
                                    ],
                                    data=[
                                        {
                                            'key': i,
                                            '单按钮示例': {
                                                'content': '按钮示例',
                                                'type': 'primary'
                                            },
                                            '多按钮示例': [
                                                {
                                                    'content': '按钮示例1',
                                                    'type': 'primary'
                                                },
                                                {
                                                    'content': '按钮示例2',
                                                    'danger': True
                                                }
                                            ],
                                            '气泡确认按钮示例': {
                                                'content': '气泡确认按钮示例',
                                                'type': 'primary'
                                            }
                                        }
                                        for i in range(5)
                                    ],
                                    bordered=True,
                                    containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                                ),

                                fac.AntdSpace(
                                    [
                                        html.Div(
                                            [
                                                fac.AntdText('nClicksButton：', strong=True),
                                                fac.AntdText(
                                                    id='table-button-click-demo-recentlyButtonClickedRow-output')
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                fac.AntdText('recentlyButtonClickedRow：', strong=True),
                                                html.Pre(
                                                    id='table-button-click-demo-nClicksButton-output',
                                                    style={
                                                        'backgroundColor': 'rgb(250, 250, 250)'
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                fac.AntdText('clickedContent：', strong=True),
                                                fac.AntdText(id='table-button-click-demo-clickedContent-output')
                                            ]
                                        )
                                    ],
                                    direction='vertical',
                                    style={
                                        'width': '100%'
                                    }
                                )
                            ],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '监听按钮模式下的按钮点击事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　nClicksButton', strong=True),
                                fac.AntdText('适合作为监听表格按钮点击事件的'),
                                fac.AntdText('Input()触发器', strong=True)
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    [
        fac.AntdTable(
            id='table-button-click-demo',
            columns=[
                {
                    'title': '单按钮示例',
                    'dataIndex': '单按钮示例',
                    'renderOptions': {'renderType': 'button'},
                    'width': '25%'
                },
                {
                    'title': '多按钮示例',
                    'dataIndex': '多按钮示例',
                    'renderOptions': {'renderType': 'button'},
                    'width': '50%'
                },
                {
                    'title': '气泡确认按钮示例',
                    'dataIndex': '气泡确认按钮示例',
                    'renderOptions': {
                        'renderType': 'button',
                        'renderButtonPopConfirmProps': {
                            'title': '确认操作',
                            'okText': '继续',
                            'cancelText': '再想想'
                        }
                    },
                    'width': '25%'
                }
            ],
            data=[
                {
                    'key': i,
                    '单按钮示例': {
                        'content': '按钮示例',
                        'type': 'primary'
                    },
                    '多按钮示例': [
                        {
                            'content': '按钮示例1',
                            'type': 'primary'
                        },
                        {
                            'content': '按钮示例2',
                            'danger': True
                        }
                    ],
                    '气泡确认按钮示例': {
                        'content': '气泡确认按钮示例',
                        'type': 'primary'
                    }
                }
                for i in range(5)
            ],
            bordered=True,
            containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
        ),

        fac.AntdSpace(
            [
                html.Div(
                    [
                        fac.AntdText('nClicksButton：', strong=True),
                        fac.AntdText(
                            id='table-button-click-demo-recentlyButtonClickedRow-output')
                    ]
                ),
                html.Div(
                    [
                        fac.AntdText('recentlyButtonClickedRow：', strong=True),
                        html.Pre(
                            id='table-button-click-demo-nClicksButton-output',
                            style={
                                'backgroundColor': 'rgb(250, 250, 250)'
                            }
                        )
                    ]
                ),
                html.Div(
                    [
                        fac.AntdText('clickedContent：', strong=True),
                        fac.AntdText(id='table-button-click-demo-clickedContent-output')
                    ]
                )
            ],
            direction='vertical',
            style={
                'width': '100%'
            }
        )
    ],
    text='回调中'
)
...
@app.callback(
    [Output('table-button-click-demo-recentlyButtonClickedRow-output', 'children'),
     Output('table-button-click-demo-nClicksButton-output', 'children'),
     Output('table-button-click-demo-clickedContent-output', 'children')],
    Input('table-button-click-demo', 'nClicksButton'),
    [State('table-button-click-demo', 'recentlyButtonClickedRow'),
     State('table-button-click-demo', 'clickedContent')],
    prevent_initial_call=True
)
def table_button_click_demo_callback(nClicksButton, recentlyButtonClickedRow, clickedContent):
    return str(nClicksButton), json.dumps(recentlyButtonClickedRow, ensure_ascii=False, indent=4), str(clickedContent)
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
                    id='监听按钮模式下的按钮点击事件',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            [
                                fac.AntdTable(
                                    id='table-mouse-event-demo',
                                    enableHoverListen=True,
                                    bordered=True,
                                    columns=[
                                        {
                                            'title': '字段1',
                                            'dataIndex': '字段1'
                                        },
                                        {
                                            'title': '字段2',
                                            'dataIndex': '字段2'
                                        },
                                        {
                                            'title': '字段3',
                                            'dataIndex': '字段3'
                                        }
                                    ],
                                    data=[
                                        {
                                            'key': str(i),
                                            '字段1': i,
                                            '字段2': i,
                                            '字段3': i
                                        }
                                        for i in range(5)
                                    ]
                                ),

                                fac.AntdSpace(
                                    id='table-mouse-event-demo-output',
                                    direction='vertical',
                                    style={
                                        'width': '100%'
                                    }
                                )
                            ],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '监听表头/数据行的鼠标移入事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdTable', strong=True),
                                fac.AntdText('的表头/数据行鼠标移入事件监听默认不开启，设置参数'),
                                fac.AntdText('enableHoverListen=True', code=True),
                                fac.AntdText('后会启用相关功能，但同时会与一些其他涉及到鼠标悬浮触发的其他功能相冲突，请慎用！')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    [
        fac.AntdTable(
            id='table-mouse-event-demo',
            enableHoverListen=True,
            bordered=True,
            columns=[
                {
                    'title': '字段1',
                    'dataIndex': '字段1'
                },
                {
                    'title': '字段2',
                    'dataIndex': '字段2'
                },
                {
                    'title': '字段3',
                    'dataIndex': '字段3'
                }
            ],
            data=[
                {
                    'key': str(i),
                    '字段1': i,
                    '字段2': i,
                    '字段3': i
                }
                for i in range(5)
            ]
        ),

        fac.AntdSpace(
            id='table-mouse-event-demo-output',
            direction='vertical',
            style={
                'width': '100%'
            }
        )
    ],
    text='回调中'
)
...

@app.callback(
    Output('table-mouse-event-demo-output', 'children'),
    [Input('table-mouse-event-demo', 'recentlyMouseEnterColumn'),
     Input('table-mouse-event-demo', 'recentlyMouseEnterRow')],
    prevent_initial_call=True
)
def table_mouse_event_demo_callback(recentlyMouseEnterColumn,
                                    recentlyMouseEnterRow):
    return [
        html.Div(
            [
                fac.AntdText('recentlyMouseEnterColumn：', strong=True),
                fac.AntdText(recentlyMouseEnterColumn)
            ]
        ),
        html.Div(
            [
                fac.AntdText('recentlyMouseEnterRow：', strong=True),
                fac.AntdText(recentlyMouseEnterRow)
            ]
        )
    ]
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
                    id='监听表头/数据行的鼠标移入事件',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdSpin(
                            [
                                fac.AntdTable(
                                    id='table-row-select-demo',
                                    columns=[
                                        {
                                            'title': '字段示例1',
                                            'dataIndex': '字段示例1'
                                        },
                                        {
                                            'title': '字段示例2',
                                            'dataIndex': '字段示例2'
                                        },
                                        {
                                            'title': '字段示例3',
                                            'dataIndex': '字段示例3'
                                        }
                                    ],
                                    data=[
                                        {
                                            '字段示例1': i,
                                            '字段示例2': i,
                                            '字段示例3': i
                                        }
                                        for i in range(5)
                                    ],
                                    rowSelectionType='checkbox',
                                    containerId='docs-content'  # 绑定局部滚动容器以确保悬浮层正常显示
                                ),

                                fac.AntdSpace(
                                    [
                                        html.Div(
                                            [
                                                fac.AntdText('selectedRowKeys：', strong=True),
                                                fac.AntdText(id='table-row-select-demo-selectedRowKeys-output')
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                fac.AntdText('selectedRows：', strong=True),
                                                html.Pre(
                                                    id='table-row-select-demo-selectedRows-output',
                                                    style={
                                                        'backgroundColor': 'rgb(250, 250, 250)'
                                                    }
                                                )
                                            ]
                                        )
                                    ],
                                    direction='vertical',
                                    style={
                                        'width': '100%'
                                    }
                                )
                            ],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '监听行选择事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    [
        fac.AntdTable(
            id='table-row-select-demo',
            columns=[
                {
                    'title': '字段示例1',
                    'dataIndex': '字段示例1'
                },
                {
                    'title': '字段示例2',
                    'dataIndex': '字段示例2'
                },
                {
                    'title': '字段示例3',
                    'dataIndex': '字段示例3'
                }
            ],
            data=[
                {
                    '字段示例1': i,
                    '字段示例2': i,
                    '字段示例3': i
                }
                for i in range(5)
            ],
            rowSelectionType='checkbox',
            containerId='docs-content' # 绑定局部滚动容器以确保悬浮层正常显示
        ),

        fac.AntdSpace(
            [
                html.Div(
                    [
                        fac.AntdText('selectedRowKeys：', strong=True),
                        fac.AntdText(id='table-row-select-demo-selectedRowKeys-output')
                    ]
                ),
                html.Div(
                    [
                        fac.AntdText('selectedRows：', strong=True),
                        html.Pre(
                            id='table-row-select-demo-selectedRows-output',
                            style={
                                'backgroundColor': 'rgb(250, 250, 250)'
                            }
                        )
                    ]
                )
            ],
            direction='vertical',
            style={
                'width': '100%'
            }
        )
    ],
    text='回调中'
)
...
@app.callback(
    [Output('table-row-select-demo-selectedRowKeys-output', 'children'),
     Output('table-row-select-demo-selectedRows-output', 'children')],
    [Input('table-row-select-demo', 'selectedRowKeys'),
     Input('table-row-select-demo', 'selectedRows')],
    prevent_initial_call=True
)
def table_row_select_demo_callback(selectedRowKeys, selectedRows):
    return str(selectedRowKeys), json.dumps(selectedRows, ensure_ascii=False, indent=4)
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
                    id='监听行选择事件',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'width': 'calc(100vw - 650px)'
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
                            {'title': '基础的表格', 'href': '#基础的表格'},
                            {'title': '手动分配百分比宽度', 'href': '#手动分配百分比宽度'},
                            {'title': '限定maxHeight开启横向滚动模式', 'href': '#限定maxHeight开启横向滚动模式'},
                            {'title': '限定maxHeight以固定表头', 'href': '#限定maxHeight以固定表头'},
                            {'title': '宽度溢出时固定左侧或右侧指定列', 'href': '#宽度溢出时固定左侧或右侧指定列'},
                            {'title': '指定部分列可编辑', 'href': '#指定部分列可编辑'},
                            {'title': '超长内容省略模式', 'href': '#超长内容省略模式'},
                            {'title': '超链接模式', 'href': '#超链接模式'},
                            {'title': '迷你图模式', 'href': '#迷你图模式'},
                            {'title': '标签模式', 'href': '#标签模式'},
                            {'title': '按钮模式', 'href': '#按钮模式'},
                            {'title': '可复制模式', 'href': '#可复制模式'},
                            {'title': '状态徽标模式', 'href': '#状态徽标模式'},
                            {'title': '分页相关设置', 'href': '#分页相关设置'},
                            {'title': '常规单列排序', 'href': '#常规单列排序'},
                            {'title': '多列组合排序', 'href': '#多列组合排序'},
                            {'title': '使用字段筛选功能', 'href': '#使用字段筛选功能'},
                            {'title': '为表头添加字段说明信息', 'href': '#为表头添加字段说明信息'},
                            {'title': '添加行选择功能', 'href': '#添加行选择功能'},
                            {'title': '添加编辑内容格式校验功能', 'href': '#添加编辑内容格式校验功能'},
                            {'title': '妥善使用containerId参数', 'href': '#妥善使用containerId参数'},
                            {'title': '监听翻页、筛选及单元格内容编辑变动', 'href': '#监听翻页、筛选及单元格内容编辑变动'},
                            {'title': '服务端数据渲染模式示例', 'href': '#服务端数据渲染模式示例'},
                            {'title': '监听按钮模式下的按钮点击事件', 'href': '#监听按钮模式下的按钮点击事件'},
                            {'title': '监听表头/数据行的鼠标移入事件', 'href': '#监听表头/数据行的鼠标移入事件'},
                            {'title': '监听行选择事件', 'href': '#监听行选择事件'},
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200,
                style={
                    'maxHeight': '750px'
                }
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
            return [
                batch_df.iloc[(pagination['current'] - 1) * pagination['pageSize']
                              :
                              pagination['current'] * pagination['pageSize'], :].to_dict('records'),
                {
                    **pagination,
                    **{
                        'current': 1,
                        'pageSize': 5,
                        'total': batch_df.shape[0]
                    }
                }
            ]

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
            {
                **pagination,
                'pageSizeOptions': [5]
            }
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


@app.callback(
    [Output('table-button-click-demo-recentlyButtonClickedRow-output', 'children'),
     Output('table-button-click-demo-nClicksButton-output', 'children'),
     Output('table-button-click-demo-clickedContent-output', 'children')],
    Input('table-button-click-demo', 'nClicksButton'),
    [State('table-button-click-demo', 'recentlyButtonClickedRow'),
     State('table-button-click-demo', 'clickedContent')],
    prevent_initial_call=True
)
def table_button_click_demo_callback(nClicksButton, recentlyButtonClickedRow, clickedContent):
    return str(nClicksButton), json.dumps(recentlyButtonClickedRow, ensure_ascii=False, indent=4), str(clickedContent)


@app.callback(
    [Output('table-row-select-demo-selectedRowKeys-output', 'children'),
     Output('table-row-select-demo-selectedRows-output', 'children')],
    [Input('table-row-select-demo', 'selectedRowKeys'),
     Input('table-row-select-demo', 'selectedRows')],
    prevent_initial_call=True
)
def table_row_select_demo_callback(selectedRowKeys, selectedRows):
    return str(selectedRowKeys), json.dumps(selectedRows, ensure_ascii=False, indent=4)


@app.callback(
    Output('table-mouse-event-demo-output', 'children'),
    [Input('table-mouse-event-demo', 'recentlyMouseEnterColumn'),
     Input('table-mouse-event-demo', 'recentlyMouseEnterRow')],
    prevent_initial_call=True
)
def table_mouse_event_demo_callback(recentlyMouseEnterColumn,
                                    recentlyMouseEnterRow):
    return [
        html.Div(
            [
                fac.AntdText('recentlyMouseEnterColumn：', strong=True),
                fac.AntdText(recentlyMouseEnterColumn)
            ]
        ),
        html.Div(
            [
                fac.AntdText('recentlyMouseEnterRow：', strong=True),
                fac.AntdText(recentlyMouseEnterRow)
            ]
        )
    ]
