import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': '交互式图片',
                'dataIndex': '交互式图片',
                'renderOptions': {'renderType': 'image'},
            },
            {
                'title': '静态图片',
                'dataIndex': '静态图片',
                'renderOptions': {'renderType': 'image'},
            },
        ],
        data=[
            {
                '交互式图片': {
                    'src': '/assets/imgs/fac-logo.svg',
                    'height': '75px',
                },
                '静态图片': {
                    'src': '/assets/imgs/fac-logo.svg',
                    'height': '75px',
                    'preview': False,
                },
            }
            for i in range(5)
        ],
        bordered=True,
        style={'width': '300px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': '交互式图片',
            'dataIndex': '交互式图片',
            'renderOptions': {'renderType': 'image'},
        },
        {
            'title': '静态图片',
            'dataIndex': '静态图片',
            'renderOptions': {'renderType': 'image'},
        },
    ],
    data=[
        {
            '交互式图片': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px',
            },
            '静态图片': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px',
                'preview': False,
            },
        }
        for i in range(5)
    ],
    bordered=True,
    style={'width': '300px'},
)
"""
    }
]
