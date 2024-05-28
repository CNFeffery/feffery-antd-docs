import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFloatButtonGroup(
            [
                fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-question')),
                fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-setting')),
                fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-mail')),
            ],
            id='float-button-group-basic-event',
            trigger='click',
            icon=fac.AntdIcon(icon='antd-menu'),
            type='primary',
        ),
        fac.AntdText(id='float-button-group-basic-event-output'),
    ]

    return demo_contents


@app.callback(
    Output('float-button-group-basic-event-output', 'children'),
    Input('float-button-group-basic-event', 'open'),
    prevent_initial_call=True,
)
def float_button_group_basic_event(open):
    return f'open: {open}'


code_string = [
    {
        'code': """
[
    fac.AntdFloatButtonGroup(
        [
            fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-question')),
            fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-setting')),
            fac.AntdFloatButton(icon=fac.AntdIcon(icon='antd-mail')),
        ],
        id='float-button-group-basic-event',
        trigger='click',
        icon=fac.AntdIcon(icon='antd-menu'),
        type='primary',
    ),
    fac.AntdText(id='float-button-group-basic-event-output'),
]

...

@app.callback(
    Output('float-button-group-basic-event-output', 'children'),
    Input('float-button-group-basic-event', 'open'),
    prevent_initial_call=True,
)
def float_button_group_basic_event(open):
    return f'open: {open}'
"""
    }
]
