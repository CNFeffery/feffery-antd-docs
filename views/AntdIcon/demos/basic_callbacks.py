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
                    fac.AntdText('常规点击事件：'),
                    fac.AntdIcon(
                        id='icon-basic-event',
                        icon='antd-thunderbolt',
                        style={'cursor': 'pointer'},
                    ),
                    fac.AntdText(id='icon-basic-event-output'),
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdText('防抖点击事件：'),
                    fac.AntdIcon(
                        id='icon-debounce-event',
                        icon='antd-thunderbolt',
                        debounceWait=300,
                        style={'cursor': 'pointer'},
                    ),
                    fac.AntdText(id='icon-debounce-event-output'),
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
    Output('icon-basic-event-output', 'children'),
    Input('icon-basic-event', 'nClicks'),
    prevent_initial_call=True,
)
def icon_basic_event(nClicks):
    return f'nClicks: {nClicks}'


@app.callback(
    Output('icon-debounce-event-output', 'children'),
    Input('icon-debounce-event', 'nClicks'),
    prevent_initial_call=True,
)
def icon_debounce_event(nClicks):
    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdText('常规点击事件：'),
                fac.AntdIcon(
                    id='icon-basic-event',
                    icon='antd-thunderbolt',
                    style={'cursor': 'pointer'},
                ),
                fac.AntdText(id='icon-basic-event-output'),
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdText('防抖点击事件：'),
                fac.AntdIcon(
                    id='icon-debounce-event',
                    icon='antd-thunderbolt',
                    debounceWait=300,
                    style={'cursor': 'pointer'},
                ),
                fac.AntdText(id='icon-debounce-event-output'),
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
    Output('icon-basic-event-output', 'children'),
    Input('icon-basic-event', 'nClicks'),
    prevent_initial_call=True,
)
def icon_basic_event(nClicks):
    return f'nClicks: {nClicks}'


@app.callback(
    Output('icon-debounce-event-output', 'children'),
    Input('icon-debounce-event', 'nClicks'),
    prevent_initial_call=True,
)
def icon_debounce_event(nClicks):
    return f'nClicks: {nClicks}'
"""
    }
]
