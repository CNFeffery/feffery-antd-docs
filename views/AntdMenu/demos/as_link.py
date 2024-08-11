import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


code_string = [
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
