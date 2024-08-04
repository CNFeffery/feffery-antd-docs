import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        size='small',
        columns=[
            {
                'title': '角标模式',
                'dataIndex': '角标模式',
                'renderOptions': {'renderType': 'corner-mark'},
            }
        ],
        data=[
            {
                'key': i,
                '角标模式': {
                    'content': '角标模式',
                    'color': ['red', 'blue', 'green'][i],
                    'offsetX': -7.5,
                    'offsetY': -8.5,
                    'placement': 'top-left',
                    'hide': [False, True, False][i],
                },
            }
            for i in range(3)
        ],
        bordered=True,
        style={'width': '200px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    size='small',
    columns=[
        {
            'title': '角标模式',
            'dataIndex': '角标模式',
            'renderOptions': {'renderType': 'corner-mark'},
        }
    ],
    data=[
        {
            'key': i,
            '角标模式': {
                'content': '角标模式',
                'color': ['red', 'blue', 'green'][i],
                'offsetX': -7.5,
                'offsetY': -8.5,
                'placement': 'top-left',
                'hide': [False, True, False][i],
            },
        }
        for i in range(3)
    ],
    bordered=True,
    style={'width': '200px'},
)
"""
    }
]
