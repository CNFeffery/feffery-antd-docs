import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                [fac.AntdText("'outline'", code=True), '风格'],
                innerTextOrientation='left',
            ),
            fac.AntdRadioGroup(
                options=[
                    {'label': f'选项{c}', 'value': c} for c in list('abcdef')
                ],
                defaultValue='a',
                optionType='button',
            ),
            fac.AntdDivider(
                [fac.AntdText("'solid'", code=True), '风格'],
                innerTextOrientation='left',
            ),
            fac.AntdRadioGroup(
                options=[
                    {'label': f'选项{c}', 'value': c} for c in list('abcdef')
                ],
                defaultValue='a',
                optionType='button',
                buttonStyle='solid',
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
            [fac.AntdText("'outline'", code=True), '风格'],
            innerTextOrientation='left',
        ),
        fac.AntdRadioGroup(
            options=[
                {'label': f'选项{c}', 'value': c} for c in list('abcdef')
            ],
            defaultValue='a',
            optionType='button',
        ),
        fac.AntdDivider(
            [fac.AntdText("'solid'", code=True), '风格'],
            innerTextOrientation='left',
        ),
        fac.AntdRadioGroup(
            options=[
                {'label': f'选项{c}', 'value': c} for c in list('abcdef')
            ],
            defaultValue='a',
            optionType='button',
            buttonStyle='solid',
        ),
    ],
    direction='vertical',
)
"""
    }
]
