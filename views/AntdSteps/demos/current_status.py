import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSteps(
                steps=[
                    {
                        'title': f'步骤{i + 1}的title',
                        'subTitle': f'步骤{i + 1}的subTitle',
                        'description': f'步骤{i + 1}的description',
                    }
                    for i in range(3)
                ],
                current=2,
                status=status,
            )
            for status in ['process', 'wait', 'finish', 'error']
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
        fac.AntdSteps(
            steps=[
                {
                    'title': f'步骤{i + 1}的title',
                    'subTitle': f'步骤{i + 1}的subTitle',
                    'description': f'步骤{i + 1}的description',
                }
                for i in range(3)
            ],
            current=2,
            status=status,
        )
        for status in ['process', 'wait', 'finish', 'error']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
