import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSlider(
                min=0,
                max=100,
                defaultValue=33,
                style={'width': 300},
                railStyle={'background': '#37d67a'},
            ),
            fac.AntdSlider(
                range=True,
                min=0,
                max=100,
                defaultValue=[10, 90],
                style={'width': 300},
                railStyle={'background': '#37d67a'},
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
        fac.AntdSlider(
            min=0,
            max=100,
            defaultValue=33,
            style={'width': 300},
            railStyle={'background': '#37d67a'},
        ),
        fac.AntdSlider(
            range=True,
            min=0,
            max=100,
            defaultValue=[10, 90],
            style={'width': 300},
            railStyle={'background': '#37d67a'},
        ),
    ],
    direction='vertical',
)
"""
    }
]
