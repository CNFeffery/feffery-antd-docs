import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
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
                    {
                        'text': 'a-c',
                        'children': [
                            {'text': s, 'value': s} for s in list('abc')
                        ],
                    },
                    {'text': 'd', 'value': 'd'},
                    {'text': 'e', 'value': 'e'},
                ],
            },
        },
    )

    return demo_contents


code_string = [
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
                {
                    'text': 'a-c',
                    'children': [
                        {'text': s, 'value': s} for s in list('abc')
                    ],
                },
                {'text': 'd', 'value': 'd'},
                {'text': 'e', 'value': 'e'},
            ],
        },
    },
)
"""
    }
]
