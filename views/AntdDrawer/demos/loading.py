import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '打开示例抽屉', id='drawer-loading-demo-open', type='primary'
        ),
        fac.AntdDrawer(
            '示例内容',
            title='加载状态示例',
            id='drawer-loading-demo',
            loading=True,
        ),
    ]

    return demo_contents


@app.callback(
    Output('drawer-loading-demo', 'visible'),
    Input('drawer-loading-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_loading_demo(nCLicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '打开示例抽屉', id='drawer-loading-demo-open', type='primary'
    ),
    fac.AntdDrawer(
        '示例内容',
        title='加载状态示例',
        id='drawer-loading-demo',
        loading=True,
    ),
]

...

@app.callback(
    Output('drawer-loading-demo', 'visible'),
    Input('drawer-loading-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_loading_demo(nCLicks):
    return True
"""
    }
]
