import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == 'zh-cn':
        col = lambda i: f'字段{i}'
        cell = '示例内容'
        pop_title = lambda i: f'字段{i}说明'
        pop_content = lambda i: f'这是字段{i}的说明巴拉巴拉巴拉'
    else:  # en-us fallback
        col = lambda i: f'Field {i}'
        cell = 'Sample Content'
        pop_title = lambda i: f'About Field {i}'
        pop_content = (
            lambda i: f'This is a description for Field {i} (placeholder).'
        )

    columns = [{'title': col(i), 'dataIndex': col(i)} for i in range(1, 6)]
    data = [
        {**{col(i): cell for i in range(1, 6)}, 'key': f'row-{row + 1}'}
        for row in range(3)
    ]

    title_popover_info = {
        col(i): {
            'title': pop_title(i),
            'content': pop_content(i),
            'placement': 'top',
        }
        for i in range(1, 6)
    }

    demo_contents = fac.AntdTable(
        columns=columns,
        data=data,
        titlePopoverInfo=title_popover_info,
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
        {'title': f'字段{i}', 'dataIndex': f'字段{i}'} for i in range(1, 6)
    ],
    data=[
        {
            **{f'字段{i}': '示例内容' for i in range(1, 6)},
            'key': f'row-{row+1}',
        }
        for row in range(3)
    ],
    titlePopoverInfo={
        f'字段{i}': {
            'title': f'字段{i}说明',
            'content': f'这是字段{i}的说明巴拉巴拉巴拉',
            'placement': 'top',
        }
        for i in range(1, 6)
    },
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
        {'title': f'Field {i}', 'dataIndex': f'Field {i}'} for i in range(1, 6)
    ],
    data=[
        {
            **{f'Field {i}': 'Sample Content' for i in range(1, 6)},
            'key': f'row-{row+1}',
        }
        for row in range(3)
    ],
    titlePopoverInfo={
        f'Field {i}': {
            'title': f'About Field {i}',
            'content': f'This is a description for Field {i} (placeholder).',
            'placement': 'top',
        }
        for i in range(1, 6)
    },
)
"""
            }
        ]
