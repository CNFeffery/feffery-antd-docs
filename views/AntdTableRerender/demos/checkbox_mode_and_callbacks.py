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
            id='table-rerender-checkbox-demo',
            columns=[
                {
                    'title': 'checkbox示例',
                    'dataIndex': 'checkbox示例',
                    'renderOptions': {'renderType': 'checkbox'},
                }
            ],
            data=[
                {
                    'checkbox示例': {
                        'checked': i % 2 == 0,
                        'label': f'选项{i}',
                        'custom': 'balabalabalabala',
                    }
                }
                for i in range(1, 4)
            ],
            bordered=True,
            style={'width': 200},
        ),
        html.Pre(id='table-rerender-checkbox-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('table-rerender-checkbox-demo-output', 'children'),
    [
        Input('table-rerender-checkbox-demo', 'recentlyCheckedLabel'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedDataIndex'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedStatus'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_checkbox_demo(
    recentlyCheckedLabel,
    recentlyCheckedDataIndex,
    recentlyCheckedStatus,
    recentlyCheckedRow,
):
    return json.dumps(
        dict(
            recentlyCheckedLabel=recentlyCheckedLabel,
            recentlyCheckedDataIndex=recentlyCheckedDataIndex,
            recentlyCheckedStatus=recentlyCheckedStatus,
            recentlyCheckedRow=recentlyCheckedRow,
        ),
        indent=4,
        ensure_ascii=False,
    )


code_string = [
    {
        'code': """
[
    fac.AntdTable(
        id='table-rerender-checkbox-demo',
        columns=[
            {
                'title': 'checkbox示例',
                'dataIndex': 'checkbox示例',
                'renderOptions': {'renderType': 'checkbox'},
            }
        ],
        data=[
            {
                'checkbox示例': {
                    'checked': i % 2 == 0,
                    'label': f'选项{i}',
                    'custom': 'balabalabalabala',
                }
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 200},
    ),
    html.Pre(id='table-rerender-checkbox-demo-output'),
]

...

@app.callback(
    Output('table-rerender-checkbox-demo-output', 'children'),
    [
        Input('table-rerender-checkbox-demo', 'recentlyCheckedLabel'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedDataIndex'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedStatus'),
        Input('table-rerender-checkbox-demo', 'recentlyCheckedRow'),
    ],
    prevent_initial_call=True,
)
def table_rerender_checkbox_demo(
    recentlyCheckedLabel,
    recentlyCheckedDataIndex,
    recentlyCheckedStatus,
    recentlyCheckedRow,
):
    return json.dumps(
        dict(
            recentlyCheckedLabel=recentlyCheckedLabel,
            recentlyCheckedDataIndex=recentlyCheckedDataIndex,
            recentlyCheckedStatus=recentlyCheckedStatus,
            recentlyCheckedRow=recentlyCheckedRow,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
    }
]
