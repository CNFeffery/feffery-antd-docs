import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}'} for i in range(1, 4)
        ],
        data=[
            {f'字段{i}': '示例内容' for i in range(1, 4)} for row in range(30)
        ],
        sticky=True,
        size='large',
        pagination={'pageSize': 999},
        title='请点击本示例下方的“在新窗口打开”按钮，以查看无页首遮挡干扰的完整效果。',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}'} for i in range(1, 4)
    ],
    data=[
        {f'字段{i}': '示例内容' for i in range(1, 4)} for row in range(30)
    ],
    sticky=True,
    size='large',
    pagination={'pageSize': 999},
    title='请点击本示例下方的“在新窗口打开”按钮，以查看无页首遮挡干扰的完整效果。',
)
"""
    }
]
