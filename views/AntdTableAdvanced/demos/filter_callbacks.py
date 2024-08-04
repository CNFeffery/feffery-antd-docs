import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTable(
            id='table-filter-demo',
            columns=[
                {'title': '基础示例', 'dataIndex': '基础示例', 'width': '20%'},
                {
                    'title': '自定义选项',
                    'dataIndex': '自定义选项',
                    'width': '20%',
                },
                {'title': '单选模式', 'dataIndex': '单选模式', 'width': '20%'},
                {
                    'title': '启用搜索框',
                    'dataIndex': '启用搜索框',
                    'width': '20%',
                },
                {
                    'title': '搜索型筛选',
                    'dataIndex': '搜索型筛选',
                    'width': '20%',
                },
            ],
            data=[
                {
                    '基础示例': s,
                    '自定义选项': s,
                    '单选模式': s,
                    '启用搜索框': s,
                    '搜索型筛选': s,
                }
                for s in list('abced')
            ],
            filterOptions={
                '基础示例': {},
                '自定义选项': {'filterCustomItems': list('abcdefghijk')},
                '单选模式': {'filterMultiple': False},
                '启用搜索框': {'filterSearch': True},
                '搜索型筛选': {'filterMode': 'keyword'},
            },
        ),
        html.Pre(id='table-filter-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('table-filter-demo-output', 'children'),
    Input('table-filter-demo', 'filter'),
    prevent_initial_call=True,
)
def table_filter_demo(filter_):
    return json.dumps(filter_, indent=4, ensure_ascii=False)


code_string = [
    {
        'code': """
[
    fac.AntdTable(
        id='table-filter-demo',
        columns=[
            {'title': '基础示例', 'dataIndex': '基础示例', 'width': '20%'},
            {
                'title': '自定义选项',
                'dataIndex': '自定义选项',
                'width': '20%',
            },
            {'title': '单选模式', 'dataIndex': '单选模式', 'width': '20%'},
            {
                'title': '启用搜索框',
                'dataIndex': '启用搜索框',
                'width': '20%',
            },
            {
                'title': '搜索型筛选',
                'dataIndex': '搜索型筛选',
                'width': '20%',
            },
        ],
        data=[
            {
                '基础示例': s,
                '自定义选项': s,
                '单选模式': s,
                '启用搜索框': s,
                '搜索型筛选': s,
            }
            for s in list('abced')
        ],
        filterOptions={
            '基础示例': {},
            '自定义选项': {'filterCustomItems': list('abcdefghijk')},
            '单选模式': {'filterMultiple': False},
            '启用搜索框': {'filterSearch': True},
            '搜索型筛选': {'filterMode': 'keyword'},
        },
    ),
    html.Pre(id='table-filter-demo-output'),
]

...

@app.callback(
    Output('table-filter-demo-output', 'children'),
    Input('table-filter-demo', 'filter'),
    prevent_initial_call=True,
)
def table_filter_demo(filter_):
    return json.dumps(filter_, indent=4, ensure_ascii=False)
"""
    }
]
