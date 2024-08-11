import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCard('size="default"', title='卡片示例'),
            fac.AntdCard('size="small"', title='卡片示例', size='small'),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """

fac.AntdSpace(
    [
        fac.AntdCard(
            'size="default"',
            title='卡片示例'
        ),

        fac.AntdCard(
            'size="small"',
            title='卡片示例',
            size='small'
        )
    ],
    direction='vertical'
)
"""
    }
]
