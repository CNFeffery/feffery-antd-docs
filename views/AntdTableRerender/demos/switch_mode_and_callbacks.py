import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTable(
            id='table-rerender-switch-demo',
            columns=[
                {
                    'title': 'switch示例',
                    'dataIndex': 'switch示例',
                    'renderOptions': {'renderType': 'switch'},
                }
            ],
            data=[
                {
                    'switch示例': {
                        'checked': i % 2 == 0,
                        'checkedChildren': '开',
                        'unCheckedChildren': '关',
                        'custom': 'balabalabalabala',
                    }
                }
                for i in range(1, 4)
            ],
            bordered=True,
            style={'width': 200},
        ),
        html.Pre(id='table-rerender-switch-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('table-rerender-switch-demo-output', 'children'),
    [
        Input('table-rerender-switch-demo', 'recentlySwitchDataIndex'),
        Input('table-rerender-switch-demo', 'recentlySwitchStatus'),
        Input('table-rerender-switch-demo', 'recentlySwitchRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_switch_demo(
    recentlySwitchDataIndex, recentlySwitchStatus, recentlySwitchRow
):
    return json.dumps(
        dict(
            recentlySwitchDataIndex=recentlySwitchDataIndex,
            recentlySwitchStatus=recentlySwitchStatus,
            recentlySwitchRow=recentlySwitchRow,
        ),
        indent=4,
        ensure_ascii=False,
    )


code_string = [
    {
        'code': """
[
    fac.AntdTable(
        id='table-rerender-switch-demo',
        columns=[
            {
                'title': 'switch示例',
                'dataIndex': 'switch示例',
                'renderOptions': {'renderType': 'switch'},
            }
        ],
        data=[
            {
                'switch示例': {
                    'checked': i % 2 == 0,
                    'checkedChildren': '开',
                    'unCheckedChildren': '关',
                    'custom': 'balabalabalabala',
                }
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-switch-demo-output'),
]

...

@app.callback(
    Output('table-rerender-switch-demo-output', 'children'),
    [
        Input('table-rerender-switch-demo', 'recentlySwitchDataIndex'),
        Input('table-rerender-switch-demo', 'recentlySwitchStatus'),
        Input('table-rerender-switch-demo', 'recentlySwitchRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_switch_demo(
    recentlySwitchDataIndex, recentlySwitchStatus, recentlySwitchRow
):
    return json.dumps(
        dict(
            recentlySwitchDataIndex=recentlySwitchDataIndex,
            recentlySwitchStatus=recentlySwitchStatus,
            recentlySwitchRow=recentlySwitchRow,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
    }
]
