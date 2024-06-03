import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdInput(
                        id=f'input-{mode}-mode-demo',
                        placeholder=f'mode="{mode}"{"（默认）" if mode == "default" else ""}',
                        mode=mode,
                    )
                    for mode in ['default', 'search', 'text-area', 'password']
                ],
                direction='vertical',
                style={'width': '100%'},
            ),
            fac.AntdCard(id='input-demo-output', headStyle={'display': 'none'}),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


@app.callback(
    Output('input-demo-output', 'children'),
    [
        Input(f'input-{mode}-mode-demo', 'value')
        for mode in ['default', 'search', 'text-area', 'password']
    ],
)
def input_mode_demo(*value_list):
    return fac.AntdSpace(
        [
            fac.AntdText(f'{mode}模式value：{value_list[i]}')
            for i, mode in enumerate(
                ['default', 'search', 'text-area', 'password']
            )
        ],
        direction='vertical',
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdInput(
                    id=f'input-{mode}-mode-demo',
                    placeholder=f'mode="{mode}"{"（默认）" if mode == "default" else ""}',
                    mode=mode,
                )
                for mode in ['default', 'search', 'text-area', 'password']
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
        fac.AntdCard(id='input-demo-output', headStyle={'display': 'none'}),
    ],
    direction='vertical',
    style={'width': 350},
)


@app.callback(
    Output('input-demo-output', 'children'),
    [
        Input(f'input-{mode}-mode-demo', 'value')
        for mode in ['default', 'search', 'text-area', 'password']
    ],
)
def input_mode_demo(*value_list):
    return fac.AntdSpace(
        [
            fac.AntdText(f'{mode}模式value：{value_list[i]}')
            for i, mode in enumerate(
                ['default', 'search', 'text-area', 'password']
            )
        ],
        direction='vertical',
    )
"""
    }
]
