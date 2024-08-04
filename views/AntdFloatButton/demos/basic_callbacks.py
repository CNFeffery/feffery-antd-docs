import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdFloatButton(
            id='float-button-basic-event', description='点我', type='primary'
        ),
        fac.AntdText(id='float-button-basic-event-output'),
    ]

    return demo_contents


@app.callback(
    Output('float-button-basic-event-output', 'children'),
    Input('float-button-basic-event', 'nClicks'),
    prevent_initial_call=True,
)
def float_button_basic_event(nClicks):
    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
[
    fac.AntdFloatButton(
        id='float-button-basic-event', description='点我', type='primary'
    ),
    fac.AntdText(id='float-button-basic-event-output'),
]

...

@app.callback(
    Output('float-button-basic-event-output', 'children'),
    Input('float-button-basic-event', 'nClicks'),
    prevent_initial_call=True,
)
def float_button_basic_event(nClicks):
    return f'nClicks: {nClicks}'
"""
    }
]
