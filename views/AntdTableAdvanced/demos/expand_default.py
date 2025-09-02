import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        title = lambda i: f'字段{i}'
        data_key = lambda i: f'字段{i}'
        btn_text = lambda i: f'第{i}行展开内容示例'
    elif current_locale == 'en-us':
        title = lambda i: f'Field {i}'
        data_key = lambda i: f'Field {i}'
        btn_text = lambda i: f'Expanded content for row {i}'
    else:
        title = lambda i: f'字段{i}'
        data_key = lambda i: f'字段{i}'
        btn_text = lambda i: f'第{i}行展开内容示例'

    demo_contents = fac.AntdTable(
        columns=[
            {'title': title(i), 'dataIndex': data_key(i), 'width': 400}
            for i in range(5)
        ],
        data=[
            {**{data_key(j): i for j in range(5)}, 'key': f'row-{i}'}
            for i in range(10)
        ],
        bordered=True,
        expandedRowKeyToContent=[
            {
                'key': f'row-{i}',
                'content': fac.AntdButton(btn_text(i), type='primary'),
            }
            for i in range(0, 10, 2)
        ],
        defaultExpandedRowKeys=['row-2', 'row-6'],
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
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': 400}
        for i in range(5)
    ],
    data=[
        {**{f'字段{j}': i for j in range(5)}, 'key': f'row-{i}'}
        for i in range(10)
    ],
    bordered=True,
    expandedRowKeyToContent=[
        {
            'key': f'row-{i}',
            'content': fac.AntdButton(
                f'第{i}行展开内容示例', type='primary'
            ),
        }
        for i in range(0, 10, 2)
    ],
    defaultExpandedRowKeys=['row-2', 'row-6'],
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
        {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': 400}
        for i in range(5)
    ],
    data=[
        {**{f'Field {j}': i for j in range(5)}, 'key': f'row-{i}'}
        for i in range(10)
    ],
    bordered=True,
    expandedRowKeyToContent=[
        {
            'key': f'row-{i}',
            'content': fac.AntdButton(
                f'Expanded content for row {i}', type='primary'
            ),
        }
        for i in range(0, 10, 2)
    ],
    defaultExpandedRowKeys=['row-2', 'row-6'],
)
"""
            }
        ]
