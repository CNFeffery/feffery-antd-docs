import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdAvatar 头像'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdAvatar 头像', level=2),
        fac.AntdParagraph('用于渲染图标、文字或图片形式的头像。'),
    ]
