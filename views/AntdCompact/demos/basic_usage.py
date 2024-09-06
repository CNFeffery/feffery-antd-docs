import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdDivider('基于AntdSpace', innerTextOrientation='left'),
            fac.AntdSpace(
                [fac.AntdButton(f'按钮{i}') for i in range(1, 6)], size=0
            ),
            fac.AntdDivider('基于AntdCompact', innerTextOrientation='left'),
            fac.AntdCompact([fac.AntdButton(f'按钮{i}') for i in range(1, 6)]),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDivider('Base on AntdSpace', innerTextOrientation='left'),
            fac.AntdSpace(
                [fac.AntdButton(f'button{i}') for i in range(1, 6)], size=0
            ),
            fac.AntdDivider('Base on AntdCompact', innerTextOrientation='left'),
            fac.AntdCompact(
                [fac.AntdButton(f'button{i}') for i in range(1, 6)]
            ),
        ]

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdDivider('基于AntdSpace', innerTextOrientation='left'),
    fac.AntdSpace(
        [fac.AntdButton(f'按钮{i}') for i in range(1, 6)], size=0
    ),
    fac.AntdDivider('基于AntdCompact', innerTextOrientation='left'),
    fac.AntdCompact([fac.AntdButton(f'按钮{i}') for i in range(1, 6)]),
]
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdDivider('Base on AntdSpace', innerTextOrientation='left'),
    fac.AntdSpace(
        [fac.AntdButton(f'button{i}') for i in range(1, 6)], size=0
    ),
    fac.AntdDivider('Base on AntdCompact', innerTextOrientation='left'),
    fac.AntdCompact(
        [fac.AntdButton(f'button{i}') for i in range(1, 6)]
    ),
]
"""
            }
        ]
