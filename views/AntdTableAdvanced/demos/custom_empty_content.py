import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        emptyContent=fac.AntdEmpty(
            image='/assets/imgs/components/AntdEmpty/自定义占位图.png',
            description=fac.AntdText('没有数据哦~', type='secondary'),
            imageStyle={'height': 150},
        ),
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
        for i in range(1, 6)
    ],
    emptyContent=fac.AntdEmpty(
        image='/assets/imgs/AntdEmpty/自定义占位图.png',
        description=fac.AntdText('没有数据哦~', type='secondary'),
        imageStyle={'height': 150},
    ),
)
"""
    }
]
