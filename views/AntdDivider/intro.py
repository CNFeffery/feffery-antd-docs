import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '布局'},
                {'title': 'AntdDivider 分割线'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdDivider 分割线', level=2),
        fac.AntdParagraph('对控件或功能区进行水平或竖直方向上的分割。'),
    ]
