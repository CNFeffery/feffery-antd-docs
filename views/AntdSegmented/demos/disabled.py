import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdSegmented(
                options=[
                    {'label': i, 'value': i}
                    for i in ['Map', 'Transit', 'Satellite']
                ],
                defaultValue='Map',
                disabled=True,
            ),
            fac.AntdSegmented(
                options=[
                    {
                        'label': i,
                        'value': i,
                        'disabled': True
                        if i in ['Weekly', 'Quarterly']
                        else False,
                    }
                    for i in [
                        'Daily',
                        'Weekly',
                        'Monthly',
                        'Quarterly',
                        'Yearly',
                    ]
                ],
                defaultValue='Daily',
            ),
        ],
        gap='small',
        align='flex-start',
        vertical=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdSegmented(
            options=[
                {'label': i, 'value': i}
                for i in ['Map', 'Transit', 'Satellite']
            ],
            defaultValue='Map',
            disabled=True,
        ),
        fac.AntdSegmented(
            options=[
                {
                    'label': i,
                    'value': i,
                    'disabled': True
                    if i in ['Weekly', 'Quarterly']
                    else False,
                }
                for i in [
                    'Daily',
                    'Weekly',
                    'Monthly',
                    'Quarterly',
                    'Yearly',
                ]
            ],
            defaultValue='Daily',
        ),
    ],
    gap='small',
    align='flex-start',
    vertical=True,
)
"""
    }
]
