import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSegmentedColoring(
            id='segmented-coloring-color-block-click-event-demo',
            size='small',
            min=-10,
            max=10,
            breakpoints=[0, 1, 2, 3, 4, 5],
            colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
        ),
        html.Pre(id='segmented-coloring-color-block-click-event-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output(
        'segmented-coloring-color-block-click-event-demo-output', 'children'
    ),
    Input(
        'segmented-coloring-color-block-click-event-demo',
        'colorBlockClickEvent',
    ),
    prevent_initial_call=True,
)
def show_color_block_click_event(colorBlockClickEvent):
    return json.dumps(colorBlockClickEvent, indent=4, ensure_ascii=False)


code_string = [
    {
        'code': """
[
    fac.AntdSegmentedColoring(
        id='segmented-coloring-color-block-click-event-demo',
        size='small',
        min=-10,
        max=10,
        breakpoints=[0, 1, 2, 3, 4, 5],
        colors=['#deecf9', '#71afe5', '#2b88d8', '#0078d4', '#106ebe'],
    ),
    html.Pre(id='segmented-coloring-color-block-click-event-demo-output'),
]

...

@app.callback(
    Output(
        'segmented-coloring-color-block-click-event-demo-output', 'children'
    ),
    Input(
        'segmented-coloring-color-block-click-event-demo',
        'colorBlockClickEvent',
    ),
    prevent_initial_call=True,
)
def show_color_block_click_event(colorBlockClickEvent):
    return json.dumps(colorBlockClickEvent, indent=4, ensure_ascii=False)
"""
    }
]
