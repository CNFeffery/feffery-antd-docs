import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        titles = [
            '基础示例',
            '自定义选项',
            '单选模式',
            '启用搜索框',
            '树形筛选',
        ]
        keys = titles
    elif current_locale == 'en-us':
        titles = [
            'Basic Example',
            'Custom Options',
            'Single Selection',
            'Enable Search Box',
            'Tree Filter',
        ]
        keys = titles
    else:
        titles = [
            '基础示例',
            '自定义选项',
            '单选模式',
            '启用搜索框',
            '树形筛选',
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
        keys[4]: {
            'filterMode': 'tree',
            'filterCustomTreeItems': [
                {
                    'text': 'a-c',
                    'children': [{'text': s, 'value': s} for s in list('abc')],
                },
                {'text': 'd', 'value': 'd'},
                {'text': 'e', 'value': 'e'},
            ],
        },
    }

    demo_contents = fac.AntdTable(
        columns=columns, data=data, filterOptions=filter_options
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {'title': '基础示例', 'dataIndex': '基础示例', 'width': '20%'},
        {'title': '自定义选项', 'dataIndex': '自定义选项', 'width': '20%'},
        {'title': '单选模式', 'dataIndex': '单选模式', 'width': '20%'},
        {'title': '启用搜索框', 'dataIndex': '启用搜索框', 'width': '20%'},
        {'title': '树形筛选', 'dataIndex': '树形筛选', 'width': '20%'},
    ],
    data=[
        {
            '基础示例': s,
            '自定义选项': s,
            '单选模式': s,
            '启用搜索框': s,
            '树形筛选': s,
        }
        for s in list('abced')
    ],
    filterOptions={
        '基础示例': {},
        '自定义选项': {'filterCustomItems': list('abcdefghijk')},
        '单选模式': {'filterMultiple': False},
        '启用搜索框': {'filterSearch': True},
        '树形筛选': {
            'filterMode': 'tree',
            'filterCustomTreeItems': [
                {'text': 'a-c', 'children': [{'text': s, 'value': s} for s in list('abc')]},
                {'text': 'd', 'value': 'd'},
                {'text': 'e', 'value': 'e'},
            ],
        },
    },
)
"""
            }
        ]
    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {'title': 'Basic Example', 'dataIndex': 'Basic Example', 'width': '20%'},
        {'title': 'Custom Options', 'dataIndex': 'Custom Options', 'width': '20%'},
        {'title': 'Single Selection', 'dataIndex': 'Single Selection', 'width': '20%'},
        {'title': 'Enable Search Box', 'dataIndex': 'Enable Search Box', 'width': '20%'},
        {'title': 'Tree Filter', 'dataIndex': 'Tree Filter', 'width': '20%'},
    ],
    data=[
        {
            'Basic Example': s,
            'Custom Options': s,
            'Single Selection': s,
            'Enable Search Box': s,
            'Tree Filter': s,
        }
        for s in list('abced')
    ],
    filterOptions={
        'Basic Example': {},
        'Custom Options': {'filterCustomItems': list('abcdefghijk')},
        'Single Selection': {'filterMultiple': False},
        'Enable Search Box': {'filterSearch': True},
        'Tree Filter': {
            'filterMode': 'tree',
            'filterCustomTreeItems': [
                {'text': 'a-c', 'children': [{'text': s, 'value': s} for s in list('abc')]},
                {'text': 'd', 'value': 'd'},
                {'text': 'e', 'value': 'e'},
            ],
        },
    },
)
"""
            }
        ]
