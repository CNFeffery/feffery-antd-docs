import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton('新通知', id='fragment-demo-trigger', type='primary'),
        fac.Fragment(id='fragment-demo'),
    ]

    return demo_contents


@app.callback(
    Output('fragment-demo', 'children'),
    Input('fragment-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def fragment_demo(nClicks):
    return fac.AntdMessage(content=f'nClicks: {nClicks}', type='info')


code_string = [
    {
        'code': """
[
    fac.AntdButton('新通知', id='fragment-demo-trigger', type='primary'),
    fac.Fragment(id='fragment-demo'),
]

...

@app.callback(
    Output('fragment-demo', 'children'),
    Input('fragment-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def fragment_demo(nClicks):
    return fac.AntdMessage(content=f'nClicks: {nClicks}', type='info')
"""
    }
]
