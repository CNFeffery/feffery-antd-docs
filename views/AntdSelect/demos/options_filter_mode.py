import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('尝试搜索大小写字母', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='case-insensitive',
                optionFilterMode='case-insensitive',
                options=[
                    f'选项{i}-{index}'
                    for index, i in enumerate(
                        ['A', 'a', 'B', 'b', 'c', 'D', 'e']
                    )
                ],
                style={'width': '100%'},
            ),
            fac.AntdDivider('尝试搜索大小写字母', innerTextOrientation='left'),
            fac.AntdSelect(
                placeholder='case-sensitive',
                optionFilterMode='case-sensitive',
                options=[
                    f'选项{i}-{index}'
                    for index, i in enumerate(
                        ['A', 'a', 'B', 'b', 'c', 'D', 'e']
                    )
                ],
                style={'width': '100%'},
            ),
            fac.AntdDivider(
                '尝试搜索[a-z]、[a-z]|[A-Z]、[0-9]等',
                innerTextOrientation='left',
            ),
            fac.AntdSelect(
                placeholder='regex',
                optionFilterMode='regex',
                options=[
                    f'选项{i}-{index}'
                    for index, i in enumerate(
                        ['A', 'a', 'B', 'b', 'c', 'D', 'e']
                    )
                ],
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
        fac.AntdDivider('尝试搜索大小写字母', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='case-insensitive',
            optionFilterMode='case-insensitive',
            options=[
                f'选项{i}-{index}'
                for index, i in enumerate(
                    ['A', 'a', 'B', 'b', 'c', 'D', 'e']
                )
            ],
            style={'width': '100%'},
        ),
        fac.AntdDivider('尝试搜索大小写字母', innerTextOrientation='left'),
        fac.AntdSelect(
            placeholder='case-sensitive',
            optionFilterMode='case-sensitive',
            options=[
                f'选项{i}-{index}'
                for index, i in enumerate(
                    ['A', 'a', 'B', 'b', 'c', 'D', 'e']
                )
            ],
            style={'width': '100%'},
        ),
        fac.AntdDivider(
            '尝试搜索[a-z]、[a-z]|[A-Z]、[0-9]等',
            innerTextOrientation='left',
        ),
        fac.AntdSelect(
            placeholder='regex',
            optionFilterMode='regex',
            options=[
                f'选项{i}-{index}'
                for index, i in enumerate(
                    ['A', 'a', 'B', 'b', 'c', 'D', 'e']
                )
            ],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
