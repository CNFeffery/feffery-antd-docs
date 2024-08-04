import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdDivider(
                        f'placement="{placement}"', innerTextOrientation='left'
                    ),
                    fac.AntdTable(
                        columns=[
                            {
                                'title': f'字段{i}',
                                'dataIndex': f'字段{i}',
                                'width': '20%',
                            }
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
                'topLeft',
                'topCenter',
                'topRight',
                'bottomLeft',
                'bottomCenter',
                'bottomRight',
            ]
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdDivider(
                    f'placement="{placement}"', innerTextOrientation='left'
                ),
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}',
                            'width': '20%',
                        }
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
            'topLeft',
            'topCenter',
            'topRight',
            'bottomLeft',
            'bottomCenter',
            'bottomRight',
        ]
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
