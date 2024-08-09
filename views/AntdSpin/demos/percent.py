import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例',
            id='spin-percent-demo-trigger',
            style={'marginBottom': 10},
        ),
        fac.AntdSpin(
            fac.AntdText(id='spin-percent-demo-output'),
            percent='auto',
        ),
    ]

    return demo_contents


@app.callback(
    Output('spin-percent-demo-output', 'children'),
    Input('spin-percent-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_percent_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例',
        id='spin-percent-demo-trigger',
        style={'marginBottom': 10},
    ),
    fac.AntdSpin(
        fac.AntdText(id='spin-percent-demo-output'),
        percent='auto',
    ),
]

...

@app.callback(
    Output('spin-percent-demo-output', 'children'),
    Input('spin-percent-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_percent_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'
"""
    }
]
