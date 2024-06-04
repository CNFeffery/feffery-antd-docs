import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': '排版相关'},
                {'title': 'AntdMentions 提及'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdMentions 提及', level=2),
        fac.AntdParagraph('用于实现在输入内容中对不同角色进行提及的功能，常用于构建论坛、协同办公等平台中的评论功能。'),
    ]
