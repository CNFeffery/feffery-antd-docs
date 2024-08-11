import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSwitch(id='popover-open-switch', checked=False),
            fac.AntdPopover(
                fac.AntdButton('锚点示例'),
                id='popover-open-demo',
                title='气泡卡片示例',
                content='内容示例',
            ),
        ]
    )

    return demo_contents


@app.callback(
    Output('popover-open-demo', 'open'),
    Input('popover-open-switch', 'checked'),
    prevent_initial_call=True,
)
def control_popover_open(checked):
    return checked


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSwitch(id='popover-open-switch', checked=False),
        fac.AntdPopover(
            fac.AntdButton('锚点示例'),
            id='popover-open-demo',
            title='气泡卡片示例',
            content='内容示例',
        ),
    ]
)

...

@app.callback(
    Output('popover-open-demo', 'open'),
    Input('popover-open-switch', 'checked'),
    prevent_initial_call=True,
)
def control_popover_open(checked):
    return checked
"""
    }
]
