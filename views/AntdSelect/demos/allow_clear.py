import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                'allowClear=True（默认值）', innerTextOrientation='left'
            ),
            fac.AntdSelect(
                placeholder='mode="default"（默认）',
                options=[f'选项{i}' for i in range(1, 6)],
                value='选项1',
                allowClear=True,
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                placeholder='mode="multiple"',
                mode='multiple',
                options=[f'选项{i}' for i in range(1, 6)],
                value=[f'选项{i}' for i in range(1, 3)],
                allowClear=True,
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                placeholder='mode="tags"',
                mode='tags',
                options=[f'选项{i}' for i in range(1, 6)],
                value=['选项1', '自由新增选项'],
                allowClear=True,
                style={'width': '100%'},
            ),
            fac.AntdDivider('allowClear=False', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='mode="default"（默认）',
                options=[f'选项{i}' for i in range(1, 6)],
                value='选项1',
                allowClear=False,
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                placeholder='mode="multiple"',
                mode='multiple',
                options=[f'选项{i}' for i in range(1, 6)],
                value=[f'选项{i}' for i in range(1, 3)],
                allowClear=False,
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                placeholder='mode="tags"',
                mode='tags',
                options=[f'选项{i}' for i in range(1, 6)],
                value=['选项1', '自由新增选项'],
                allowClear=False,
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
            'allowClear=True（默认值）', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            placeholder='mode="default"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            allowClear=True,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="multiple"',
            mode='multiple',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            allowClear=True,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="tags"',
            mode='tags',
            options=[f'选项{i}' for i in range(1, 6)],
            value=['选项1', '自由新增选项'],
            allowClear=True,
            style={'width': '100%'},
        ),
        fac.AntdDivider('allowClear=False', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='mode="default"（默认）',
            options=[f'选项{i}' for i in range(1, 6)],
            value='选项1',
            allowClear=False,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="multiple"',
            mode='multiple',
            options=[f'选项{i}' for i in range(1, 6)],
            value=[f'选项{i}' for i in range(1, 3)],
            allowClear=False,
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='mode="tags"',
            mode='tags',
            options=[f'选项{i}' for i in range(1, 6)],
            value=['选项1', '自由新增选项'],
            allowClear=False,
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
