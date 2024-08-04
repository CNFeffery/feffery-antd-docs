import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '导航'},
                {'title': 'AntdMenu 导航菜单'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdMenu 导航菜单', level=2),
        fac.AntdParagraph(
            '导航菜单用于引导用户在不同层级的页面之间进行跳转，一般分为顶部导航和侧边导航，顶部导航提供全局性的类目和功能，侧边导航提供多级结构来收纳和排列网站架构。'
        ),
    ]
