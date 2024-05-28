import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdCenter 居中'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCenter 居中', level=2),
        fac.AntdParagraph('快捷实现内容在水平垂直方向上居中。'),
    ]
