import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdRadioGroup(
                options=[
                    {'label': f'选项{c}', 'value': c} for c in list('abcdef')
                ],
                defaultValue='c',
                readOnly=True,
            ),
            fac.AntdRadioGroup(
                options=[
                    {'label': f'选项{c}', 'value': c} for c in list('abcdef')
                ],
                defaultValue='c',
                optionType='button',
                readOnly=True,
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
        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='c',
            readOnly=True
        ),

        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{c}',
                    'value': c
                }
                for c in list('abcdef')
            ],
            defaultValue='c',
            optionType='button',
            readOnly=True
        )
    ],
    direction='vertical'
)
"""
    }
]
