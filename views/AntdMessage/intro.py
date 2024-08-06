import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': 'AntdMessage 全局提示'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdMessage 全局提示', level=2),
        fac.AntdParagraph('用于全局展示操作反馈信息。'),
    ]
