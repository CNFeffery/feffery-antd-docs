import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例对话框', id='modal-loading-demo-open', type='primary'
        ),
        fac.AntdModal(
            '示例内容',
            id='modal-loading-demo',
            title='loading状态示例',
            loading=True,
        ),
    ]

    return demo_contents


@app.callback(
    Output('modal-loading-demo', 'visible'),
    Input('modal-loading-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_loading_demo(nClicks):
    return True


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例对话框', id='modal-loading-demo-open', type='primary'
    ),
    fac.AntdModal(
        '示例内容',
        id='modal-loading-demo',
        title='loading状态示例',
        loading=True,
    ),
]

...

@app.callback(
    Output('modal-loading-demo', 'visible'),
    Input('modal-loading-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_loading_demo(nClicks):
    return True
"""
    }
]
