import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('status="warning"', innerTextOrientation='left'),
            fac.AntdSelect(
                options=[f'选项{i}' for i in range(1, 6)],
                status='warning',
                value='选项1',
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                mode='multiple',
                options=[f'选项{i}' for i in range(1, 6)],
                status='warning',
                value=[f'选项{i}' for i in range(1, 3)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                mode='tags',
                options=[f'选项{i}' for i in range(1, 6)],
                status='warning',
                value=['选项1', '自由新增选项'],
                style={'width': '100%'},
            ),
            fac.AntdDivider('status="error"', innerTextOrientation='left'),
            fac.AntdSelect(
                options=[f'选项{i}' for i in range(1, 6)],
                status='error',
                value='选项1',
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                mode='multiple',
                options=[f'选项{i}' for i in range(1, 6)],
                status='error',
                value=[f'选项{i}' for i in range(1, 3)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                mode='tags',
                options=[f'选项{i}' for i in range(1, 6)],
                status='error',
                value=['选项1', '自由新增选项'],
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
        fac.AntdDivider('status="warning"', innerTextOrientation='left'),
        fac.AntdSelect(
            options=[f'选项{i}' for i in range(1, 6)],
            status='warning',
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            mode='multiple',
            options=[f'选项{i}' for i in range(1, 6)],
            status='warning',
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            mode='tags',
            options=[f'选项{i}' for i in range(1, 6)],
            status='warning',
            value=['选项1', '自由新增选项'],
            style={'width': '100%'},
        ),
        fac.AntdDivider('status="error"', innerTextOrientation='left'),
        fac.AntdSelect(
            options=[f'选项{i}' for i in range(1, 6)],
            status='error',
            value='选项1',
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            mode='multiple',
            options=[f'选项{i}' for i in range(1, 6)],
            status='error',
            value=[f'选项{i}' for i in range(1, 3)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            mode='tags',
            options=[f'选项{i}' for i in range(1, 6)],
            status='error',
            value=['选项1', '自由新增选项'],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
