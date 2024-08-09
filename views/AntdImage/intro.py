import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdImage 图片'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdImage 图片', level=2),
        fac.AntdParagraph('用于展示单张或一组图片。'),
    ]
