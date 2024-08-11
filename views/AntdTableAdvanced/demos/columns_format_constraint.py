import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': '纯数字约束',
                'dataIndex': '纯数字约束',
                'editable': True,
                'width': '25%',
            },
            {
                'title': '纯字母约束',
                'dataIndex': '纯字母约束',
                'editable': True,
                'width': '25%',
            },
            {
                'title': '日期格式约束',
                'dataIndex': '日期格式约束',
                'editable': True,
                'width': '25%',
            },
            {
                'title': '纯汉字约束',
                'dataIndex': '纯汉字约束',
                'editable': True,
                'width': '25%',
            },
        ],
        data=[
            {
                '纯数字约束': '12345',
                '纯字母约束': 'fac',
                '日期格式约束': '2099-01-01',
                '纯汉字约束': '测试',
            }
        ],
        columnsFormatConstraint={
            '纯数字约束': {
                'rule': '^[0-9]+$',
                'content': '不符合纯数字输入要求',
            },
            '纯字母约束': {
                'rule': '^[a-zA-Z]+$',
                'content': '不符合纯字母输入要求',
            },
            '日期格式约束': {
                'rule': '^\d{4}-\d{2}-\d{2}$',
                'content': '不符合日期格式输入要求',
            },
            '纯汉字约束': {
                'rule': '^[一-龥]+$',
                'content': '不符合纯汉字输入要求',
            },
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': '纯数字约束',
            'dataIndex': '纯数字约束',
            'editable': True,
            'width': '25%',
        },
        {
            'title': '纯字母约束',
            'dataIndex': '纯字母约束',
            'editable': True,
            'width': '25%',
        },
        {
            'title': '日期格式约束',
            'dataIndex': '日期格式约束',
            'editable': True,
            'width': '25%',
        },
        {
            'title': '纯汉字约束',
            'dataIndex': '纯汉字约束',
            'editable': True,
            'width': '25%',
        },
    ],
    data=[
        {
            '纯数字约束': '12345',
            '纯字母约束': 'fac',
            '日期格式约束': '2099-01-01',
            '纯汉字约束': '测试',
        }
    ],
    columnsFormatConstraint={
        '纯数字约束': {
            'rule': '^[0-9]+$',
            'content': '不符合纯数字输入要求',
        },
        '纯字母约束': {
            'rule': '^[a-zA-Z]+$',
            'content': '不符合纯字母输入要求',
        },
        '日期格式约束': {
            'rule': '^\d{4}-\d{2}-\d{2}$',
            'content': '不符合日期格式输入要求',
        },
        '纯汉字约束': {
            'rule': '^[一-龥]+$',
            'content': '不符合纯汉字输入要求',
        },
    },
)
"""
    }
]
