import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdIcon 图标'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdIcon 图标', level=2),
        fac.AntdParagraph('用于提示不同的功能及场景。'),
    ]
