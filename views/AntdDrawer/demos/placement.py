import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdRadioGroup(
                    id='drawer-placement-demo-placement',
                    options=[
                        {'label': placement, 'value': placement}
                        for placement in ['left', 'top', 'right', 'bottom']
                    ],
                    defaultValue='right',
                ),
                fac.AntdButton(
                    '打开示例抽屉',
                    id='drawer-placement-demo-open',
                    type='primary',
                ),
            ],
            direction='vertical',
        ),
        fac.AntdDrawer('示例内容', id='drawer-placement-demo'),
    ]

    return demo_contents


@app.callback(
    [
        Output('drawer-placement-demo', 'title'),
        Output('drawer-placement-demo', 'placement'),
    ],
    Input('drawer-placement-demo-placement', 'value'),
)
def update_drawer_placement_and_title_dmeo(value):
    return [f'placement="{value}"', value]


@app.callback(
    Output('drawer-placement-demo', 'visible'),
    Input('drawer-placement-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def draw_placement_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdSpace(
        [
            fac.AntdRadioGroup(
                id='drawer-placement-demo-placement',
                options=[
                    {'label': placement, 'value': placement}
                    for placement in ['left', 'top', 'right', 'bottom']
                ],
                defaultValue='right',
            ),
            fac.AntdButton(
                '打开示例抽屉',
                id='drawer-placement-demo-open',
                type='primary',
            ),
        ],
        direction='vertical',
    ),
    fac.AntdDrawer('示例内容', id='drawer-placement-demo'),
]

...

@app.callback(
    [
        Output('drawer-placement-demo', 'title'),
        Output('drawer-placement-demo', 'placement'),
    ],
    Input('drawer-placement-demo-placement', 'value'),
)
def update_drawer_placement_and_title_dmeo(value):
    return [f'placement="{value}"', value]


@app.callback(
    Output('drawer-placement-demo', 'visible'),
    Input('drawer-placement-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def draw_placement_demo(nClicks):
    return True
"""
    }
]
