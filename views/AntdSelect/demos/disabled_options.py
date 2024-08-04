import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('常规用法', innerTextOrientation='left'),
            fac.AntdSelect(
                options=[
                    {
                        'label': f'选项{i}',
                        'value': f'选项{i}',
                        'disabled': True if i == 3 else False,
                    }
                    for i in range(1, 6)
                ],
                style={'width': '100%'},
            ),
            fac.AntdDivider('自定义label用法', innerTextOrientation='left'),
            fac.AntdSelect(
                options=[
                    {
                        'label': fac.AntdFlex(
                            [
                                fac.AntdFlex(
                                    [
                                        fac.AntdAvatar(
                                            text=f'{i}',
                                            mode='text',
                                            size='small',
                                        ),
                                        fac.AntdTag(
                                            content=f'选项{i}',
                                            color=[
                                                'blue',
                                                'green',
                                                'purple',
                                                'orange',
                                                'cyan',
                                            ][i - 1],
                                        ),
                                    ],
                                    justify='flex-start',
                                    align='center',
                                    gap=5,
                                ),
                                # 可通过额外的元素来展示disabled的视觉效果
                                fac.AntdIcon(
                                    icon='antd-stop',
                                    style={
                                        'color': 'gray',
                                    },
                                )
                                if i == 3
                                else None,
                            ],
                            justify='space-between',
                            align='center',
                            gap=5,
                        ),
                        'value': f'选项{i}',
                        'disabled': True if i == 3 else False,
                    }
                    for i in range(1, 6)
                ],
                size='large',
                style={'width': 350},
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
        fac.AntdDivider('常规用法', innerTextOrientation='left'),
        fac.AntdSelect(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}',
                    'disabled': True if i == 3 else False,
                }
                for i in range(1, 6)
            ],
            style={'width': '100%'},
        ),
        fac.AntdDivider('自定义label用法', innerTextOrientation='left'),
        fac.AntdSelect(
            options=[
                {
                    'label': fac.AntdFlex(
                        [
                            fac.AntdFlex(
                                [
                                    fac.AntdAvatar(
                                        text=f'{i}',
                                        mode='text',
                                        size='small',
                                    ),
                                    fac.AntdTag(
                                        content=f'选项{i}',
                                        color=[
                                            'blue',
                                            'green',
                                            'purple',
                                            'orange',
                                            'cyan',
                                        ][i - 1],
                                    ),
                                ],
                                justify='flex-start',
                                align='center',
                                gap=5,
                            ),
                            # 可通过额外的元素来展示disabled的视觉效果
                            fac.AntdIcon(
                                icon='antd-stop',
                                style={
                                    'color': 'gray',
                                },
                            )
                            if i == 3
                            else None,
                        ],
                        justify='space-between',
                        align='center',
                        gap=5,
                    ),
                    'value': f'选项{i}',
                    'disabled': True if i == 3 else False,
                }
                for i in range(1, 6)
            ],
            size='large',
            style={'width': 350},
        ),
    ],
    direction='vertical',
    style={'width': 350},
)
"""
    }
]
