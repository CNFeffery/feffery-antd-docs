import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdTooltip 信息提示'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTooltip 信息提示', level=2),
        fac.AntdParagraph('用于为指定元素添加额外信息提示。'),
    ]
