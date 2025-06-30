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
                    fac.AntdSelect(
                        id=f'select-{mode}-mode-demo',
                        placeholder=f'mode="{mode}"' if mode else '基础模式',
                        options=[f'选项{i}' for i in range(1, 6)],
                        mode=mode,
                        style={'width': '100%'},
                    )
                    for mode in [None, 'multiple', 'tags']
                ],
                direction='vertical',
                style={'width': '100%'},
            ),
            fac.AntdCard(
                id='select-demo-output',
                styles={'header': {'display': 'none'}},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


@app.callback(
    Output('select-demo-output', 'children'),
    [
        Input(f'select-{mode}-mode-demo', 'value')
        for mode in [None, 'multiple', 'tags']
    ],
)
def select_mode_demo(*value_list):
    return fac.AntdSpace(
        [
            fac.AntdText(
                f'{mode if mode else "基础"}模式value：{value_list[i]}'
            )
            for i, mode in enumerate([None, 'multiple', 'tags'])
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
                fac.AntdSelect(
                    id=f'select-{mode}-mode-demo',
                    placeholder=f'mode="{mode}"' if mode else '基础模式',
                    options=[f'选项{i}' for i in range(1, 6)],
                    mode=mode,
                    style={'width': '100%'},
                )
                for mode in [None, 'multiple', 'tags']
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
        fac.AntdCard(
            id='select-demo-output',
            styles={'header': {'display': 'none'}},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)


@app.callback(
    Output('select-demo-output', 'children'),
    [
        Input(f'select-{mode}-mode-demo', 'value')
        for mode in [None, 'multiple', 'tags']
    ],
)
def select_mode_demo(*value_list):
    return fac.AntdSpace(
        [
            fac.AntdText(
                f'{mode if mode else "基础"}模式value：{value_list[i]}'
            )
            for i, mode in enumerate([None, 'multiple', 'tags'])
        ],
        direction='vertical',
    )
"""
    }
]
