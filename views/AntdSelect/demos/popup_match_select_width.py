import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash import html
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            # 使用fuc.FefferyStyle注入原始css类样式，覆盖原本的min-width样式
            fuc.FefferyStyle(
                rawStyle='.popup-custom-style {min-width: 100px!important;}'
            ),
            fac.AntdSpace(
                [
                    fac.AntdSelect(
                        options=[f'选项{i}' for i in range(1, 26)],
                        placeholder='popupMatchSelectWidth=True',
                        popupMatchSelectWidth=True,
                        # 使用fuc.FefferyStyle中设置好的自定义类样式，来使用自定义的宽度
                        popupClassName='popup-custom-style',
                        style={'width': '100%'},
                    ),
                    fac.AntdSelect(
                        options=[f'选项{i}' for i in range(1, 26)],
                        placeholder='popupMatchSelectWidth=False',
                        popupMatchSelectWidth=False,
                        # 使用fuc.FefferyStyle中设置好的自定义类样式，来使用自定义的宽度
                        popupClassName='popup-custom-style',
                        style={'width': '100%'},
                    ),
                ],
                direction='vertical',
                style={'width': 350, 'marginBottom': 5},
            ),
            fac.AntdParagraph(
                [
                    '可以看到，即使设置了自定义的下拉选择菜单宽度，在',
                    fac.AntdText('popupMatchSelectWidth=True', code=True),
                    '时，弹出框的宽度仍与选择框的宽度一致，只有在',
                    fac.AntdText('popupMatchSelectWidth=False', code=True),
                    '时，下拉选择菜单的自定义宽度才能生效。同时不再使用虚拟滚动。',
                ]
            ),
        ],
    )

    return demo_contents


code_string = [
    {
        'code': """
html.Div(
    [
        # 使用fuc.FefferyStyle注入原始css类样式，覆盖原本的min-width样式
        fuc.FefferyStyle(
            rawStyle='.popup-custom-style {min-width: 100px!important;}'
        ),
        fac.AntdSpace(
            [
                fac.AntdSelect(
                    options=[f'选项{i}' for i in range(1, 26)],
                    placeholder='popupMatchSelectWidth=True',
                    popupMatchSelectWidth=True,
                    # 使用fuc.FefferyStyle中设置好的自定义类样式，来使用自定义的宽度
                    popupClassName='popup-custom-style',
                    style={'width': '100%'},
                ),
                fac.AntdSelect(
                    options=[f'选项{i}' for i in range(1, 26)],
                    placeholder='popupMatchSelectWidth=False',
                    popupMatchSelectWidth=False,
                    # 使用fuc.FefferyStyle中设置好的自定义类样式，来使用自定义的宽度
                    popupClassName='popup-custom-style',
                    style={'width': '100%'},
                ),
            ],
            direction='vertical',
            style={'width': 350, 'marginBottom': 5},
        ),
        fac.AntdParagraph(
            [
                '可以看到，即使设置了自定义的下拉选择菜单宽度，在',
                fac.AntdText('popupMatchSelectWidth=True', code=True),
                '时，弹出框的宽度仍与选择框的宽度一致，只有在',
                fac.AntdText('popupMatchSelectWidth=False', code=True),
                '时，下拉选择菜单的自定义宽度才能生效。同时不再使用虚拟滚动。',
            ]
        ),
    ],
)
"""
    }
]
