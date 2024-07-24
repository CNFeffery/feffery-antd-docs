import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': 'AntdPopconfirm 气泡确认框'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdPopconfirm 气泡确认框', level=2),
        fac.AntdParagraph('用于实现二次确认功能，相较于对话框更加简便。'),
    ]
