import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdButton(
            '触发示例',
            id='skeleton-active-demo-trigger',
            style={'marginBottom': 10},
        ),
        fac.AntdSkeleton(
            fac.AntdParagraph(id='skeleton-active-demo-output'), active=True
        ),
    ]

    return demo_contents


@app.callback(
    Output('skeleton-active-demo-output', 'children'),
    Input('skeleton-active-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def skeleton_active_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例',
        id='skeleton-active-demo-trigger',
        style={'marginBottom': 10},
    ),
    fac.AntdSkeleton(
        fac.AntdParagraph(id='skeleton-active-demo-output'), active=True
    ),
]

...

@app.callback(
    Output('skeleton-active-demo-output', 'children'),
    Input('skeleton-active-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def skeleton_active_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'
"""
    }
]
