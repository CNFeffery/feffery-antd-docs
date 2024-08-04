import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


@app.callback(
    Output('flex-gap-demo', 'gap'),
    Input('flex-gap-demo-gap', 'value'),
)
def update_demo_gap(value):
    if value == '66':
        return 66

    return value


code_string = [
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
