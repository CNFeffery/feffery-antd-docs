import json
import feffery_antd_components as fac
from dash.dependencies import Component
from datetime import datetime, timedelta
from dash.dependencies import Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                '创建新的倒计时', id='countdown-create-new', type='primary'
            ),
            fac.Fragment(id='countdown-new-demo-container'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('countdown-new-demo-container', 'children'),
    Input('countdown-create-new', 'nClicks'),
    prevent_initial_call=True,
)
def create_new_countdown(nClicks):
    return fac.AntdSpace(
        [
            fac.AntdCountdown(
                id='countdown-new-demo',
                title='Countdown',
                value=(datetime.now() + timedelta(seconds=5)).strftime(
                    '%Y-%m-%d %H:%M:%S:%f'
                ),
            ),
            fac.AntdText(id='countdown-new-demo-finish-event'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )


@app.callback(
    Output('countdown-new-demo-finish-event', 'children'),
    Input('countdown-new-demo', 'finishEvent'),
    prevent_initial_call=True,
)
def show_countdown_finish_event(finishEvent):
    return json.dumps(
        {'finishEvent': finishEvent}, ensure_ascii=False, indent=4
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '创建新的倒计时', id='countdown-create-new', type='primary'
        ),
        fac.Fragment(id='countdown-new-demo-container'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('countdown-new-demo-container', 'children'),
    Input('countdown-create-new', 'nClicks'),
    prevent_initial_call=True,
)
def create_new_countdown(nClicks):
    return fac.AntdSpace(
        [
            fac.AntdCountdown(
                id='countdown-new-demo',
                title='Countdown',
                value=(datetime.now() + timedelta(seconds=5)).strftime(
                    '%Y-%m-%d %H:%M:%S:%f'
                ),
            ),
            fac.AntdText(id='countdown-new-demo-finish-event'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )


@app.callback(
    Output('countdown-new-demo-finish-event', 'children'),
    Input('countdown-new-demo', 'finishEvent'),
    prevent_initial_call=True,
)
def show_countdown_finish_event(finishEvent):
    return json.dumps(
        {'finishEvent': finishEvent}, ensure_ascii=False, indent=4
    )
"""
    }
]
