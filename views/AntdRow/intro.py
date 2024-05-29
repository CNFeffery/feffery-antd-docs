import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '布局'},
                {'title': '网格系统'},
                {'title': 'AntdRow 行'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdRow 行', level=2),
        fac.AntdParagraph('在网格系统中构建单个行元素。'),
    ]
