from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '打开示例抽屉', id='drawer-footer-demo-open', type='primary'
        ),
        fac.AntdDrawer(
            html.Div('示例内容', style={'height': 10000}),
            id='drawer-footer-demo',
            title='抽屉示例',
            footer=fac.AntdButton('页脚内容示例', type='primary'),
        ),
    ]

    return demo_contents


@app.callback(
    Output('drawer-footer-demo', 'visible'),
    Input('drawer-footer-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_footer_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '打开示例抽屉', id='drawer-footer-demo-open', type='primary'
    ),
    fac.AntdDrawer(
        html.Div('示例内容', style={'height': 10000}),
        id='drawer-footer-demo',
        title='抽屉示例',
        footer=fac.AntdButton('页脚内容示例', type='primary'),
    ),
]

...

@app.callback(
    Output('drawer-footer-demo', 'visible'),
    Input('drawer-footer-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def drawer_footer_demo(nClicks):
    return True
"""
    }
]
