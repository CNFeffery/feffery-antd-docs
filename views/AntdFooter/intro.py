import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '布局'},
                {'title': '经典布局'},
                {'title': 'AntdFooter 页尾'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdFooter 页尾', level=2),
        fac.AntdParagraph('用于在经典布局方案中构建页尾部分。'),
    ]