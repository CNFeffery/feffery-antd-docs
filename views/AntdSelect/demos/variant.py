import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                '默认模式不同变体示例', innerTextOrientation='left'
            ),
            fac.AntdSelect(
                variant='outlined',
                placeholder='variant="outlined"（默认）',
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                variant='filled',
                placeholder='variant="filled"',
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                variant='borderless',
                placeholder='variant="borderless"',
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdDivider(
                '多选模式不同变体示例', innerTextOrientation='left'
            ),
            fac.AntdSelect(
                variant='outlined',
                mode='multiple',
                placeholder='variant="outlined"（默认）',
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                variant='filled',
                mode='multiple',
                placeholder='variant="filled"',
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                variant='borderless',
                mode='multiple',
                placeholder='variant="borderless"',
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
        ],
        direction='vertical',
        style={'width': 350},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider(
            '默认模式不同变体示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            variant='outlined',
            placeholder='variant="outlined"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='filled',
            placeholder='variant="filled"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='borderless',
            placeholder='variant="borderless"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdDivider(
            '多选模式不同变体示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            variant='outlined',
            mode='multiple',
            placeholder='variant="outlined"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='filled',
            mode='multiple',
            placeholder='variant="filled"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            variant='borderless',
            mode='multiple',
            placeholder='variant="borderless"',
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
