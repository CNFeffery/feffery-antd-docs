import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTooltip(
                fac.AntdButton(placement),
                title='信息提示示例',
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
        fac.AntdTooltip(
            fac.AntdButton(placement),
            title='信息提示示例',
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
        ]
    ],
    wrap=True,
)
"""
    }
]
