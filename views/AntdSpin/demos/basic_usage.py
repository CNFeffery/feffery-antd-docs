import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例', id='spin-basic-demo-trigger', style={'marginBottom': 10}
        ),
        fac.AntdSpin(fac.AntdText(id='spin-basic-demo-output'), text='回调中'),
    ]

    return demo_contents


@app.callback(
    Output('spin-basic-demo-output', 'children'),
    Input('spin-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_basic_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例', id='spin-basic-demo-trigger', style={'marginBottom': 10}
    ),
    fac.AntdSpin(fac.AntdText(id='spin-basic-demo-output'), text='回调中'),
]

...

@app.callback(
    Output('spin-basic-demo-output', 'children'),
    Input('spin-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_basic_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'
"""
    }
]
