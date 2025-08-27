import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = [
            html.Div(
                fac.AntdTable(
                    columns=[
                        {"title": f"字段{i}", "dataIndex": f"字段{i}"}
                        for i in range(1, 6)
                    ],
                    data=[{f"字段{i}": "示例内容" for i in range(1, 6)}] * 3,
                    maxWidth=900,
                    title="maxWidth=900",
                ),
                style={"maxWidth": 700, "margin": "0 auto"},
            ),
            fac.AntdTable(
                columns=[
                    {"title": f"字段{i}", "dataIndex": f"字段{i}"} for i in range(1, 6)
                ],
                data=[{f"字段{i}": "示例内容" * 4 for i in range(1, 6)}] * 3,
                maxWidth="max-content",
                title='maxWidth="max-content"',
            ),
        ]

    elif current_locale == "en-us":
        demo_contents = [
            html.Div(
                fac.AntdTable(
                    columns=[
                        {"title": f"Field {i}", "dataIndex": f"Field {i}"}
                        for i in range(1, 6)
                    ],
                    data=[{f"Field {i}": "Example Content" for i in range(1, 6)}] * 3,
                    maxWidth=900,
                    title="maxWidth=900",
                    locale="en-us",
                ),
                style={"maxWidth": 700, "margin": "0 auto"},
            ),
            fac.AntdTable(
                columns=[
                    {"title": f"Field {i}", "dataIndex": f"Field {i}"}
                    for i in range(1, 6)
                ],
                data=[{f"Field {i}": "Example Content" * 4 for i in range(1, 6)}] * 3,
                maxWidth="max-content",
                title='maxWidth="max-content"',
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
    html.Div(
        fac.AntdTable(
            columns=[
                {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
            maxWidth=900,
            title='maxWidth=900',
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
            for i in range(1, 6)
        ],
        data=[{f'字段{i}': '示例内容' * 4 for i in range(1, 6)}] * 3,
        maxWidth='max-content',
        title='maxWidth="max-content"',
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
    html.Div(
        fac.AntdTable(
            columns=[
                {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
                for i in range(1, 6)
            ],
            data=[{f'Field {i}': 'Example Content' for i in range(1, 6)}] * 3,
            maxWidth=900,
            title='maxWidth=900',
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdTable(
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
            for i in range(1, 6)
        ],
        data=[{f'Field {i}': 'Example Content' * 4 for i in range(1, 6)}] * 3,
        maxWidth='max-content',
        title='maxWidth="max-content"',
    ),
]
"""
            }
        ]
