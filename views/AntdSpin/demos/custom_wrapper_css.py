import time
from dash import html
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
            id='spin-custom-wrapper-demo-trigger',
            style={'marginBottom': 10},
        ),
        # 动态注入css片段
        fuc.FefferyStyle(
            rawStyle="""
.spin-custom-wrapper {
    height: 100%;
}
"""
        ),
        html.Div(
            fac.AntdSpin(
                fac.AntdText(id='spin-custom-wrapper-demo-output'),
                text='回调中',
                wrapperClassName='spin-custom-wrapper',
            ),
            style={'height': 500, 'border': '1px dashed #bae7ff'},
        ),
    ]

    return demo_contents


@app.callback(
    Output('spin-custom-wrapper-demo-output', 'children'),
    Input('spin-custom-wrapper-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_custom_wrapper_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': '''
[
    fac.AntdButton(
        '触发示例',
        id='spin-custom-wrapper-demo-trigger',
        style={'marginBottom': 10},
    ),
    # 动态注入css片段
    fuc.FefferyStyle(
        rawStyle="""
.spin-custom-wrapper {
    height: 100%;
}
"""
    ),
    html.Div(
        fac.AntdSpin(
            fac.AntdText(id='spin-custom-wrapper-demo-output'),
            text='回调中',
            wrapperClassName='spin-custom-wrapper',
        ),
        style={'height': 500, 'border': '1px dashed #bae7ff'},
    ),
]

...

@app.callback(
    Output('spin-custom-wrapper-demo-output', 'children'),
    Input('spin-custom-wrapper-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def spin_custom_wrapper_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'
'''
    }
]
