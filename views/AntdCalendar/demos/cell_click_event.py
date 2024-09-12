import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdCalendar(
                id='calendar-cell-click-event-demo',
            ),
            html.Pre(id='calendar-cell-click-event-demo-output'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdCalendar(
                id='calendar-cell-click-event-demo',
                locale='en-us',
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdCalendar(
        id='calendar-cell-click-event-demo',
        locale='en-us',
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
