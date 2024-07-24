import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdPopconfirm(
                fac.AntdButton('触发'), id='popconfirm-demo', title='确认继续'
            ),
            html.Pre(id='popconfirm-demo-output'),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('popconfirm-demo-output', 'children'),
    Input('popconfirm-demo', 'confirmCounts'),
    Input('popconfirm-demo', 'cancelCounts'),
    prevent_initial_call=True,
)
def popconfirm_callback_demo(confirmCounts, cancelCounts):
    return json.dumps(
        {'confirmCounts': confirmCounts, 'cancelCounts': cancelCounts}, indent=4
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdPopconfirm(
            fac.AntdButton('触发'), id='popconfirm-demo', title='确认继续'
        ),
        html.Pre(id='popconfirm-demo-output'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('popconfirm-demo-output', 'children'),
    Input('popconfirm-demo', 'confirmCounts'),
    Input('popconfirm-demo', 'cancelCounts'),
    prevent_initial_call=True,
)
def popconfirm_callback_demo(confirmCounts, cancelCounts):
    return json.dumps(
        {'confirmCounts': confirmCounts, 'cancelCounts': cancelCounts}, indent=4
    )
"""
    }
]
