import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdFloatButtonGroup 悬浮按钮组'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdFloatButtonGroup 悬浮按钮组', level=2),
        fac.AntdParagraph('用于承载一组悬浮按钮。'),
    ]
