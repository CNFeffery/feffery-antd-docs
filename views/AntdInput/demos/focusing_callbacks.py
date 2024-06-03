import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdInput(
                id='input-focusing-demo',
                placeholder='尝试聚焦于此输入框',
            ),
            fac.AntdCard(
                id='input-focusing-demo-output', headStyle={'display': 'none'}
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


@app.callback(
    Output('input-focusing-demo-output', 'children'),
    Input('input-focusing-demo', 'focusing'),
)
def input_focusing_dmeo(focusing):
    return f'focusing: {focusing}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdInput(
            id='input-focusing-demo',
            placeholder='尝试聚焦于此输入框',
        ),
        fac.AntdCard(
            id='input-focusing-demo-output', headStyle={'display': 'none'}
        ),
    ],
    direction='vertical',
    style={'width': 350},
)

...

@app.callback(
    Output('input-focusing-demo-output', 'children'),
    Input('input-focusing-demo', 'focusing'),
)
def input_focusing_dmeo(focusing):
    return f'focusing: {focusing}'
"""
    }
]
