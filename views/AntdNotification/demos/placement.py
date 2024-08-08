import feffery_antd_components as fac
from dash import ctx, html, no_update
from dash.dependencies import ALL, Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    'top',
                    id={
                        'type': 'placement-trigger-notification',
                        'index': 'top',
                    },
                    type='primary',
                ),
                fac.AntdButton(
                    'bottom',
                    id={
                        'type': 'placement-trigger-notification',
                        'index': 'bottom',
                    },
                    type='primary',
                ),
            ],
        ),
        fac.AntdDivider(),
        fac.AntdSpace(
            [
                fac.AntdButton(
                    'topLeft',
                    id={
                        'type': 'placement-trigger-notification',
                        'index': 'topLeft',
                    },
                    type='primary',
                ),
                fac.AntdButton(
                    'topRight',
                    id={
                        'type': 'placement-trigger-notification',
                        'index': 'topRight',
                    },
                    type='primary',
                ),
            ],
        ),
        fac.AntdDivider(),
        fac.AntdSpace(
            [
                fac.AntdButton(
                    'bottomLeft',
                    id={
                        'type': 'placement-trigger-notification',
                        'index': 'bottomLeft',
                    },
                    type='primary',
                ),
                fac.AntdButton(
                    'bottomRight',
                    id={
                        'type': 'placement-trigger-notification',
                        'index': 'bottomRight',
                    },
                    type='primary',
                ),
            ],
        ),
        html.Div(id='notification-placement-demo'),
    ]

    return demo_contents


@app.callback(
    Output('notification-placement-demo', 'children'),
    Input({'type': 'placement-trigger-notification', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def notification_placement_demo(nClicks):
    triggered_index = ctx.triggered_id.index
    if nClicks:
        return fac.AntdNotification(
            message=f'{triggered_index.capitalize()} notification',
            description=f'This is the content of the {triggered_index} notification. '
            * 3,
            placement=triggered_index,
            type='info',
        )

    return no_update


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            'top',
            id={
                'type': 'placement-trigger-notification',
                'index': 'top',
            },
            type='primary',
        ),
        fac.AntdButton(
            'bottom',
            id={
                'type': 'placement-trigger-notification',
                'index': 'bottom',
            },
            type='primary',
        ),
    ],
),
fac.AntdDivider(),
fac.AntdSpace(
    [
        fac.AntdButton(
            'topLeft',
            id={
                'type': 'placement-trigger-notification',
                'index': 'topLeft',
            },
            type='primary',
        ),
        fac.AntdButton(
            'topRight',
            id={
                'type': 'placement-trigger-notification',
                'index': 'topRight',
            },
            type='primary',
        ),
    ],
),
fac.AntdDivider(),
fac.AntdSpace(
    [
        fac.AntdButton(
            'bottomLeft',
            id={
                'type': 'placement-trigger-notification',
                'index': 'bottomLeft',
            },
            type='primary',
        ),
        fac.AntdButton(
            'bottomRight',
            id={
                'type': 'placement-trigger-notification',
                'index': 'bottomRight',
            },
            type='primary',
        ),
    ],
),
html.Div(id='notification-placement-demo'),

...

@app.callback(
    Output('notification-placement-demo', 'children'),
    Input({'type': 'placement-trigger-notification', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def notification_placement_demo(nClicks):
    triggered_index = ctx.triggered_id.index
    if nClicks:
        return fac.AntdNotification(
            message=f'{triggered_index.capitalize()} notification',
            description=f'This is the content of the {triggered_index} notification. '
            * 3,
            placement=triggered_index,
            type='info',
        )

    return no_update
"""
    }
]
