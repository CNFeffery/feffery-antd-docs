import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSegmented(
                options=[
                    {'value': i, 'icon': icon}
                    for i, icon in enumerate(
                        [
                            'antd-carry-out',
                            'antd-branches',
                            'antd-team',
                            'antd-send',
                            'antd-setting',
                        ]
                    )
                ],
                defaultValue=0,
            ),
            fac.AntdSegmented(
                options=[
                    {'value': i, 'icon': icon}
                    for i, icon in enumerate(
                        [
                            'antd-carry-out',
                            'antd-branches',
                            'antd-team',
                            'antd-send',
                            'antd-setting',
                        ]
                    )
                ],
                defaultValue=0,
                vertical=True,
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSegmented(
            options=[
                {'value': i, 'icon': icon}
                for i, icon in enumerate(
                    [
                        'antd-carry-out',
                        'antd-branches',
                        'antd-team',
                        'antd-send',
                        'antd-setting',
                    ]
                )
            ],
            defaultValue=0,
        ),
        fac.AntdSegmented(
            options=[
                {'value': i, 'icon': icon}
                for i, icon in enumerate(
                    [
                        'antd-carry-out',
                        'antd-branches',
                        'antd-team',
                        'antd-send',
                        'antd-setting',
                    ]
                )
            ],
            defaultValue=0,
            vertical=True,
        ),
    ],
    direction='vertical',
)
"""
    }
]
