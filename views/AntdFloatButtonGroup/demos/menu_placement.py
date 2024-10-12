import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSegmented(
            id='float-button-group-placement',
            options=[
                {'label': placement, 'value': placement}
                for placement in ['top', 'right', 'bottom', 'left']
            ],
            value='top',
            block=True,
        ),
        fac.AntdFloatButtonGroup(
            [
                fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-question')),
                fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-setting')),
            ],
            id='float-button-group-placement-demo',
            trigger='click',
            style={'right': 'calc(50vw - 20px)', 'bottom': 'calc(50vh - 20px)'},
            icon=fac.AntdIcon(icon='antd-menu'),
            type='primary',
        ),
    ]

    return demo_contents


@app.callback(
    Output('float-button-group-placement-demo', 'placement'),
    Input('float-button-group-placement', 'value'),
)
def float_button_group_placement_demo(value):
    return value


code_string = [
    {
        'code': """
[
    fac.AntdSegmented(
        id='float-button-group-placement',
        options=[
            {'label': placement, 'value': placement}
            for placement in ['top', 'right', 'bottom', 'left']
        ],
        value='top',
        block=True,
    ),
    fac.AntdFloatButtonGroup(
        [
            fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-question')),
            fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-setting')),
        ],
        id='float-button-group-placement-demo',
        trigger='click',
        style={'right': 'calc(50vw - 20px)', 'bottom': 'calc(50vh - 20px)'},
        icon=fac.AntdIcon(icon='antd-menu'),
        type='primary',
    ),
]

...

@app.callback(
    Output('float-button-group-placement-demo', 'placement'),
    Input('float-button-group-placement', 'value'),
)
def float_button_group_placement_demo(value):
    return value
"""
    }
]
