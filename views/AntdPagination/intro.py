import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': '排版相关'},
                {'title': 'AntdPagination 分页'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdPagination 分页', level=2),
        fac.AntdParagraph('采用分页的形式分隔长列表，每次只加载单页内容。'),
    ]
