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
                {'title': 'AntdSkeletonImage 图片占位图'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdSkeletonImage 图片占位图', level=2),
        fac.AntdParagraph('用于在自定义骨架屏中构建图片占位相关内容。'),
    ]