import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdCollapse 折叠面板'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCollapse 折叠面板', level=2),
        fac.AntdParagraph('可折叠展开的特殊容器。'),
    ]
