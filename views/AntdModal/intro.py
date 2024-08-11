import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': 'AntdModal 对话框'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdModal 对话框', level=2),
        fac.AntdParagraph('用于渲染弹出式对话框。'),
    ]
