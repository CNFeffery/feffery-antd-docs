import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '其他'},
                {'title': 'Fragment 空节点'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('Fragment 空节点', level=2),
        fac.AntdParagraph('承载内部元素且本身不渲染占用DOM节点。'),
    ]
