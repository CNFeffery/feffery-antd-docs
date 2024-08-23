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
                fac.AntdText(
                    '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100, ellipsis=True
                ),
                fac.AntdText(
                    '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100,
                    ellipsis={'suffix': '👉'},
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdText(
                    'Content ellipsis example ' + 'bala' * 100,
                    ellipsis=True,
                ),
                fac.AntdText(
                    'Content ellipsis example ' + 'bala' * 100,
                    ellipsis={'suffix': '👉'},
                ),
            ],
            direction='vertical',
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
        fac.AntdText(
            '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100, ellipsis=True
        ),
        fac.AntdText(
            '内容省略示例' + '巴拉巴拉巴拉巴拉' * 100,
            ellipsis={'suffix': '👉'},
        ),
    ],
    direction='vertical',
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
        fac.AntdText(
            'Content ellipsis example ' + 'bala' * 100,
            ellipsis=True,
        ),
        fac.AntdText(
            'Content ellipsis example ' + 'bala' * 100,
            ellipsis={'suffix': '👉'},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
