import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == 'zh-cn':
        col = lambda i: f'字段{i}'
        cell = '示例内容'
        table_title = '请点击本示例下方的“在新窗口打开”按钮，以查看无页首遮挡干扰的完整效果。'
    else:  # en-us fallback
        col = lambda i: f'Field {i}'
        cell = 'Sample Content'
        table_title = 'Click the “Open in new window” button below to view the full effect without the header overlapping.'

    demo_contents = fac.AntdTable(
        columns=[{'title': col(i), 'dataIndex': col(i)} for i in range(1, 4)],
        data=[{col(i): cell for i in range(1, 4)} for _ in range(30)],
        sticky=True,
        size='large',
        pagination={'pageSize': 999},
        title=table_title,
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
        {'title': f'字段{i}', 'dataIndex': f'字段{i}'} for i in range(1, 4)
    ],
    data=[
        {f'字段{i}': '示例内容' for i in range(1, 4)} for row in range(30)
    ],
    sticky=True,
    size='large',
    pagination={'pageSize': 999},
    title='请点击本示例下方的“在新窗口打开”按钮，以查看无页首遮挡干扰的完整效果。',
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
        {'title': f'Field {i}', 'dataIndex': f'Field {i}'} for i in range(1, 4)
    ],
    data=[
        {f'Field {i}': 'Sample Content' for i in range(1, 4)} for _ in range(30)
    ],
    sticky=True,
    size='large',
    pagination={'pageSize': 999},
    title='Click the “Open in new window” button below to view the full effect without the header overlapping.',
)
"""
            }
        ]
