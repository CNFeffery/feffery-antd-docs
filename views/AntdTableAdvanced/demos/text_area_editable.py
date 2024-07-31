import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': '文本域编辑示例',
                'dataIndex': '文本域编辑示例',
                'editable': True,
                'editOptions': {
                    'mode': 'text-area',  # 开启文本域编辑模式
                    'autoSize': {'minRows': 1, 'maxRows': 3},
                },
            }
        ],
        data=[{'文本域编辑示例': '内容示例'}] * 3,
        bordered=True,
        style={'width': 200},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': '文本域编辑示例',
            'dataIndex': '文本域编辑示例',
            'editable': True,
            'editOptions': {
                'mode': 'text-area',  # 开启文本域编辑模式
                'autoSize': {'minRows': 1, 'maxRows': 3},
            },
        }
    ],
    data=[{'文本域编辑示例': '内容示例'}] * 3,
    bordered=True,
    style={'width': 200},
)
"""
    }
]
