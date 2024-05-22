import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdButton 按钮'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdButton 按钮', level=2),
        fac.AntdParagraph('按钮用于触发一个即时操作'),
    ]
