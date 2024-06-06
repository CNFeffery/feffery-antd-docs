import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSlider(
                vertical=True,
                min=0,
                max=100,
                defaultValue=33,
                style={'height': 200},
            ),
            fac.AntdSlider(
                vertical=True,
                range=True,
                min=0,
                max=100,
                defaultValue=[10, 90],
                style={'height': 200},
            ),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSlider(
            vertical=True,
            min=0,
            max=100,
            defaultValue=33,
            style={'height': 200},
        ),
        fac.AntdSlider(
            vertical=True,
            range=True,
            min=0,
            max=100,
            defaultValue=[10, 90],
            style={'height': 200},
        ),
    ]
)
"""
    }
]
