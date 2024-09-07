import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdBreadcrumb(
            items=[
                {
                    'title': 'awesome-feffery-dash仓库主页',
                    'href': 'https://github.com/CNFeffery/awesome-feffery-dash',
                    'target': '_blank',
                },
                {
                    'title': 'feffery-antd-components文档首页',
                    'href': '/',
                    'target': '_blank',
                },
                {
                    'title': 'AntdBreadcrumb文档页',
                    'href': '/AntdBreadcrumb',
                    'target': '_blank',
                },
            ]
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdBreadcrumb(
            items=[
                {
                    'title': 'awesome-feffery-dash',
                    'href': 'https://github.com/CNFeffery/awesome-feffery-dash',
                    'target': '_blank',
                },
                {
                    'title': 'feffery-antd-components',
                    'href': '/',
                    'target': '_blank',
                },
                {
                    'title': 'AntdBreadcrumb doc',
                    'href': '/AntdBreadcrumb',
                    'target': '_blank',
                },
            ]
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdBreadcrumb(
    items=[
        {
            'title': 'awesome-feffery-dash仓库主页',
            'href': 'https://github.com/CNFeffery/awesome-feffery-dash',
            'target': '_blank',
        },
        {
            'title': 'feffery-antd-components文档首页',
            'href': '/',
            'target': '_blank',
        },
        {
            'title': 'AntdBreadcrumb文档页',
            'href': '/AntdBreadcrumb',
            'target': '_blank',
        },
    ]
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdBreadcrumb(
    items=[
        {
            'title': 'awesome-feffery-dash',
            'href': 'https://github.com/CNFeffery/awesome-feffery-dash',
            'target': '_blank',
        },
        {
            'title': 'feffery-antd-components',
            'href': '/',
            'target': '_blank',
        },
        {
            'title': 'AntdBreadcrumb doc',
            'href': '/AntdBreadcrumb',
            'target': '_blank',
        },
    ]
)
"""
            }
        ]
