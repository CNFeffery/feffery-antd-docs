import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        fac.AntdText('Regular click event:'),
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
                        fac.AntdText('Debounced click event:'),
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdText('Regular click event:'),
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
                fac.AntdText('Debounced click event:'),
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
