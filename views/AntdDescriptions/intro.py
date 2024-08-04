import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': '描述列表'},
                {'title': 'AntdDescriptions 描述列表'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdDescriptions 描述列表', level=2),
        fac.AntdParagraph('用于配合AntdDescriptionItem进行一组属性的展示。'),
    ]
