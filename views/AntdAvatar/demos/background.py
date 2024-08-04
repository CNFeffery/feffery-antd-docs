import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyHexColorPicker(id='avatar-bg-color-input'),
            fac.AntdSpace(
                [
                    fac.AntdAvatar(id='avatar-bg-color-icon-demo'),
                    fac.AntdAvatar(
                        id='avatar-bg-color-text-demo', mode='text', text='F'
                    ),
                ]
            ),
        ],
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    [
        Output('avatar-bg-color-icon-demo', 'style'),
        Output('avatar-bg-color-text-demo', 'style'),
    ],
    Input('avatar-bg-color-input', 'color'),
)
def avatar_bg_color_demo(color):
    return [{'background': color}] * 2


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fuc.FefferyHexColorPicker(id='avatar-bg-color-input'),
        fac.AntdSpace(
            [
                fac.AntdAvatar(id='avatar-bg-color-icon-demo'),
                fac.AntdAvatar(
                    id='avatar-bg-color-text-demo', mode='text', text='F'
                ),
            ]
        ),
    ],
    style={'width': '100%'},
)

...

@app.callback(
    [
        Output('avatar-bg-color-icon-demo', 'style'),
        Output('avatar-bg-color-text-demo', 'style'),
    ],
    Input('avatar-bg-color-input', 'color'),
)
def avatar_bg_color_demo(color):
    return [{'background': color}] * 2
"""
    }
]
