import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                '默认模式不同尺寸示例', innerTextOrientation='left'
            ),
            fac.AntdSelect(
                size='small',
                placeholder='size="small"',
                options=[f'选项{i}' for i in range(1, 6)],
                value='选项1',
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                size='middle',
                placeholder='size="middle"（默认）',
                options=[f'选项{i}' for i in range(1, 6)],
                value='选项1',
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                size='large',
                placeholder='size="large"',
                options=[f'选项{i}' for i in range(1, 6)],
                value='选项1',
                style={'width': '100%'},
            ),
            fac.AntdDivider(
                '多选模式不同尺寸示例', innerTextOrientation='left'
            ),
            fac.AntdSelect(
                size='small',
                mode='multiple',
                placeholder='size="small"',
                options=[f'选项{i}' for i in range(1, 6)],
                value=[f'选项{i}' for i in range(1, 3)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                size='middle',
                mode='multiple',
                placeholder='size="middle"（默认）',
                options=[f'选项{i}' for i in range(1, 6)],
                value=[f'选项{i}' for i in range(1, 3)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                size='large',
                mode='multiple',
                placeholder='size="large"',
                options=[f'选项{i}' for i in range(1, 6)],
                value=[f'选项{i}' for i in range(1, 3)],
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
            '默认模式不同尺寸示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            size='small',
            placeholder='size="small"',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='middle',
            placeholder='size="middle"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='large',
            placeholder='size="large"',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdDivider(
            '多选模式不同尺寸示例', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            size='small',
            mode='multiple',
            placeholder='size="small"',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='middle',
            mode='multiple',
            placeholder='size="middle"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            size='large',
            mode='multiple',
            placeholder='size="large"',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
