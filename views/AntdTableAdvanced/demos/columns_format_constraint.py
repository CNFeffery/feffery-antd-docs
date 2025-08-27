import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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
                    'rule': '^\\d{4}-\\d{2}-\\d{2}$',
                    'content': '不符合日期格式输入要求',
                },
                '纯汉字约束': {
                    'rule': '^[一-龥]+$',
                    'content': '不符合纯汉字输入要求',
                },
            },
        )

    elif current_locale == 'en-us':
        # construct demo contents (dataIndex translated too)
        demo_contents = fac.AntdTable(
            columns=[
                {
                    'title': 'Digits-only Constraint',
                    'dataIndex': 'Digits-only Constraint',
                    'editable': True,
                    'width': '25%',
                },
                {
                    'title': 'Letters-only Constraint',
                    'dataIndex': 'Letters-only Constraint',
                    'editable': True,
                    'width': '25%',
                },
                {
                    'title': 'Date Format Constraint',
                    'dataIndex': 'Date Format Constraint',
                    'editable': True,
                    'width': '25%',
                },
                {
                    'title': 'Chinese-characters-only Constraint',
                    'dataIndex': 'Chinese-characters-only Constraint',
                    'editable': True,
                    'width': '25%',
                },
            ],
            data=[
                {
                    'Digits-only Constraint': '12345',
                    'Letters-only Constraint': 'fac',
                    'Date Format Constraint': '2099-01-01',
                    'Chinese-characters-only Constraint': '测试',
                }
            ],
            columnsFormatConstraint={
                'Digits-only Constraint': {
                    'rule': '^[0-9]+$',
                    'content': 'Input must be digits-only.',
                },
                'Letters-only Constraint': {
                    'rule': '^[a-zA-Z]+$',
                    'content': 'Input must be letters-only.',
                },
                'Date Format Constraint': {
                    'rule': '^\\d{4}-\\d{2}-\\d{2}$',
                    'content': 'Input must match the date format YYYY-MM-DD.',
                },
                'Chinese-characters-only Constraint': {
                    'rule': '^[一-龥]+$',
                    'content': 'Input must be Chinese characters only.',
                },
            },
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
        {'title': '纯数字约束', 'dataIndex': '纯数字约束', 'editable': True, 'width': '25%'},
        {'title': '纯字母约束', 'dataIndex': '纯字母约束', 'editable': True, 'width': '25%'},
        {'title': '日期格式约束', 'dataIndex': '日期格式约束', 'editable': True, 'width': '25%'},
        {'title': '纯汉字约束', 'dataIndex': '纯汉字约束', 'editable': True, 'width': '25%'},
    ],
    data=[
        {'纯数字约束': '12345', '纯字母约束': 'fac', '日期格式约束': '2099-01-01', '纯汉字约束': '测试'}
    ],
    columnsFormatConstraint={
        '纯数字约束': {'rule': '^[0-9]+$', 'content': '不符合纯数字输入要求'},
        '纯字母约束': {'rule': '^[a-zA-Z]+$', 'content': '不符合纯字母输入要求'},
        '日期格式约束': {'rule': '^\\\\d{4}-\\\\d{2}-\\\\d{2}$', 'content': '不符合日期格式输入要求'},
        '纯汉字约束': {'rule': '^[一-龥]+$', 'content': '不符合纯汉字输入要求'},
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
        {'title': 'Digits-only Constraint', 'dataIndex': 'Digits-only Constraint', 'editable': True, 'width': '25%'},
        {'title': 'Letters-only Constraint', 'dataIndex': 'Letters-only Constraint', 'editable': True, 'width': '25%'},
        {'title': 'Date Format Constraint', 'dataIndex': 'Date Format Constraint', 'editable': True, 'width': '25%'},
        {'title': 'Chinese-characters-only Constraint', 'dataIndex': 'Chinese-characters-only Constraint', 'editable': True, 'width': '25%'},
    ],
    data=[
        {'Digits-only Constraint': '12345', 'Letters-only Constraint': 'fac', 'Date Format Constraint': '2099-01-01', 'Chinese-characters-only Constraint': '测试'}
    ],
    columnsFormatConstraint={
        'Digits-only Constraint': {'rule': '^[0-9]+$', 'content': 'Input must be digits-only.'},
        'Letters-only Constraint': {'rule': '^[a-zA-Z]+$', 'content': 'Input must be letters-only.'},
        'Date Format Constraint': {'rule': '^\\\\d{4}-\\\\d{2}-\\\\d{2}$', 'content': 'Input must match the date format YYYY-MM-DD.'},
        'Chinese-characters-only Constraint': {'rule': '^[一-龥]+$', 'content': 'Input must be Chinese characters only.'},
    },
)
"""
            }
        ]
