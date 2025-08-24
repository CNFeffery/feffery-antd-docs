import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        div_top = "showLessItems=False（默认）"
        div_bottom = "showLessItems=True"
        title = lambda i: f"字段{i}"
        key = lambda i: f"字段{i}"
        cell = "示例内容"
    else:  # en-us fallback
        div_top = "showLessItems=False (default)"
        div_bottom = "showLessItems=True"
        title = lambda i: f"Field {i}"
        key = lambda i: f"Field {i}"
        cell = "Sample Content"

    table_cols = [
        {"title": title(i), "dataIndex": key(i), "width": "20%"} for i in range(1, 6)
    ]
    table_data = [{key(i): cell for i in range(1, 6)}] * 20

    demo_contents = [
        fac.AntdDivider(div_top, innerTextOrientation="left"),
        fac.AntdTable(
            columns=table_cols,
            data=table_data,
            pagination={"pageSize": 2, "current": 5},
        ),
        fac.AntdDivider(div_bottom, innerTextOrientation="left"),
        fac.AntdTable(
            columns=table_cols,
            data=table_data,
            pagination={"pageSize": 2, "showLessItems": True, "current": 5},
        ),
    ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
[
    fac.AntdDivider('showLessItems=False（默认）', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 20,
        pagination={'pageSize': 2, 'current': 5},
    ),
    fac.AntdDivider('showLessItems=True', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 20,
        pagination={'pageSize': 2, 'showLessItems': True, 'current': 5},
    ),
]
"""
            }
        ]
    else:  # en-us
        return [
            {
                "code": """
[
    fac.AntdDivider('showLessItems=False (default)', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[{f'Field {i}': 'Sample Content' for i in range(1, 6)}] * 20,
        pagination={'pageSize': 2, 'current': 5},
    ),
    fac.AntdDivider('showLessItems=True', innerTextOrientation='left'),
    fac.AntdTable(
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[{f'Field {i}': 'Sample Content' for i in range(1, 6)}] * 20,
        pagination={'pageSize': 2, 'showLessItems': True, 'current': 5},
    ),
]
"""
            }
        ]
