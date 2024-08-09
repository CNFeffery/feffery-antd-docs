import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdButton('按钮1', id='spin-include-demo-trigger1'),
                fac.AntdButton('按钮2', id='spin-include-demo-trigger2'),
            ],
            style={'width': '100%', 'marginBottom': 10},
        ),
        fac.AntdSpin(
            [
                fac.AntdParagraph(id='spin-include-demo-output1'),
                fac.AntdParagraph(id='spin-include-demo-output2'),
            ],
            text='回调中',
            listenPropsMode='include',
            includeProps=['spin-include-demo-output1.children'],
        ),
    ]

    return demo_contents


@app.callback(
    Output('spin-include-demo-output1', 'children'),
    Input('spin-include-demo-trigger1', 'nClicks'),
    prevent_initial_call=True,
)
def spin_include_demo1(nClicks):
    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('spin-include-demo-output2', 'children'),
    Input('spin-include-demo-trigger2', 'nClicks'),
    prevent_initial_call=True,
)
def spin_include_demo2(nClicks):
    time.sleep(1)

    return f'按钮2: {nClicks}'


code_string = [
    {
        'code': """
[
    fac.AntdSpace(
        [
            fac.AntdButton('按钮1', id='spin-include-demo-trigger1'),
            fac.AntdButton('按钮2', id='spin-include-demo-trigger2'),
        ],
        style={'width': '100%', 'marginBottom': 10},
    ),
    fac.AntdSpin(
        [
            fac.AntdParagraph(id='spin-include-demo-output1'),
            fac.AntdParagraph(id='spin-include-demo-output2'),
        ],
        text='回调中',
        listenPropsMode='include',
        includeProps=['spin-include-demo-output1.children'],
    ),
]

...

@app.callback(
    Output('spin-include-demo-output1', 'children'),
    Input('spin-include-demo-trigger1', 'nClicks'),
    prevent_initial_call=True,
)
def spin_include_demo1(nClicks):
    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('spin-include-demo-output2', 'children'),
    Input('spin-include-demo-trigger2', 'nClicks'),
    prevent_initial_call=True,
)
def spin_include_demo2(nClicks):
    time.sleep(1)

    return f'按钮2: {nClicks}'
"""
    }
]
