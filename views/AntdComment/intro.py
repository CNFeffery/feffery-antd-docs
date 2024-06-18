import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdComment 评论'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdComment 评论', level=2),
        fac.AntdParagraph('构建常用的用户评论相关功能。'),
    ]
