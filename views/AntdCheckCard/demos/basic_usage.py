import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCheckCard(fac.AntdText('选择卡片示例' * 10)),
            fac.AntdCheckCard(
                fac.AntdStatistic(title='统计数值示例', value=1332971),
                defaultChecked=True,
            ),
            fac.AntdCheckCard(
                fac.AntdSpace(
                    [
                        fac.AntdAvatar(
                            mode='image',
                            size=48,
                            src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                        ),
                        fac.AntdText('选择卡片示例' * 10),
                    ],
                    align='start',
                )
            ),
        ],
        direction='vertical',
        size='small',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCheckCard(fac.AntdText('选择卡片示例' * 10)),
        fac.AntdCheckCard(
            fac.AntdStatistic(title='统计数值示例', value=1332971),
            defaultChecked=True,
        ),
        fac.AntdCheckCard(
            fac.AntdSpace(
                [
                    fac.AntdAvatar(
                        mode='image',
                        size=48,
                        src='/assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                    ),
                    fac.AntdText('选择卡片示例' * 10),
                ],
                align='start',
            )
        ),
    ],
    direction='vertical',
    size='small',
    style={'width': '100%'},
)
"""
    }
]
