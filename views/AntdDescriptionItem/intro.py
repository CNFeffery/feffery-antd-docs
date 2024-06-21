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
                {'title': 'AntdDescriptionItem 描述列表子项'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdDescriptionItem 描述列表子项', level=2),
        fac.AntdParagraph('在描述列表中构建单个描述列表子项。'),
    ]
