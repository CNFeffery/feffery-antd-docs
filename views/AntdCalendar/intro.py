import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': '排版相关'},
                {'title': 'AntdCalendar 日历'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCalendar 日历', level=2),
        fac.AntdParagraph('用于渲染可交互的日历。'),
    ]
