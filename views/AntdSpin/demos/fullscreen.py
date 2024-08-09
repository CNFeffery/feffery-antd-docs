import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                '触发示例',
                id='spin-fullscreen-demo-trigger',
                style={'marginBottom': 10},
            ),
            fac.AntdSpin(
                fac.AntdText(id='spin-fullscreen-demo-output'), fullscreen=True
            ),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('spin-fullscreen-demo-output', 'children'),
    Input('spin-fullscreen-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_fullscreen_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '触发示例',
            id='spin-fullscreen-demo-trigger',
            style={'marginBottom': 10},
        ),
        fac.AntdSpin(
            fac.AntdText(id='spin-fullscreen-demo-output'), fullscreen=True
        ),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('spin-fullscreen-demo-output', 'children'),
    Input('spin-fullscreen-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_fullscreen_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'
"""
    }
]
