import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdCalendar(
            id='calendar-cell-click-event-demo',
        ),
        html.Pre(id='calendar-cell-click-event-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('calendar-cell-click-event-demo-output', 'children'),
    Input('calendar-cell-click-event-demo', 'cellClickEvent'),
    prevent_initial_call=True,
)
def calendar_cell_click_event_demo(cellClickEvent):
    return json.dumps(cellClickEvent, indent=4, ensure_ascii=False)


code_string = [
    {
        'code': """
[
    fac.AntdCalendar(
        id='calendar-cell-click-event-demo',
    ),
    html.Pre(id='calendar-cell-click-event-demo-output'),
]

...

@app.callback(
    Output('calendar-cell-click-event-demo-output', 'children'),
    Input('calendar-cell-click-event-demo', 'cellClickEvent'),
    prevent_initial_call=True,
)
def calendar_cell_click_event_demo(cellClickEvent):
    return json.dumps(cellClickEvent, indent=4, ensure_ascii=False)
"""
    }
]
