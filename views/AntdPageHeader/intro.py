import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '导航'},
                {'title': 'AntdPageHeader 页头'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdPageHeader 页头', level=2),
        fac.AntdParagraph('页头位于页容器顶部，起到内容概览和引导页级操作的作用。'),
    ]
