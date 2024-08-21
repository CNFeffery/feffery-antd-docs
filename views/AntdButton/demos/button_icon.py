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
                fac.AntdButton(
                    'fac文档首页', icon=fac.AntdIcon(icon='antd-search')
                ),
                fac.AntdButton(
                    'fac文档首页',
                    icon=fac.AntdIcon(icon='antd-search'),
                    iconPosition='end',
                ),
            ],
            wrap=True,
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdButton(
                    'fac documentation', icon=fac.AntdIcon(icon='antd-search')
                ),
                fac.AntdButton(
                    'fac documentation',
                    icon=fac.AntdIcon(icon='antd-search'),
                    iconPosition='end',
                ),
            ],
            wrap=True,
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
        fac.AntdButton(
            'fac文档首页', icon=fac.AntdIcon(icon='antd-search')
        ),
        fac.AntdButton(
            'fac文档首页',
            icon=fac.AntdIcon(icon='antd-search'),
            iconPosition='end',
        ),
    ],
    wrap=True
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
        fac.AntdButton(
            'fac documentation', icon=fac.AntdIcon(icon='antd-search')
        ),
        fac.AntdButton(
            'fac documentation',
            icon=fac.AntdIcon(icon='antd-search'),
            iconPosition='end',
        ),
    ],
    wrap=True,
)
"""
            }
        ]
