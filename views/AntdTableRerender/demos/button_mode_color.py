import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'dataIndex': 'variant参数值',
                'title': 'variant参数值',
            },
            {
                'dataIndex': '渲染效果',
                'title': '渲染效果',
                'renderOptions': {'renderType': 'button'},
            },
        ],
        data=[
            {
                'variant参数值': variant,
                '渲染效果': [
                    {'content': color, 'color': color, 'variant': variant}
                    for color in [
                        'default',
                        'primary',
                        'danger',
                        'blue',
                        'purple',
                        'cyan',
                        'green',
                        'magenta',
                        'pink',
                        'red',
                        'orange',
                        'yellow',
                        'volcano',
                        'geekblue',
                        'lime',
                        'gold',
                    ]
                ],
            }
            for variant in [
                'outlined',
                'dashed',
                'solid',
                'filled',
                'text',
                'link',
            ]
        ],
        bordered=True,
        tableLayout='fixed',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'dataIndex': 'variant参数值',
            'title': 'variant参数值',
        },
        {
            'dataIndex': '渲染效果',
            'title': '渲染效果',
            'renderOptions': {'renderType': 'button'},
        },
    ],
    data=[
        {
            'variant参数值': variant,
            '渲染效果': [
                {'content': color, 'color': color, 'variant': variant}
                for color in [
                    'default',
                    'primary',
                    'danger',
                    'blue',
                    'purple',
                    'cyan',
                    'green',
                    'magenta',
                    'pink',
                    'red',
                    'orange',
                    'yellow',
                    'volcano',
                    'geekblue',
                    'lime',
                    'gold',
                ]
            ],
        }
        for variant in [
            'outlined',
            'dashed',
            'solid',
            'filled',
            'text',
            'link',
        ]
    ],
    bordered=True,
    tableLayout='fixed',
)
"""
    }
]
