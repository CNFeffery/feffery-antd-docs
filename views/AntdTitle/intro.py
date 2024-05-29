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
                {'title': 'AntdTitle 标题'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTitle 标题', level=2),
        fac.AntdParagraph('用于渲染具有丰富样式和功能的标题。'),
    ]
