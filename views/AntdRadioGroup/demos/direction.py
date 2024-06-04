import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('水平排列', innerTextOrientation='left'),
            fac.AntdRadioGroup(
                options=[
                    {'label': f'选项{c}', 'value': c} for c in list('abcdef')
                ],
                defaultValue='a',
            ),
            fac.AntdDivider('竖直排列', innerTextOrientation='left'),
            fac.AntdRadioGroup(
                options=[
                    {'label': f'选项{c}', 'value': c} for c in list('abcdef')
                ],
                defaultValue='a',
                direction='vertical',
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
        fac.AntdDivider('水平排列', innerTextOrientation='left'),
        fac.AntdRadioGroup(
            options=[
                {'label': f'选项{c}', 'value': c} for c in list('abcdef')
            ],
            defaultValue='a',
        ),
        fac.AntdDivider('竖直排列', innerTextOrientation='left'),
        fac.AntdRadioGroup(
            options=[
                {'label': f'选项{c}', 'value': c} for c in list('abcdef')
            ],
            defaultValue='a',
            direction='vertical',
        ),
    ],
    direction='vertical',
)
"""
    }
]
