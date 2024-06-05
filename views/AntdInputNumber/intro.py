import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdInputNumber 数值输入框'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdInputNumber 数值输入框', level=2),
        fac.AntdParagraph('专门提供数值输入功能的输入框。'),
    ]
