import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '打开示例抽屉', id='drawer-basic-demo-open', type='primary'
        ),
        fac.AntdDrawer(
            '示例内容', title='基础抽屉示例', id='drawer-basic-demo'
        ),
    ]

    return demo_contents


@app.callback(
    Output('drawer-basic-demo', 'visible'),
    Input('drawer-basic-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_basic_demo(nCLicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '打开示例抽屉', id='drawer-basic-demo-open', type='primary'
    ),
    fac.AntdDrawer(
        '示例内容', title='基础抽屉示例', id='drawer-basic-demo'
    ),
]

...

@app.callback(
    Output('drawer-basic-demo', 'visible'),
    Input('drawer-basic-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_basic_demo(nCLicks):
    return True
"""
    }
]
