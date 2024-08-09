import time
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例',
            id='spin-custom-demo-trigger',
            style={'marginBottom': 10},
        ),
        fac.AntdSpin(
            fac.AntdText('nClicks: 0', id='spin-custom-demo-output'),
            indicator=fuc.FefferyExtraSpinner(type='heart'),
        ),
    ]

    return demo_contents


@app.callback(
    Output('spin-custom-demo-output', 'children'),
    Input('spin-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_custom_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例',
        id='spin-custom-demo-trigger',
        style={'marginBottom': 10},
    ),
    fac.AntdSpin(
        fac.AntdText('nClicks: 0', id='spin-custom-demo-output'),
        indicator=fuc.FefferyExtraSpinner(type='heart'),
    ),
]

...

@app.callback(
    Output('spin-custom-demo-output', 'children'),
    Input('spin-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_custom_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'
"""
    }
]
