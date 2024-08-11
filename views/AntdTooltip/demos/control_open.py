import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSwitch(id='tooltip-open-switch', checked=False),
            fac.AntdTooltip(
                fac.AntdButton('锚点示例'),
                id='tooltip-open-demo',
                title='信息提示示例',
            ),
        ]
    )

    return demo_contents


@app.callback(
    Output('tooltip-open-demo', 'open'),
    Input('tooltip-open-switch', 'checked'),
    prevent_initial_call=True,
)
def control_tooltip_open(checked):
    return checked


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSwitch(id='tooltip-open-switch', checked=False),
        fac.AntdTooltip(
            fac.AntdButton('锚点示例'),
            id='tooltip-open-demo',
            title='信息提示示例',
        ),
    ]
)

...

@app.callback(
    Output('tooltip-open-demo', 'open'),
    Input('tooltip-open-switch', 'checked'),
    prevent_initial_call=True,
)
def control_tooltip_open(checked):
    return checked
"""
    }
]
