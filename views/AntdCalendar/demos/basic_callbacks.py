import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                fac.AntdCalendar(
                    id='calendar-demo',
                    defaultValue='2024-01-01',
                    style={'width': '300px'},
                ),
                fac.AntdParagraph(id='calendar-demo-output'),
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdCalendar(
                    id='calendar-format-demo',
                    defaultValue='2024年01月01日',
                    format='YYYY年MM月DD日',
                    style={'width': '300px'},
                ),
                fac.AntdParagraph(id='calendar-format-demo-output'),
            ]
        ),
    ]

    return demo_contents


@app.callback(
    Output('calendar-demo-output', 'children'), Input('calendar-demo', 'value')
)
def calendar_demo(value):
    return f'value: {value}'


@app.callback(
    Output('calendar-format-demo-output', 'children'),
    Input('calendar-format-demo', 'value'),
)
def calendar_format_demo(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCalendar(
            id='calendar-demo',
            defaultValue='2024-01-01',
            style={
                'width': '300px'
            }
        ),
        fac.AntdParagraph(
            id='calendar-demo-output'
        )
    ]
),

fac.AntdSpace(
    [
        fac.AntdCalendar(
            id='calendar-format-demo',
            defaultValue='2024年01月01日',
            format='YYYY年MM月DD日',
            style={
                'width': '300px'
            }
        ),
        fac.AntdParagraph(
            id='calendar-format-demo-output'
        )
    ]
)

...

@app.callback(
    Output('calendar-demo-output', 'children'),
    Input('calendar-demo', 'value')
)
def calendar_demo(value):

    return f'value: {value}'


@app.callback(
    Output('calendar-format-demo-output', 'children'),
    Input('calendar-format-demo', 'value')
)
def calendar_format_demo(value):

    return f'value: {value}'
"""
    }
]
