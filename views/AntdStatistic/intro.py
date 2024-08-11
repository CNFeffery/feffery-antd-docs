import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdStatistic 统计数值'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdStatistic 统计数值', level=2),
        fac.AntdParagraph('用于构建漂亮的统计数值展示。'),
    ]
