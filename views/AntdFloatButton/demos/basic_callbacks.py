import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdFloatButton(
                id='float-button-basic-event',
                description='点我',
                type='primary',
            ),
            fac.AntdText(id='float-button-basic-event-output'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdFloatButton(
                id='float-button-basic-event',
                description='Click',
                type='primary',
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdFloatButton(
        id='float-button-basic-event', description='Click', type='primary'
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
