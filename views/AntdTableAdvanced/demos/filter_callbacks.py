import json

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 列名 & 键
        titles = [
            '基础示例',
            '自定义选项',
            '单选模式',
            '启用搜索框',
            '搜索型筛选',
        ]
        keys = titles  # 与标题一致
    elif current_locale == 'en-us':
        titles = [
            'Basic Example',
            'Custom Options',
            'Single Selection',
            'Enable Search Box',
            'Search Filter',
        ]
        keys = titles
    else:
        titles = [
            '基础示例',
            '自定义选项',
            '单选模式',
            '启用搜索框',
            '搜索型筛选',
        ]
        keys = titles

    columns = [
        {'title': t, 'dataIndex': k, 'width': '20%'}
        for t, k in zip(titles, keys)
    ]
    data = [
        {keys[0]: s, keys[1]: s, keys[2]: s, keys[3]: s, keys[4]: s}
        for s in list('abced')
    ]
    filter_options = {
        keys[0]: {},
        keys[1]: {'filterCustomItems': list('abcdefghijk')},
        keys[2]: {'filterMultiple': False},
        keys[3]: {'filterSearch': True},
        keys[4]: {'filterMode': 'keyword'},
    }

    demo_contents = [
        fac.AntdTable(
            id='table-filter-demo',
            columns=columns,
            data=data,
            filterOptions=filter_options,
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


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdTable(
        id='table-filter-demo',
        columns=[
            {'title': '基础示例', 'dataIndex': '基础示例', 'width': '20%'},
            {'title': '自定义选项', 'dataIndex': '自定义选项', 'width': '20%'},
            {'title': '单选模式', 'dataIndex': '单选模式', 'width': '20%'},
            {'title': '启用搜索框', 'dataIndex': '启用搜索框', 'width': '20%'},
            {'title': '搜索型筛选', 'dataIndex': '搜索型筛选', 'width': '20%'},
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
        filterOptions={{
            '基础示例': {{}},
            '自定义选项': {{'filterCustomItems': list('abcdefghijk')}},
            '单选模式': {{'filterMultiple': False}},
            '启用搜索框': {{'filterSearch': True}},
            '搜索型筛选': {{'filterMode': 'keyword'}},
        }},
    ),
    html.Pre(id='table-filter-demo-output'),
]

# ...

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
    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdTable(
        id='table-filter-demo',
        columns=[
            {'title': 'Basic Example', 'dataIndex': 'Basic Example', 'width': '20%'},
            {'title': 'Custom Options', 'dataIndex': 'Custom Options', 'width': '20%'},
            {'title': 'Single Selection', 'dataIndex': 'Single Selection', 'width': '20%'},
            {'title': 'Enable Search Box', 'dataIndex': 'Enable Search Box', 'width': '20%'},
            {'title': 'Search Filter', 'dataIndex': 'Search Filter', 'width': '20%'},
        ],
        data=[
            {
                'Basic Example': s,
                'Custom Options': s,
                'Single Selection': s,
                'Enable Search Box': s,
                'Search Filter': s,
            }
            for s in list('abced')
        ],
        filterOptions={{
            'Basic Example': {{}},
            'Custom Options': {{'filterCustomItems': list('abcdefghijk')}},
            'Single Selection': {{'filterMultiple': False}},
            'Enable Search Box': {{'filterSearch': True}},
            'Search Filter': {{'filterMode': 'keyword'}},
        }},
    ),
    html.Pre(id='table-filter-demo-output'),
]

# ...

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
