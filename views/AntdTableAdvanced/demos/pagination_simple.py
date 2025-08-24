import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        title = lambda i: f"字段{i}"
        key = lambda i: f"字段{i}"
        cell = "示例内容"
    else:  # en-us fallback
        title = lambda i: f"Field {i}"
        key = lambda i: f"Field {i}"
        cell = "Sample Content"

    demo_contents = fac.AntdTable(
        columns=[
            {"title": title(i), "dataIndex": key(i), "width": "20%"}
            for i in range(1, 6)
        ],
        data=[{key(i): cell for i in range(1, 6)}] * 10,
        pagination={"pageSize": 2, "simple": True},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 10,
    pagination={'pageSize': 2, 'simple': True},
)
"""
            }
        ]
    else:  # en-us
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    data=[{f'Field {i}': 'Sample Content' for i in range(1, 6)}] * 10,
    pagination={'pageSize': 2, 'simple': True},
)
"""
            }
        ]
