import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'mini-progress示例',
                'dataIndex': 'mini-progress示例',
                'renderOptions': {
                    'renderType': 'mini-progress',
                    'progressStrokeLinecap': 'round',
                },
            }
        ],
        data=[{'mini-progress示例': x} for x in [0, 0.66, 1]],
        bordered=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': 'mini-progress示例',
            'dataIndex': 'mini-progress示例',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressStrokeLinecap': 'round',
            },
        }
    ],
    data=[{'mini-progress示例': x} for x in [0, 0.66, 1]],
    bordered=True,
)
"""
    }
]
