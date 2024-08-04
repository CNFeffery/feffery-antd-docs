import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCompact(
                [
                    fac.AntdInput(placeholder='请输入', style={'width': 150}),
                    fac.AntdSelect(
                        options=[
                            {
                                'label': f'选项{i}',
                                'value': f'选项{i}',
                            }
                            for i in range(1, 4)
                        ],
                        defaultValue='选项1',
                        style={'width': 80},
                    ),
                ]
            ),
            fac.AntdCompact(
                [
                    fac.AntdInput(
                        placeholder='请输入', style={'width': '100%'}
                    ),
                    fac.AntdSelect(
                        options=[
                            {
                                'label': f'选项{i}',
                                'value': f'选项{i}',
                            }
                            for i in range(1, 4)
                        ],
                        defaultValue='选项1',
                        style={'width': 80},
                    ),
                ],
                style={'width': '100%'},
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCompact(
            [
                fac.AntdInput(placeholder='请输入', style={'width': 150}),
                fac.AntdSelect(
                    options=[
                        {
                            'label': f'选项{i}',
                            'value': f'选项{i}',
                        }
                        for i in range(1, 4)
                    ],
                    defaultValue='选项1',
                    style={'width': 80},
                ),
            ]
        ),
        fac.AntdCompact(
            [
                fac.AntdInput(
                    placeholder='请输入', style={'width': '100%'}
                ),
                fac.AntdSelect(
                    options=[
                        {
                            'label': f'选项{i}',
                            'value': f'选项{i}',
                        }
                        for i in range(1, 4)
                    ],
                    defaultValue='选项1',
                    style={'width': 80},
                ),
            ],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
