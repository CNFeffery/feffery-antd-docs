import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdFlex(
                [
                    fac.AntdTitle('计算任务xxx', level=4),
                    fac.AntdText(
                        '这是计算任务xxx的描述信息balabalabala',
                        type='secondary',
                    ),
                ],
                vertical=True,
            ),
            fac.AntdSteps(
                steps=[
                    {
                        'title': f'步骤{i + 1}',
                        'description': f'这是步骤{i + 1}的描述',
                    }
                    for i in range(3)
                ],
                type='inline',
                style={'height': 50},
            ),
        ],
        justify='space-between',
        align='flex-end',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdFlex(
            [
                fac.AntdTitle('计算任务xxx', level=4),
                fac.AntdText(
                    '这是计算任务xxx的描述信息balabalabala',
                    type='secondary',
                ),
            ],
            vertical=True,
        ),
        fac.AntdSteps(
            steps=[
                {
                    'title': f'步骤{i + 1}',
                    'description': f'这是步骤{i + 1}的描述',
                }
                for i in range(3)
            ],
            type='inline',
            style={'height': 50},
        ),
    ],
    justify='space-between',
    align='flex-end',
)
"""
    }
]
