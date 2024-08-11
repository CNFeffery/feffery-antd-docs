import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fuc.FefferyHexColorPicker(
                id='tooltip-color-demo-input', showAlpha=True, color='#f6f7f866'
            ),
            fac.AntdTooltip(
                fac.AntdButton('锚点示例'),
                id='tooltip-color-demo',
                title='信息提示示例',
            ),
        ]
    )

    return demo_contents


@app.callback(
    [
        Output('tooltip-color-demo', 'color'),
        Output('tooltip-color-demo', 'title'),
    ],
    Input('tooltip-color-demo-input', 'color'),
)
def tooltip_color_demo(color):
    return [
        color,
        fac.AntdParagraph(['当前color: ', fac.AntdText(color, copyable=True)]),
    ]


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fuc.FefferyHexColorPicker(
            id='tooltip-color-demo-input', showAlpha=True, color='#f6f7f866'
        ),
        fac.AntdTooltip(
            fac.AntdButton('锚点示例'),
            id='tooltip-color-demo',
            title='信息提示示例',
        ),
    ]
)

...

@app.callback(
    [
        Output('tooltip-color-demo', 'color'),
        Output('tooltip-color-demo', 'title'),
    ],
    Input('tooltip-color-demo-input', 'color'),
)
def tooltip_color_demo(color):
    return [
        color,
        fac.AntdParagraph(['当前color: ', fac.AntdText(color, copyable=True)]),
    ]
"""
    }
]
