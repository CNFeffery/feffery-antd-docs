import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdImageGroup 图片组'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdImageGroup 图片组', level=2),
        fac.AntdParagraph('用于灵活整合一系列图片。'),
    ]
