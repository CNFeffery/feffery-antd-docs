import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '其他'},
                {'title': 'AntdAffix 固钉'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdAffix 固钉', level=2),
        fac.AntdParagraph(
            '确保内部元素原有位置在被用户滚动出视口后，仍然可以在视口范围内保持可见状态。'
        ),
    ]
