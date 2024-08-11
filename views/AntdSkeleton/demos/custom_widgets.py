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
            id='skeleton-custom-demo-trigger',
            style={'marginBottom': 10},
        ),
        fac.AntdSkeleton(
            fac.AntdParagraph(id='skeleton-custom-demo-output'),
            active=True,
            avatar={'size': 'large', 'shape': 'square'},
            paragraph={'rows': 10, 'width': '20%'},
            title={'width': '4rem'},
        ),
    ]

    return demo_contents


@app.callback(
    Output('skeleton-custom-demo-output', 'children'),
    Input('skeleton-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def skeleton_custom_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'


code_string = [
    {
        'code': """
[
    fac.AntdButton(
        '触发示例',
        id='skeleton-custom-demo-trigger',
        style={'marginBottom': 10},
    ),
    fac.AntdSkeleton(
        fac.AntdParagraph(id='skeleton-custom-demo-output'),
        active=True,
        avatar={'size': 'large', 'shape': 'square'},
        paragraph={'rows': 10, 'width': '20%'},
        title={'width': '4rem'},
    ),
]

...

@app.callback(
    Output('skeleton-custom-demo-output', 'children'),
    Input('skeleton-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True,
)
def skeleton_custom_demo(nClicks):
    time.sleep(2)

    return f'nClicks: {nClicks}'
"""
    }
]
