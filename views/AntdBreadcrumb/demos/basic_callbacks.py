import feffery_antd_components as fac
import json
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdBreadcrumb(
            id='breadcrumnb-demo',
            items=[
                {'title': '首页', 'key': '首页'},
                {'title': '下属页面1', 'key': '下属页面1'},
                {'title': '下属页面1-1', 'key': '下属页面1-1'},
            ],
        ),
        html.Pre(id='breadcrumnb-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('breadcrumnb-demo-output', 'children'),
    Input('breadcrumnb-demo', 'clickedItem'),
    prevent_initial_call=True,
)
def breadcrumb_callback_demo(clickedItem):
    return json.dumps(
        dict(clickedItem=clickedItem), indent=4, ensure_ascii=False
    )


code_string = [
    {
        'code': """
fac.AntdBreadcrumb(
    id='breadcrumnb-demo',
    items=[
        {'title': '首页', 'key': '首页'},
        {'title': '下属页面1', 'key': '下属页面1'},
        {'title': '下属页面1-1', 'key': '下属页面1-1'},
    ],
),
html.Pre(id='breadcrumnb-demo-output'),

...

import json

...

@app.callback(
    Output('breadcrumnb-demo-output', 'children'),
    Input('breadcrumnb-demo', 'clickedItem'),
    prevent_initial_call=True
)
def breadcrumb_callback_demo(clickedItem):

    return json.dumps(
        dict(clickedItem=clickedItem),
        indent=4,
        ensure_ascii=False
    )
"""
    }
]
