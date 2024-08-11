import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '导航'},
                {'title': 'AntdDropdown 下拉菜单'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdDropdown 下拉菜单', level=2),
        fac.AntdParagraph('用于展示具有若干选项或链接的向下弹出的列表。'),
    ]
