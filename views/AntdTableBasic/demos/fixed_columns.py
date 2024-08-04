from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('冻结在左侧', innerTextOrientation='left'),
        html.Div(
            fac.AntdTable(
                columns=[
                    {
                        'title': f'字段{i}',
                        'dataIndex': f'字段{i}',
                        'fixed': 'left' if i == 1 else None,
                    }
                    for i in range(1, 6)
                ],
                data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
                maxWidth=900,
            ),
            style={'maxWidth': 700, 'margin': '0 auto'},
        ),
        fac.AntdDivider('冻结在右侧', innerTextOrientation='left'),
        html.Div(
            fac.AntdTable(
                columns=[
                    {
                        'title': f'字段{i}',
                        'dataIndex': f'字段{i}',
                        'fixed': 'right' if i == 5 else None,
                    }
                    for i in range(1, 6)
                ],
                data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
                maxWidth=900,
            ),
            style={'maxWidth': 700, 'margin': '0 auto'},
        ),
        fac.AntdDivider('双侧同时冻结', innerTextOrientation='left'),
        html.Div(
            fac.AntdTable(
                columns=[
                    {
                        'title': f'字段{i}',
                        'dataIndex': f'字段{i}',
                        'fixed': (
                            'left' if i == 1 else ('right' if i == 5 else None)
                        ),
                    }
                    for i in range(1, 6)
                ],
                data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
                maxWidth=900,
            ),
            style={'maxWidth': 700, 'margin': '0 auto'},
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('冻结在左侧', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'字段{i}',
                    'dataIndex': f'字段{i}',
                    'fixed': 'left' if i == 1 else None,
                }
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdDivider('冻结在右侧', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'字段{i}',
                    'dataIndex': f'字段{i}',
                    'fixed': 'right' if i == 5 else None,
                }
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
    fac.AntdDivider('双侧同时冻结', innerTextOrientation='left'),
    html.Div(
        fac.AntdTable(
            columns=[
                {
                    'title': f'字段{i}',
                    'dataIndex': f'字段{i}',
                    'fixed': (
                        'left' if i == 1 else ('right' if i == 5 else None)
                    ),
                }
                for i in range(1, 6)
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
            maxWidth=900,
        ),
        style={'maxWidth': 700, 'margin': '0 auto'},
    ),
]
"""
    }
]
