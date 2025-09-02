import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == 'zh-cn':
        col = lambda i: f'字段{i}'
        grp = '组1'
        cell = lambda i: f'示例内容{i}'
        summary = [
            {'content': '第1列总结', 'align': 'center'},
            {'content': '第2到3列总结', 'colSpan': 2, 'align': 'center'},
            {'content': '第4列总结', 'align': 'center'},
            {'content': '第5到6列总结', 'colSpan': 2, 'align': 'center'},
            {'content': 'xxx', 'align': 'center'},
            {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
            {'content': 'xxx', 'align': 'center'},
            {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
        ]
    else:  # en-us fallback
        col = lambda i: f'Field {i}'
        grp = 'Group 1'
        cell = lambda i: f'Sample Content {i}'
        summary = [
            {'content': 'Summary of Col 1', 'align': 'center'},
            {'content': 'Summary of Cols 2–3', 'colSpan': 2, 'align': 'center'},
            {'content': 'Summary of Col 4', 'align': 'center'},
            {'content': 'Summary of Cols 5–6', 'colSpan': 2, 'align': 'center'},
            {'content': 'xxx', 'align': 'center'},
            {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
            {'content': 'xxx', 'align': 'center'},
            {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
        ]

    columns = [
        {'title': col(1), 'dataIndex': col(1)},
        {'title': col(2), 'dataIndex': col(2)},
        {'title': col(3), 'dataIndex': col(3), 'group': grp},
        {'title': col(4), 'dataIndex': col(4), 'group': grp},
        {'title': col(5), 'dataIndex': col(5)},
        {'title': col(6), 'dataIndex': col(6)},
    ]

    data = [{col(i): cell(i) for i in range(1, 7)}] * 5

    demo_contents = fac.AntdTable(
        columns=columns,
        data=data,
        bordered=True,
        summaryRowContents=summary,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {'title': '字段1', 'dataIndex': '字段1'},
        {'title': '字段2', 'dataIndex': '字段2'},
        {'title': '字段3', 'dataIndex': '字段3', 'group': '组1'},
        {'title': '字段4', 'dataIndex': '字段4', 'group': '组1'},
        {'title': '字段5', 'dataIndex': '字段5'},
        {'title': '字段6', 'dataIndex': '字段6'},
    ],
    data=[{f'字段{i}': f'示例内容{i}' for i in range(1, 7)}] * 5,
    bordered=True,
    summaryRowContents=[
        {'content': '第1列总结', 'align': 'center'},
        {'content': '第2到3列总结', 'colSpan': 2, 'align': 'center'},
        {'content': '第4列总结', 'align': 'center'},
        {'content': '第5到6列总结', 'colSpan': 2, 'align': 'center'},
        {'content': 'xxx', 'align': 'center'},
        {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
        {'content': 'xxx', 'align': 'center'},
        {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
    ],
)
"""
            }
        ]
    else:  # en-us
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {'title': 'Field 1', 'dataIndex': 'Field 1'},
        {'title': 'Field 2', 'dataIndex': 'Field 2'},
        {'title': 'Field 3', 'dataIndex': 'Field 3', 'group': 'Group 1'},
        {'title': 'Field 4', 'dataIndex': 'Field 4', 'group': 'Group 1'},
        {'title': 'Field 5', 'dataIndex': 'Field 5'},
        {'title': 'Field 6', 'dataIndex': 'Field 6'},
    ],
    data=[{f'Field {i}': f'Sample Content {i}' for i in range(1, 7)}] * 5,
    bordered=True,
    summaryRowContents=[
        {'content': 'Summary of Col 1', 'align': 'center'},
        {'content': 'Summary of Cols 2–3', 'colSpan': 2, 'align': 'center'},
        {'content': 'Summary of Col 4', 'align': 'center'},
        {'content': 'Summary of Cols 5–6', 'colSpan': 2, 'align': 'center'},
        {'content': 'xxx', 'align': 'center'},
        {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
        {'content': 'xxx', 'align': 'center'},
        {'content': 'xxx', 'colSpan': 2, 'align': 'center'},
    ],
)
"""
            }
        ]
