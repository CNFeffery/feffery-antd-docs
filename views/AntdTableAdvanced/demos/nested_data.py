import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        title = lambda i: f"字段{i}"
        data_key = lambda i: f"字段{i}"
        level1 = "第一层"
        level2 = "第二层"
    else:  # en-us fallback
        title = lambda i: f"Field {i}"
        data_key = lambda i: f"Field {i}"
        level1 = "First Level"
        level2 = "Second Level"

    demo_contents = fac.AntdTable(
        columns=[
            {"title": title(i), "dataIndex": data_key(i), "width": "calc(100% / 3)"}
            for i in range(1, 4)
        ],
        data=[
            {
                "key": f"row-{i}",
                data_key(1): level1,
                data_key(2): level1,
                data_key(3): level1,
                "children": [
                    {
                        "key": f"row-{i}{j}",
                        data_key(1): level2,
                        data_key(2): level2,
                        data_key(3): level2,
                    }
                    for j in range(3)
                ],
            }
            for i in range(3)
        ],
        bordered=True,
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': 'calc(100% / 3)'}
        for i in range(1, 4)
    ],
    data=[
        {
            'key': f'row-{i}',
            '字段1': '第一层',
            '字段2': '第一层',
            '字段3': '第一层',
            'children': [
                {
                    'key': f'row-{i}{j}',
                    '字段1': '第二层',
                    '字段2': '第二层',
                    '字段3': '第二层',
                }
                for j in range(3)
            ],
        }
        for i in range(3)
    ],
    bordered=True,
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
        {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': 'calc(100% / 3)'}
        for i in range(1, 4)
    ],
    data=[
        {
            'key': f'row-{i}',
            'Field 1': 'First Level',
            'Field 2': 'First Level',
            'Field 3': 'First Level',
            'children': [
                {
                    'key': f'row-{i}{j}',
                    'Field 1': 'Second Level',
                    'Field 2': 'Second Level',
                    'Field 3': 'Second Level',
                }
                for j in range(3)
            ],
        }
        for i in range(3)
    ],
    bordered=True,
)
"""
            }
        ]
