import feffery_antd_components as fac
from dash import ctx, html, no_update
from dash.dependencies import ALL, Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdButton(
                'Default',
                id={'type': 'trigger-notification', 'index': 'default'},
                type='default',
            ),
            fac.AntdButton(
                'Info',
                id={'type': 'trigger-notification', 'index': 'info'},
                type='default',
            ),
            fac.AntdButton(
                'Success',
                id={'type': 'trigger-notification', 'index': 'success'},
                type='default',
            ),
            fac.AntdButton(
                'Warning',
                id={'type': 'trigger-notification', 'index': 'warning'},
                type='default',
            ),
            fac.AntdButton(
                'Error',
                id={'type': 'trigger-notification', 'index': 'error'},
                type='default',
            ),
            html.Div(id='notification-type-demo'),
        ],
        gap='small',
        align='flex-start',
    )

    return demo_contents


@app.callback(
    Output('notification-type-demo', 'children'),
    Input({'type': 'trigger-notification', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def notification_type_demo(nClicks):
    triggered_index = ctx.triggered_id.index
    if nClicks:
        return fac.AntdNotification(
            message=f'{triggered_index.capitalize()} notification',
            description=f'This is the content of the {triggered_index} notification. '
            * 3,
            type=triggered_index,
        )

    return no_update


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdButton(
            'Default',
            id={'type': 'trigger-notification', 'index': 'default'},
            type='default',
        ),
        fac.AntdButton(
            'Info',
            id={'type': 'trigger-notification', 'index': 'info'},
            type='default',
        ),
        fac.AntdButton(
            'Success',
            id={'type': 'trigger-notification', 'index': 'success'},
            type='default',
        ),
        fac.AntdButton(
            'Warning',
            id={'type': 'trigger-notification', 'index': 'warning'},
            type='default',
        ),
        fac.AntdButton(
            'Error',
            id={'type': 'trigger-notification', 'index': 'error'},
            type='default',
        ),
        html.Div(id='notification-type-demo'),
    ],
    gap='small',
    align='flex-start',
)

...

@app.callback(
    Output('notification-type-demo', 'children'),
    Input({'type': 'trigger-notification', 'index': ALL}, 'nClicks'),
    prevent_initial_call=True,
)
def notification_type_demo(nClicks):
    triggered_index = ctx.triggered_id.index
    if nClicks:
        return fac.AntdNotification(
            message=f'{triggered_index.capitalize()} notification',
            description=f'This is the content of the {triggered_index} notification. '
            * 3,
            type=triggered_index,
        )

    return no_update
"""
    }
]
