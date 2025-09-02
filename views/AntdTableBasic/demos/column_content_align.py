import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdTable(
            columns=[
                {'title': align, 'dataIndex': align, 'align': align}
                for align in ['left', 'center', 'right']
            ],
            data=[{align: 999 for align in ['left', 'center', 'right']}] * 3,
            bordered=True,
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdTable(
            columns=[
                {'title': align, 'dataIndex': align, 'align': align}
                for align in ['left', 'center', 'right']
            ],
            data=[{align: 999 for align in ['left', 'center', 'right']}] * 3,
            bordered=True,
            locale='en-us',
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {'title': align, 'dataIndex': align, 'align': align}
        for align in ['left', 'center', 'right']
    ],
    data=[{align: 999 for align in ['left', 'center', 'right']}] * 3,
    bordered=True,
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdTable(
    columns=[
        {'title': align, 'dataIndex': align, 'align': align}
        for align in ['left', 'center', 'right']
    ],
    data=[{align: 999 for align in ['left', 'center', 'right']}] * 3,
    bordered=True,
)
"""
            }
        ]
