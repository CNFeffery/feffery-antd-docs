import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': '骨架屏'},
                {'title': 'AntdCustomSkeleton 自定义骨架屏'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCustomSkeleton 自定义骨架屏', level=2),
        fac.AntdParagraph('用于自由设计骨架屏加载中内容。'),
    ]
