import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSelect(
                placeholder='输入内容以搜索选项',
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
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
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
