import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdTag 标签'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTag 标签', level=2),
        fac.AntdParagraph('用于渲染美观的小标签。'),
    ]
