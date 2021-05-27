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
            'AntdAnchor(id, className, style, *args, **kwargs)',
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
                        {'title': '锚点示例', 'href': '#锚点示例'}
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

        dcc.Markdown(open('documents/AntdAnchor.md', encoding='utf-8').read(),
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
                    '锚点示例：',
                    id='锚点示例',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdAnchor(
                    linkDict=[
                        {'title': '示例2-1', 'href': '#示例2-1'},
                        {'title': '示例2-1-1', 'href': '#示例2-1-1'},
                        {'title': '示例2-1-2', 'href': '#示例示例2-1-2'},
                        {'title': '示例2-2', 'href': '#示例2-2'},
                    ],
                    align='left'
                ),
                html.Div(
                    [
                        html.H5('示例2-1', id='示例2-1', style={'marginBottom': '500px'}),
                        html.H5('示例2-1-1', id='示例2-1-1', style={'marginBottom': '500px'}),
                        html.H5('示例2-1-2', id='示例2-1-2', style={'marginBottom': '500px'}),
                        html.H5('示例2-2', id='示例2-2', style={'marginBottom': '500px'}),
                    ]
                )
                ```
                '''),

                fac.AntdAnchor(
                    linkDict=[
                        {'title': '示例2-1', 'href': '#示例2-1'},
                        {'title': '示例2-1-1', 'href': '#示例2-1-1'},
                        {'title': '示例2-1-2', 'href': '#示例示例2-1-2'},
                        {'title': '示例2-2', 'href': '#示例2-2'},
                    ],
                    align='left'
                ),
                html.Div(
                    [
                        html.H5('示例2-1', id='示例2-1', style={'marginBottom': '500px'}),
                        html.H5('示例2-1-1', id='示例2-1-1', style={'marginBottom': '500px'}),
                        html.H5('示例2-1-2', id='示例2-1-2', style={'marginBottom': '500px'}),
                        html.H5('示例2-2', id='示例2-2', style={'marginBottom': '500px'}),
                    ]
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
