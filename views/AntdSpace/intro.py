import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '布局'},
                {'title': 'AntdSpace 排列'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdSpace 排列', level=2),
        fac.AntdParagraph('用于快捷对一组元素进行水平或竖直方向上的规整排列。'),
    ]
