import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例对话框', id='modal-footer-demo-open', type='primary'
        ),
        fac.AntdModal(
            '示例内容',
            id='modal-footer-demo',
            title='对话框示例',
            renderFooter=True,
        ),
    ]

    return demo_contents


@app.callback(
    Output('modal-footer-demo', 'visible'),
    Input('modal-footer-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_footer_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例对话框', id='modal-footer-demo-open', type='primary'
    ),
    fac.AntdModal(
        '示例内容',
        id='modal-footer-demo',
        title='对话框示例',
        renderFooter=True,
    ),
]

...

@app.callback(
    Output('modal-footer-demo', 'visible'),
    Input('modal-footer-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_footer_demo(nClicks):
    return True
"""
    }
]
