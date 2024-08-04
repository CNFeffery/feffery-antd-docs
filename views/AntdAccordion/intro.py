import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdAccordion 手风琴'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdAccordion 手风琴', level=2),
        fac.AntdParagraph('展示一组同级内容的特殊形式。'),
    ]
