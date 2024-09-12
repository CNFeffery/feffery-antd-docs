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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdSpace(
                [
                    fac.AntdCalendar(
                        id='calendar-demo',
                        locale='en-us',
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
                        locale='en-us',
                        defaultValue='2024/01/01',
                        format='YYYY/MM/DD',
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdSpace(
        [
            fac.AntdCalendar(
                id='calendar-demo',
                locale='en-us',
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
                locale='en-us',
                defaultValue='2024/01/01',
                format='YYYY/MM/DD',
                style={'width': '300px'},
            ),
            fac.AntdParagraph(id='calendar-format-demo-output'),
        ]
    ),
]

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
