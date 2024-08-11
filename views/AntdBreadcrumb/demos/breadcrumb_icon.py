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
            'icon': 'antd-home'
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
