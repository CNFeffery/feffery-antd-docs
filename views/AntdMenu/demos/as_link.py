import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        # 构造演示用例相关内容
        demo_contents = fac.AntdMenu(
            menuItems=[
                {
                    'component': 'Item',
                    'props': {
                        'key': 'AntdMenu文档页',
                        'title': 'AntdMenu文档页',
                        'href': '/AntdMenu',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'fac仓库',
                        'title': 'fac仓库',
                        'href': 'https://github.com/CNFeffery/feffery-antd-components',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'fuc仓库',
                        'title': 'fuc仓库',
                        'href': 'https://github.com/CNFeffery/feffery-utils-components',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'fmc仓库',
                        'title': 'fmc仓库',
                        'href': 'https://github.com/CNFeffery/feffery-markdown-components',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'feffery博客园',
                        'title': 'feffery博客园',
                        'href': 'https://www.cnblogs.com/feffery/',
                    },
                },
            ],
            mode='inline',
            defaultSelectedKey='AntdMenu文档页',
            style={'width': 256},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdMenu(
            menuItems=[
                {
                    'component': 'Item',
                    'props': {
                        'key': 'AntdMenu doc page',
                        'title': 'AntdMenu doc page',
                        'href': '/AntdMenu',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'fac repository',
                        'title': 'fac repository',
                        'href': 'https://github.com/CNFeffery/feffery-antd-components',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'fuc repository',
                        'title': 'fuc repository',
                        'href': 'https://github.com/CNFeffery/feffery-utils-components',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'fmc repository',
                        'title': 'fmc repository',
                        'href': 'https://github.com/CNFeffery/feffery-markdown-components',
                    },
                },
                {
                    'component': 'Item',
                    'props': {
                        'key': 'feffery blog',
                        'title': 'feffery blog',
                        'href': 'https://www.cnblogs.com/feffery/',
                    },
                },
            ],
            mode='inline',
            defaultSelectedKey='AntdMenu doc page',
            style={'width': 256},
        )

    return demo_contents


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdMenu(
    menuItems=[
        {
            'component': 'Item',
            'props': {
                'key': 'AntdMenu文档页',
                'title': 'AntdMenu文档页',
                'href': '/AntdMenu',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'fac仓库',
                'title': 'fac仓库',
                'href': 'https://github.com/CNFeffery/feffery-antd-components',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'fuc仓库',
                'title': 'fuc仓库',
                'href': 'https://github.com/CNFeffery/feffery-utils-components',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'fmc仓库',
                'title': 'fmc仓库',
                'href': 'https://github.com/CNFeffery/feffery-markdown-components',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'feffery博客园',
                'title': 'feffery博客园',
                'href': 'https://www.cnblogs.com/feffery/',
            },
        },
    ],
    mode='inline',
    defaultSelectedKey='AntdMenu文档页',
    style={'width': 256},
)
"""
            }
        ]

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdMenu(
    menuItems=[
        {
            'component': 'Item',
            'props': {
                'key': 'AntdMenu doc page',
                'title': 'AntdMenu doc page',
                'href': '/AntdMenu',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'fac repository',
                'title': 'fac repository',
                'href': 'https://github.com/CNFeffery/feffery-antd-components',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'fuc repository',
                'title': 'fuc repository',
                'href': 'https://github.com/CNFeffery/feffery-utils-components',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'fmc repository',
                'title': 'fmc repository',
                'href': 'https://github.com/CNFeffery/feffery-markdown-components',
            },
        },
        {
            'component': 'Item',
            'props': {
                'key': 'feffery blog',
                'title': 'feffery blog',
                'href': 'https://www.cnblogs.com/feffery/',
            },
        },
    ],
    mode='inline',
    defaultSelectedKey='AntdMenu doc page',
    style={'width': 256},
)
"""
            }
        ]
