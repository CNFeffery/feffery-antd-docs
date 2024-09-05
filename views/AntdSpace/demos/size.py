import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdRadioGroup(
                id='space-size-demo-size',
                options=['small', 'middle', 'large', '66'],
                value='small',
            ),
            fac.AntdSpace(
                [fac.AntdButton('child', type='primary')] * 4,
                id='space-size-demo',
            ),
        ],
        direction='vertical',
        size='large',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('space-size-demo', 'size'),
    Input('space-size-demo-size', 'value'),
)
def update_demo_size(value):
    if value == '66':
        return 66

    return value


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdRadioGroup(
            id='space-size-demo-size',
            options=['small', 'middle', 'large', '66'],
            value='small',
        ),
        fac.AntdSpace(
            [fac.AntdButton('child', type='primary')] * 4,
            id='space-size-demo',
        ),
    ],
    direction='vertical',
    size='large',
    style={'width': '100%'},
)

...

@app.callback(
    Output('space-size-demo', 'size'),
    Input('space-size-demo-size', 'value'),
)
def update_demo_size(value):
    if value == '66':
        return 66

    return value
"""
    }
]
