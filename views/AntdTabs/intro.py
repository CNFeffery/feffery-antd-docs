import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': '标签页 AntdTabs'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('标签页 AntdTabs', level=2),
        fac.AntdParagraph('用于构建多标签页。'),
    ]
