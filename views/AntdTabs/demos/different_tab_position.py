import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTabs(
                items=[
                    {
                        'key': f'标签页{i}',
                        'label': f'标签页{i}',
                        'children': fac.AntdCenter(
                            f'这是标签页{i}的内容示例',
                            style={
                                'fontSize': 18,
                                'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                                'height': 260,
                            },
                        ),
                    }
                    for i in range(1, 6)
                ],
                tabPosition=position,
            )
            for position in ['top', 'left', 'bottom', 'right']
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
        fac.AntdTabs(
            items=[
                {
                    'key': f'标签页{i}',
                    'label': f'标签页{i}',
                    'children': fac.AntdCenter(
                        f'这是标签页{i}的内容示例',
                        style={
                            'fontSize': 18,
                            'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                            'height': 260,
                        },
                    ),
                }
                for i in range(1, 6)
            ],
            tabPosition=position,
        )
        for position in ['top', 'left', 'bottom', 'right']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
