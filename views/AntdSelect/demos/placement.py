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
                        options=[f'选项{i}' for i in range(1, 6)],
                        placeholder=f'placement="{placement}"',
                        placement=placement,
                        # 必须设置popupMatchSelectWidth=False，否则导致弹出框宽度强制匹配select宽度
                        popupMatchSelectWidth=False,
                        # 使用fuc.FefferyStyle中设置好的自定义类样式
                        popupClassName='popup-custom-style',
                        style={'width': '100%'},
                    )
                    # 为了体现placement中"left"和"right"的效果，需要注入css样式来让悬浮层的宽度与select宽度不一致
                    # 如果只需要体现placement中"top"和"bottom"的效果，则无需注入css样式
                    for placement in [
                        'bottomLeft',
                        'bottomRight',
                        'topLeft',
                        'topRight',
                    ]
                ],
                direction='vertical',
                style={'width': 350},
            ),
        ]
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
                    options=[f'选项{i}' for i in range(1, 6)],
                    placeholder=f'placement="{placement}"',
                    placement=placement,
                    # 必须设置popupMatchSelectWidth=False，否则导致弹出框宽度强制匹配select宽度
                    popupMatchSelectWidth=False,
                    # 使用fuc.FefferyStyle中设置好的自定义类样式
                    popupClassName='popup-custom-style',
                    style={'width': '100%'},
                )
                # 为了体现placement中"left"和"right"的效果，需要注入css样式来让悬浮层的宽度与select宽度不一致
                # 如果只需要体现placement中"top"和"bottom"的效果，则无需注入css样式
                for placement in [
                    'bottomLeft',
                    'bottomRight',
                    'topLeft',
                    'topRight',
                ]
            ],
            direction='vertical',
            style={'width': 350},
        ),
    ]
)
"""
    }
]
