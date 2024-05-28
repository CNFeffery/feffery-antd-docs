import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdFloatButton 悬浮按钮'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdFloatButton 悬浮按钮', level=2),
        fac.AntdParagraph('悬浮于页面固定位置的按钮'),
    ]
