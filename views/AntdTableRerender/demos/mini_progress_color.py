import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'mini-progress示例1',
                'dataIndex': 'mini-progress示例1',
                'renderOptions': {
                    'renderType': 'mini-progress',
                    'progressColor': '#f08c00',
                },
            },
            {
                'title': 'mini-progress示例2',
                'dataIndex': 'mini-progress示例2',
                'renderOptions': {
                    'renderType': 'mini-progress',
                    'progressColor': {
                        'from': '#4c83ff',
                        'to': '#2afadf',
                    },
                },
            },
        ],
        data=[
            {'mini-progress示例1': x, 'mini-progress示例2': x}
            for x in [0, 0.66, 1]
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
            'title': 'mini-progress示例1',
            'dataIndex': 'mini-progress示例1',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressColor': '#f08c00',
            },
        },
        {
            'title': 'mini-progress示例2',
            'dataIndex': 'mini-progress示例2',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressColor': {
                    'from': '#4c83ff',
                    'to': '#2afadf',
                },
            },
        },
    ],
    data=[
        {'mini-progress示例1': x, 'mini-progress示例2': x}
        for x in [0, 0.66, 1]
    ],
    bordered=True,
    tableLayout='fixed',
)
"""
    }
]
