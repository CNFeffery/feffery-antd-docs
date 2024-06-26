import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdEmpty 空状态'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdEmpty 空状态', level=2),
        fac.AntdParagraph('用于在信息缺失时起到占位说明的作用。'),
    ]
