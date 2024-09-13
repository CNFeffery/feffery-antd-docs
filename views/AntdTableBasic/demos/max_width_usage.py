from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
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

    return demo_contents


code_string = [
    {
        'code': """
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
