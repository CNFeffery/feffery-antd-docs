import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例对话框', id='modal-prevent-close-demo-open', type='primary'
        ),
        fac.AntdModal(
            '示例内容',
            id='modal-prevent-close-demo',
            title='对话框示例',
            preventClose=True,
            okClickClose=False,
        ),
        fac.AntdModal(
            '确认要关闭模态框吗',
            id='modal-prevent-close-confirm-demo',
            title='关闭二次确认',
            renderFooter=True,
            zIndex=99999,
        ),
    ]

    return demo_contents


@app.callback(
    Output('modal-prevent-close-demo', 'visible'),
    Input('modal-prevent-close-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def open_modal_prevent_close(nClicks):
    return True


@app.callback(
    Output('modal-prevent-close-confirm-demo', 'visible'),
    Input('modal-prevent-close-demo', 'cancelCounts'),
    prevent_initial_call=True,
)
def open_modal_prevent_close_confirm(cancelCounts):
    return True


@app.callback(
    Output('modal-prevent-close-demo', 'visible', allow_duplicate=True),
    Input('modal-prevent-close-confirm-demo', 'okCounts'),
    prevent_initial_call=True,
)
def close_modal_prevent_close_confirm(okCounts):
    return False


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例对话框', id='modal-prevent-close-demo-open', type='primary'
    ),
    fac.AntdModal(
        '示例内容',
        id='modal-prevent-close-demo',
        title='对话框示例',
        preventClose=True,
        okClickClose=False,
    ),
    fac.AntdModal(
        '确认要关闭模态框吗',
        id='modal-prevent-close-confirm-demo',
        title='关闭二次确认',
        renderFooter=True,
        zIndex=99999,
    ),
]

...

@app.callback(
    Output('modal-prevent-close-demo', 'visible'),
    Input('modal-prevent-close-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def open_modal_prevent_close(nClicks):
    return True


@app.callback(
    Output('modal-prevent-close-confirm-demo', 'visible'),
    Input('modal-prevent-close-demo', 'cancelCounts'),
    prevent_initial_call=True,
)
def open_modal_prevent_close_confirm(cancelCounts):
    return True


@app.callback(
    Output('modal-prevent-close-demo', 'visible', allow_duplicate=True),
    Input('modal-prevent-close-confirm-demo', 'okCounts'),
    prevent_initial_call=True,
)
def close_modal_prevent_close_confirm(okCounts):
    return False
"""
    }
]
