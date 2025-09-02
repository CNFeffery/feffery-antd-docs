import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        title = lambda i: f'字段{i}'
        data_key = lambda i: f'字段{i}'
        cell_value = '示例内容'
        divider_label = lambda placement: f'位置="{placement}"'
    else:  # en-us fallback
        title = lambda i: f'Field {i}'
        data_key = lambda i: f'Field {i}'
        cell_value = 'Sample Content'
        divider_label = lambda placement: f'placement="{placement}"'

    placements = [
        'topLeft',
        'topCenter',
        'topRight',
        'bottomLeft',
        'bottomCenter',
        'bottomRight',
    ]

    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdDivider(
                        divider_label(placement), innerTextOrientation='left'
                    ),
                    fac.AntdTable(
                        columns=[
                            {
                                'title': title(i),
                                'dataIndex': data_key(i),
                                'width': '20%',
                            }
                            for i in range(1, 6)
                        ],
                        data=[{data_key(i): cell_value for i in range(1, 6)}],
                        pagination={'position': placement},
                    ),
                ],
                direction='vertical',
                style={'width': '100%'},
            )
            for placement in placements
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdDivider(f'位置="{placement}"', innerTextOrientation='left'),
                fac.AntdTable(
                    columns=[
                        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
                        for i in range(1, 6)
                    ],
                    data=[{f'字段{i}': '示例内容' for i in range(1, 6)}],
                    pagination={'position': placement},
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )
        for placement in [
            'topLeft', 'topCenter', 'topRight',
            'bottomLeft', 'bottomCenter', 'bottomRight'
        ]
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
    else:  # en-us
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdDivider(f'placement="{placement}"', innerTextOrientation='left'),
                fac.AntdTable(
                    columns=[
                        {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
                        for i in range(1, 6)
                    ],
                    data=[{f'Field {i}': 'Sample Content' for i in range(1, 6)}],
                    pagination={'position': placement},
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )
        for placement in [
            'topLeft', 'topCenter', 'topRight',
            'bottomLeft', 'bottomCenter', 'bottomRight'
        ]
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
