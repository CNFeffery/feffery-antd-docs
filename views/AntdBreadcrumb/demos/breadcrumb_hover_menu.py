import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdBreadcrumb(
        items=[
            {
                'title': 'feffery-components仓库主页',
                'href': 'https://github.com/CNFeffery/feffery-dash-components',
                'target': '_blank',
                'icon': 'antd-github',
            },
            {
                'title': 'feffery-antd-components文档首页',
                'href': '/',
                'target': '_blank',
                'icon': 'antd-home',
                'menuItems': [
                    {
                        'title': 'feffery-utils-components',
                        'href': 'https://github.com/CNFeffery/feffery-utils-components',
                        'target': '_blank',
                    },
                    {
                        'title': 'feffery-antd-charts',
                        'href': 'https://github.com/CNFeffery/feffery-antd-charts',
                        'target': '_blank',
                    },
                    {
                        'title': 'feffery-markdown-components',
                        'href': 'https://github.com/CNFeffery/feffery-markdown-components',
                        'target': '_blank',
                    },
                ],
            },
            {
                'title': 'AntdBreadcrumb文档页',
                'href': '/AntdBreadcrumb',
                'target': '_blank',
                'icon': 'fc-approval',
            },
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdBreadcrumb(
    items=[
        {
            'title': 'feffery-components仓库主页',
            'href': 'https://github.com/CNFeffery/feffery-dash-components',
            'target': '_blank',
            'icon': 'antd-github'
        },
        {
            'title': 'feffery-antd-components文档首页',
            'href': '/',
            'target': '_blank',
            'icon': 'antd-home',
            'menuItems': [
                {
                    'title': 'feffery-utils-components',
                    'href': 'https://github.com/CNFeffery/feffery-utils-components',
                    'target': '_blank'
                },
                {
                    'title': 'feffery-antd-charts',
                    'href': 'https://github.com/CNFeffery/feffery-antd-charts',
                    'target': '_blank'
                },
                {
                    'title': 'feffery-markdown-components',
                    'href': 'https://github.com/CNFeffery/feffery-markdown-components',
                    'target': '_blank'
                }
            ]
        },
        {
            'title': 'AntdBreadcrumb文档页',
            'href': '/AntdBreadcrumb',
            'target': '_blank',
            'icon': 'fc-approval'
        }
    ]
)
"""
    }
]
