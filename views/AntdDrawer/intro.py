import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': 'AntdDrawer 抽屉'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdDrawer 抽屉', level=2),
        fac.AntdParagraph('从页面指定方位弹出可交互的额外容器。'),
    ]
