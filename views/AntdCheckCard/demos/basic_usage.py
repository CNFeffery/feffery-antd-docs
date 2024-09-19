import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdCheckCard(fac.AntdText('Demo' * 20)),
                fac.AntdCheckCard(
                    fac.AntdStatistic(title='Statistic Demo', value=1332971),
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
                            fac.AntdText('Demo' * 20),
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdCheckCard(fac.AntdText('Demo' * 20)),
        fac.AntdCheckCard(
            fac.AntdStatistic(title='Statistic Demo', value=1332971),
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
                    fac.AntdText('Demo' * 20),
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
