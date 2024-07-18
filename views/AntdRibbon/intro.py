import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdRibbon 缎带'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdRibbon 缎带', level=2),
        fac.AntdParagraph('用于为容器类元素添加点缀作用的缎带。'),
    ]
