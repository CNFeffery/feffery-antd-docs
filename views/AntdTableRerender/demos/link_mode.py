import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'link示例1',
                'dataIndex': 'link示例1',
                'renderOptions': {'renderType': 'link'},
                'width': '50%',
            },
            {
                'title': 'link示例2',
                'dataIndex': 'link示例2',
                'renderOptions': {
                    'renderType': 'link',
                    'renderLinkText': '示例链接',
                },
                'width': '50%',
            },
        ],
        data=[
            {
                'link示例1': {'content': f'{content}仓库', 'href': href},
                'link示例2': {'href': '/AntdTable-rerender'},
            }
            for href, content in zip(
                [
                    'https://github.com/CNFeffery/feffery-antd-components',
                    'https://github.com/CNFeffery/feffery-utils-components',
                    'https://github.com/CNFeffery/feffery-antd-charts',
                    'https://github.com/CNFeffery/feffery-markdown-components',
                    'https://github.com/CNFeffery/feffery-leaflet-components',
                ],
                ['fac', 'fuc', 'fact', 'fmc', 'flc'],
            )
        ],
        bordered=True,
        style={'width': 400},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': 'link示例1',
            'dataIndex': 'link示例1',
            'renderOptions': {'renderType': 'link'},
            'width': '50%',
        },
        {
            'title': 'link示例2',
            'dataIndex': 'link示例2',
            'renderOptions': {
                'renderType': 'link',
                'renderLinkText': '示例链接',
            },
            'width': '50%',
        },
    ],
    data=[
        {
            'link示例1': {'content': f'{content}仓库', 'href': href},
            'link示例2': {'href': '/AntdTable-rerender'},
        }
        for href, content in zip(
            [
                'https://github.com/CNFeffery/feffery-antd-components',
                'https://github.com/CNFeffery/feffery-utils-components',
                'https://github.com/CNFeffery/feffery-antd-charts',
                'https://github.com/CNFeffery/feffery-markdown-components',
                'https://github.com/CNFeffery/feffery-leaflet-components',
            ],
            ['fac', 'fuc', 'fact', 'fmc', 'flc'],
        )
    ],
    bordered=True,
    style={'width': 400},
)
"""
    }
]
