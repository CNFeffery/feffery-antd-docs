import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = [
            fac.AntdDivider("align='start'"),
            fac.AntdPagination(defaultPageSize=10, total=100, align='start'),
            fac.AntdDivider("align='center'"),
            fac.AntdPagination(defaultPageSize=10, total=100, align='center'),
            fac.AntdDivider("align='end'"),
            fac.AntdPagination(defaultPageSize=10, total=100, align='end'),
        ]

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = [
            fac.AntdDivider("align='start'"),
            fac.AntdPagination(
                defaultPageSize=10, total=100, align='start', locale='en-us'
            ),
            fac.AntdDivider("align='center'"),
            fac.AntdPagination(
                defaultPageSize=10, total=100, align='center', locale='en-us'
            ),
            fac.AntdDivider("align='end'"),
            fac.AntdPagination(
                defaultPageSize=10, total=100, align='end', locale='en-us'
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
    fac.AntdDivider("align='start'"),
    fac.AntdPagination(defaultPageSize=10, total=100, align='start'),
    fac.AntdDivider("align='center'"),
    fac.AntdPagination(defaultPageSize=10, total=100, align='center'),
    fac.AntdDivider("align='end'"),
    fac.AntdPagination(defaultPageSize=10, total=100, align='end'),
]
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
[
    fac.AntdDivider("align='start'"),
    fac.AntdPagination(
        defaultPageSize=10, total=100, align='start', locale='en-us'
    ),
    fac.AntdDivider("align='center'"),
    fac.AntdPagination(
        defaultPageSize=10, total=100, align='center', locale='en-us'
    ),
    fac.AntdDivider("align='end'"),
    fac.AntdPagination(
        defaultPageSize=10, total=100, align='end', locale='en-us'
    ),
]
"""
            }
        ]
