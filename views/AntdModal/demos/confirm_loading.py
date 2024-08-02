import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例对话框',
            id='modal-confirm-loading-demo-open',
            type='primary',
        ),
        fac.AntdModal(
            '示例内容',
            id='modal-confirm-loading-demo',
            title='对话框示例',
            confirmAutoSpin=True,
            loadingOkText='运算中',
            okClickClose=False,
            renderFooter=True,
        ),
    ]

    return demo_contents


@app.callback(
    Output('modal-confirm-loading-demo', 'visible'),
    Input('modal-confirm-loading-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_confirm_loading_demo(nClicks):
    return True


@app.callback(
    Output('modal-confirm-loading-demo', 'confirmLoading'),
    Input('modal-confirm-loading-demo', 'okCounts'),
    prevent_initial_call=True,
)
def modal_confirm_loading_reset(okCounts):
    time.sleep(2)

    return False


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例对话框',
        id='modal-confirm-loading-demo-open',
        type='primary',
    ),
    fac.AntdModal(
        '示例内容',
        id='modal-confirm-loading-demo',
        title='对话框示例',
        confirmAutoSpin=True,
        loadingOkText='运算中',
        okClickClose=False,
        renderFooter=True,
    ),
]

...

@app.callback(
    Output('modal-confirm-loading-demo', 'visible'),
    Input('modal-confirm-loading-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def modal_confirm_loading_demo(nClicks):
    return True


@app.callback(
    Output('modal-confirm-loading-demo', 'confirmLoading'),
    Input('modal-confirm-loading-demo', 'okCounts'),
    prevent_initial_call=True,
)
def modal_confirm_loading_reset(okCounts):
    time.sleep(2)

    return False
"""
    }
]
