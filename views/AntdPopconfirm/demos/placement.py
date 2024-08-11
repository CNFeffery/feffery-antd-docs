import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdPopconfirm(
                fac.AntdButton(placement),
                title='确认继续',
                description=f'placement="{placement}"',
                placement=placement,
            )
            for placement in [
                'top',
                'left',
                'right',
                'bottom',
                'topLeft',
                'topRight',
                'bottomLeft',
                'bottomRight',
                'leftTop',
                'leftBottom',
                'rightTop',
                'rightBottom',
            ]
        ],
        wrap=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdPopconfirm(
            fac.AntdButton(placement),
            title='确认继续',
            description=f'placement="{placement}"',
            placement=placement,
        )
        for placement in [
            'top',
            'left',
            'right',
            'bottom',
            'topLeft',
            'topRight',
            'bottomLeft',
            'bottomRight',
            'leftTop',
            'leftBottom',
            'rightTop',
            'rightBottom',
        ]
    ],
    wrap=True,
)
"""
    }
]
