import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdTour 漫游式引导'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTour 漫游式引导', level=2),
        fac.AntdParagraph('用于分步引导用户了解产品功能的气泡组件。'),
    ]
