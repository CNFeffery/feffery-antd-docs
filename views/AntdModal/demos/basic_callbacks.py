import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例对话框', id='modal-callback-demo-open', type='primary'
        ),
        fac.AntdModal(
            '示例内容',
            id='modal-callback-demo',
            title='对话框示例',
            renderFooter=True,
        ),
        html.Pre(id='modal-callback-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('modal-callback-demo', 'visible'),
    Input('modal-callback-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def handle_modal_visible(nClicks):
    return True


@app.callback(
    Output('modal-callback-demo-output', 'children'),
    [
        Input('modal-callback-demo', 'okCounts'),
        Input('modal-callback-demo', 'cancelCounts'),
        Input('modal-callback-demo', 'closeCounts'),
    ],
    prevent_initial_call=True,
)
def handle_modal_callback_demo(okCounts, cancelCounts, closeCounts):
    return json.dumps(
        dict(
            okCounts=okCounts,
            cancelCounts=cancelCounts,
            closeCounts=closeCounts,
        ),
        indent=4,
        ensure_ascii=False,
    )


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例对话框', id='modal-callback-demo-open', type='primary'
    ),
    fac.AntdModal(
        '示例内容',
        id='modal-callback-demo',
        title='对话框示例',
        renderFooter=True,
    ),
    html.Pre(id='modal-callback-demo-output'),
]

...

@app.callback(
    Output('modal-callback-demo', 'visible'),
    Input('modal-callback-demo-open', 'nClicks'),
    prevent_initial_call=True,
)
def handle_modal_visible(nClicks):
    return True


@app.callback(
    Output('modal-callback-demo-output', 'children'),
    [
        Input('modal-callback-demo', 'okCounts'),
        Input('modal-callback-demo', 'cancelCounts'),
        Input('modal-callback-demo', 'closeCounts'),
    ],
    prevent_initial_call=True,
)
def handle_modal_callback_demo(okCounts, cancelCounts, closeCounts):
    return json.dumps(
        dict(
            okCounts=okCounts,
            cancelCounts=cancelCounts,
            closeCounts=closeCounts,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
    }
]
