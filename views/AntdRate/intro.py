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
                {'title': 'AntdRate 评分'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdRate 评分', level=2),
        fac.AntdParagraph('用于为用户提供美观的星级打分功能。'),
    ]
