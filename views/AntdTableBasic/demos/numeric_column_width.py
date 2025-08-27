import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = [
            fac.AntdTable(
                columns=[
                    {"title": f"字段{i}", "dataIndex": f"字段{i}", "width": width}
                    for i, width in zip(range(1, 6), [50, 100, 50, 100, 50])
                ],
                data=[{f"字段{i}": "示例内容" for i in range(1, 6)}] * 3,
            ),
            fac.AntdTable(
                columns=[
                    {"title": f"字段{i}", "dataIndex": f"字段{i}", "width": width}
                    for i, width in zip(range(1, 6), [5000, 10000, 5000, 10000, 5000])
                ],
                data=[{f"字段{i}": "示例内容" for i in range(1, 6)}] * 3,
            ),
        ]

    elif current_locale == "en-us":
        demo_contents = [
            fac.AntdTable(
                columns=[
                    {"title": f"Field {i}", "dataIndex": f"Field {i}", "width": width}
                    for i, width in zip(range(1, 6), [50, 100, 50, 100, 50])
                ],
                data=[{f"Field {i}": "Example Content" for i in range(1, 6)}] * 3,
                locale="en-us",
            ),
            fac.AntdTable(
                columns=[
                    {"title": f"Field {i}", "dataIndex": f"Field {i}", "width": width}
                    for i, width in zip(range(1, 6), [5000, 10000, 5000, 10000, 5000])
                ],
                data=[{f"Field {i}": "Example Content" for i in range(1, 6)}] * 3,
                locale="en-us",
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
[
    fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': width}
            for i, width in zip(range(1, 6), [50, 100, 50, 100, 50])
        ],
        data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
    ),
    fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': width}
            for i, width in zip(
                range(1, 6), [5000, 10000, 5000, 10000, 5000]
            )
        ],
        data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
    ),
]
"""
            }
        ]

    elif current_locale == "en-us":
        return [
            {
                "code": """
[
    fac.AntdTable(
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': width}
            for i, width in zip(range(1, 6), [50, 100, 50, 100, 50])
        ],
        data=[{f'Field {i}': 'Example Content' for i in range(1, 6)}] * 3,
    ),
    fac.AntdTable(
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': width}
            for i, width in zip(
                range(1, 6), [5000, 10000, 5000, 10000, 5000]
            )
        ],
        data=[{f'Field {i}': 'Example Content' for i in range(1, 6)}] * 3,
    ),
]
"""
            }
        ]
