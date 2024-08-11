import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                'autoClearSearchValue=True', innerTextOrientation='left'
            ),
            fac.AntdSelect(
                placeholder='输入内容以搜索选项',
                mode='multiple',
                autoClearSearchValue=True,
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                placeholder='输入内容以搜索选项',
                mode='tags',
                autoClearSearchValue=True,
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdDivider(
                'autoClearSearchValue=False', innerTextOrientation='left'
            ),
            fac.AntdSelect(
                placeholder='输入内容以搜索选项',
                mode='multiple',
                autoClearSearchValue=False,
                options=[f'选项{i}' for i in range(1, 6)],
                style={'width': '100%'},
            ),
            fac.AntdSelect(
                placeholder='输入内容以搜索选项',
                mode='tags',
                autoClearSearchValue=False,
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
            'autoClearSearchValue=True', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='multiple',
            autoClearSearchValue=True,
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='tags',
            autoClearSearchValue=True,
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdDivider(
            'autoClearSearchValue=False', innerTextOrientation='left'
        ),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='multiple',
            autoClearSearchValue=False,
            options=[f'选项{i}' for i in range(1, 6)],
            style={'width': '100%'},
        ),
        fac.AntdSelect(
            placeholder='输入内容以搜索选项',
            mode='tags',
            autoClearSearchValue=False,
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
