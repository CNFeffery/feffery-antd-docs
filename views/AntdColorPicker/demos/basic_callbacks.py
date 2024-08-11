import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdColorPicker(id='color-picker-demo'),
            fac.AntdText(id='color-picker-demo-output'),
        ]
    )

    return demo_contents


@app.callback(
    Output('color-picker-demo-output', 'children'),
    Input('color-picker-demo', 'value'),
    prevent_initial_call=True,
)
def color_picker_event(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdColorPicker(id='color-picker-demo'),
        fac.AntdText(id='color-picker-demo-output'),
    ]
)

...

@app.callback(
    Output('color-picker-demo-output', 'children'),
    Input('color-picker-demo', 'value'),
    prevent_initial_call=True,
)
def color_picker_event(value):
    return f'value: {value}'
"""
    }
]
