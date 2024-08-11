import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInputNumber(
                step=0.1, defaultValue=0, placeholder='step=0.1'
            ),
            fac.AntdInputNumber(
                step=0.001, defaultValue=0, placeholder='step=0.001'
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInputNumber(
            step=0.1, defaultValue=0, placeholder='step=0.1'
        ),
        fac.AntdInputNumber(
            step=0.001, defaultValue=0, placeholder='step=0.001'
        ),
    ],
    direction='vertical',
)
"""
    }
]
