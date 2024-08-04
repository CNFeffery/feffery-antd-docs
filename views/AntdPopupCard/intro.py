import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': 'AntdPopupCard 弹出式卡片'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdPopupCard 弹出式卡片', level=2),
        fac.AntdParagraph('用于以弹出式卡片的形式展现内容。'),
    ]
