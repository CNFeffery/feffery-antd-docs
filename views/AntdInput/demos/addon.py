import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                addonBefore='前缀元素示例',
                addonAfter='后缀元素示例',
            ),
            fac.AntdInput(
                addonBefore=fac.AntdSelect(
                    defaultValue='http://',
                    options=[
                        {'label': option, 'value': option}
                        for option in ['http://', 'https://']
                    ],
                    allowClear=False,
                ),
                addonAfter=fac.AntdSelect(
                    defaultValue='.com',
                    options=[
                        {'label': option, 'value': option}
                        for option in ['.com', '.cn']
                    ],
                    allowClear=False,
                ),
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            addonBefore='前缀元素示例',
            addonAfter='后缀元素示例',
        ),
        fac.AntdInput(
            addonBefore=fac.AntdSelect(
                defaultValue='http://',
                options=[
                    {'label': option, 'value': option}
                    for option in ['http://', 'https://']
                ],
                allowClear=False,
            ),
            addonAfter=fac.AntdSelect(
                defaultValue='.com',
                options=[
                    {'label': option, 'value': option}
                    for option in ['.com', '.cn']
                ],
                allowClear=False,
            ),
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
