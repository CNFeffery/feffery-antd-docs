import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdButton('常规点击监听', id='button-basic-event'),
                    fac.AntdText(id='button-basic-event-output'),
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdButton(
                        '防抖点击监听',
                        id='button-debounce-event',
                        debounceWait=300,
                    ),
                    fac.AntdText(id='button-debounce-event-output'),
                ]
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


@app.callback(
    Output('button-basic-event-output', 'children'),
    Input('button-basic-event', 'nClicks'),
    prevent_initial_call=True,
)
def button_basic_event(nClicks):
    return f'nClicks: {nClicks}'


@app.callback(
    Output('button-debounce-event-output', 'children'),
    Input('button-debounce-event', 'nClicks'),
    prevent_initial_call=True,
)
def button_debounce_event(nClicks):
    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdButton('常规点击监听', id='button-basic-event'),
                fac.AntdText(id='button-basic-event-output'),
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '防抖点击监听', id='button-debounce-event', debounceWait=300
                ),
                fac.AntdText(id='button-debounce-event-output'),
            ]
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)

...

@app.callback(
    Output('button-basic-event-output', 'children'),
    Input('button-basic-event', 'nClicks'),
    prevent_initial_call=True,
)
def button_basic_event(nClicks):
    return f'nClicks: {nClicks}'


@app.callback(
    Output('button-debounce-event-output', 'children'),
    Input('button-debounce-event', 'nClicks'),
    prevent_initial_call=True,
)
def button_debounce_event(nClicks):
    return f'nClicks: {nClicks}'
"""
    }
]
