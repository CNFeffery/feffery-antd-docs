import random

import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        label = lambda i: f"字段{i}"
    else:  # en-us fallback
        label = lambda i: f"Field {i}"

    columns = [
        {"title": label(i), "dataIndex": label(i), "width": "20%"} for i in range(1, 6)
    ]
    data = [{label(j): random.randint(1, 4) for j in range(1, 6)} for _ in range(10)]
    sort_data_indexes = [label(1), label(2), label(4), label(5)]

    demo_contents = fac.AntdTable(
        columns=columns,
        data=data,
        bordered=True,
        sortOptions={
            "sortDataIndexes": sort_data_indexes,
            "multiple": "auto",
        },
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
import random
import feffery_antd_components as fac

fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    data=[
        {f'字段{j}': random.randint(1, 4) for j in range(1, 6)}
        for _ in range(10)
    ],
    bordered=True,
    sortOptions={
        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
        'multiple': 'auto',
    },
)
"""
            }
        ]
    else:  # en-us
        return [
            {
                "code": """
import random
import feffery_antd_components as fac

fac.AntdTable(
    columns=[
        {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    data=[
        {f'Field {j}': random.randint(1, 4) for j in range(1, 6)}
        for _ in range(10)
    ],
    bordered=True,
    sortOptions={
        'sortDataIndexes': ['Field 1', 'Field 2', 'Field 4', 'Field 5'],
        'multiple': 'auto',
    },
)
"""
            }
        ]
