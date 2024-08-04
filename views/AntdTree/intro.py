import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdTree 树形控件'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTree 树形控件', level=2),
        fac.AntdParagraph('用于渲染展示树形数据结构，并支持丰富的交互功能。'),
    ]
