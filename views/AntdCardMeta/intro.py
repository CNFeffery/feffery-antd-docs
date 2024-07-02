import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': '卡片'},
                {'title': 'AntdCardMeta 结构化卡片'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCardMeta 结构化卡片', level=2),
        fac.AntdParagraph('用于为卡片添加结构化展示信息。'),
    ]
