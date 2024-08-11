import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdPopover 气泡卡片'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdPopover 气泡卡片', level=2),
        fac.AntdParagraph('用于为指定元素添加额外说明信息。'),
    ]
