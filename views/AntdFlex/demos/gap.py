import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdSpace(
            [
                fac.AntdRadioGroup(
                    id='flex-gap-demo-gap',
                    options=['small', 'middle', 'large', '66'],
                    value='small',
                ),
                fac.AntdFlex(
                    [fac.AntdButton('子元素', type='primary')] * 4,
                    id='flex-gap-demo',
                ),
            ],
            direction='vertical',
            size='large',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdRadioGroup(
                    id='flex-gap-demo-gap',
                    options=['small', 'middle', 'large', '66'],
                    value='small',
                ),
                fac.AntdFlex(
                    [fac.AntdButton('child', type='primary')] * 4,
                    id='flex-gap-demo',
                ),
            ],
            direction='vertical',
            size='large',
            style={'width': '100%'},
        )

    return demo_contents


@app.callback(
    Output('flex-gap-demo', 'gap'),
    Input('flex-gap-demo-gap', 'value'),
)
def update_demo_gap(value):
    if value == '66':
        return 66

    return value


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdRadioGroup(
            id='flex-gap-demo-gap',
            options=['small', 'middle', 'large', '66'],
            value='small',
        ),
        fac.AntdFlex(
            [fac.AntdButton('子元素', type='primary')] * 4,
            id='flex-gap-demo',
        ),
    ],
    direction='vertical',
    size='large',
    style={'width': '100%'},
)

...

@app.callback(
    Output('flex-gap-demo', 'gap'),
    Input('flex-gap-demo-gap', 'value'),
)
def update_demo_gap(value):
    if value == '66':
        return 66

    return value
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdRadioGroup(
            id='flex-gap-demo-gap',
            options=['small', 'middle', 'large', '66'],
            value='small',
        ),
        fac.AntdFlex(
            [fac.AntdButton('child', type='primary')] * 4,
            id='flex-gap-demo',
        ),
    ],
    direction='vertical',
    size='large',
    style={'width': '100%'},
)

...

@app.callback(
    Output('flex-gap-demo', 'gap'),
    Input('flex-gap-demo-gap', 'value'),
)
def update_demo_gap(value):
    if value == '66':
        return 66

    return value
"""
            }
        ]
