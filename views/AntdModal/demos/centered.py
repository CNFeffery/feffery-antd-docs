import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例对话框', id='modal-centered-demo-open', type='primary'
        ),
        fac.AntdModal(
            '示例内容',
            id='modal-centered-demo',
            title='对话框示例',
            centered=True,
        ),
    ]

    return demo_contents


@app.callback(
    Output('modal-centered-demo', 'visible'),
    Input('modal-centered-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_centered_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例对话框', id='modal-centered-demo-open', type='primary'
    ),
    fac.AntdModal(
        '示例内容',
        id='modal-centered-demo',
        title='对话框示例',
        centered=True,
    ),
]

...

@app.callback(
    Output('modal-centered-demo', 'visible'),
    Input('modal-centered-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_centered_demo(nClicks):
    return True
"""
    }
]
