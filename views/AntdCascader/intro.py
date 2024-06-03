import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdCascader 级联选择'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCascader 级联选择', level=2),
        fac.AntdParagraph('用于为用户提供一组具有层级信息的选项进行选择。'),
    ]
