import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                fac.AntdText('tooltipVisible=True', code=True),
                innerTextOrientation='left',
            ),
            fac.AntdSlider(
                min=0,
                max=100,
                defaultValue=50,
                tooltipVisible=True,
                style={'width': 300},
            ),
            fac.AntdDivider(
                fac.AntdText('tooltipVisible=False', code=True),
                innerTextOrientation='left',
            ),
            fac.AntdSlider(
                min=0,
                max=100,
                defaultValue=50,
                tooltipVisible=False,
                style={'width': 300},
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
        fac.AntdDivider(
            fac.AntdText('tooltipVisible=True', code=True),
            innerTextOrientation='left',
        ),
        fac.AntdSlider(
            min=0,
            max=100,
            defaultValue=50,
            tooltipVisible=True,
            style={'width': 300},
        ),
        fac.AntdDivider(
            fac.AntdText('tooltipVisible=False', code=True),
            innerTextOrientation='left',
        ),
        fac.AntdSlider(
            min=0,
            max=100,
            defaultValue=50,
            tooltipVisible=False,
            style={'width': 300},
        ),
    ],
    direction='vertical',
)
"""
    }
]
