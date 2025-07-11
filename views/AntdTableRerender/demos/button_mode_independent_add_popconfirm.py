import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'dataIndex': '按钮示例',
                'title': '按钮示例',
                'renderOptions': {'renderType': 'button'},
            },
        ],
        data=[
            {
                '按钮示例': [
                    {
                        'content': '带气泡确认',
                        'popConfirmProps': {
                            'title': '气泡确认标题',
                            'okText': '确认',
                            'cancelText': '取消',
                        },
                    },
                    {
                        'content': '不带气泡确认',
                    },
                ]
            }
        ],
        bordered=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'dataIndex': '按钮示例',
            'title': '按钮示例',
            'renderOptions': {'renderType': 'button'},
        },
    ],
    data=[
        {
            '按钮示例': [
                {
                    'content': '带气泡确认',
                    'popConfirmProps': {
                        'title': '气泡确认标题',
                        'okText': '确认',
                        'cancelText': '取消',
                    },
                },
                {
                    'content': '不带气泡确认',
                },
            ]
        }
    ],
    bordered=True,
)
"""
    }
]
