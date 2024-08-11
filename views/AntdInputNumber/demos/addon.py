import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInputNumber(
                addonBefore='前缀元素',
                addonAfter='后缀元素',
                style={'width': 300},
            ),
            fac.AntdInputNumber(
                addonBefore=fac.AntdSelect(
                    defaultValue='a',
                    options=[
                        {'label': option, 'value': option}
                        for option in ['a', 'b']
                    ],
                    allowClear=False,
                ),
                addonAfter=fac.AntdSelect(
                    defaultValue='m',
                    options=[
                        {'label': option, 'value': option}
                        for option in ['mm', 'cm', 'dm', 'm']
                    ],
                    allowClear=False,
                ),
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
        fac.AntdInputNumber(
            addonBefore='前缀元素',
            addonAfter='后缀元素',
            style={'width': 300},
        ),
        fac.AntdInputNumber(
            addonBefore=fac.AntdSelect(
                defaultValue='a',
                options=[
                    {'label': option, 'value': option}
                    for option in ['a', 'b']
                ],
                allowClear=False,
            ),
            addonAfter=fac.AntdSelect(
                defaultValue='m',
                options=[
                    {'label': option, 'value': option}
                    for option in ['mm', 'cm', 'dm', 'm']
                ],
                allowClear=False,
            ),
            style={'width': 300},
        ),
    ],
    direction='vertical',
)
"""
    }
]
