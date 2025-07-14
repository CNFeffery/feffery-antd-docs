import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSegmented(
                id='divider-size-demo',
                options=['small', 'middle', 'large'],
                value='large',
            ),
            'Demo content',
            fac.AntdDivider(id='divider-size-demo-output'),
            'Demo content',
        ],
        size=0,
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('divider-size-demo-output', 'size'),
    Input('divider-size-demo', 'value'),
)
def update_divider_size(value):
    return value


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSegmented(
            id='divider-size-demo',
            options=['small', 'middle', 'large'],
            value='large',
        ),
        'Demo content',
        fac.AntdDivider(id='divider-size-demo-output'),
        'Demo content',
    ],
    size=0,
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('divider-size-demo-output', 'size'),
    Input('divider-size-demo', 'value'),
)
def update_divider_size(value):
    return value
"""
    }
]
