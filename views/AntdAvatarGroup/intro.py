import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdAvatarGroup 头像组'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdAvatarGroup 头像组', level=2),
        fac.AntdParagraph('用于妥善展示一组头像。'),
    ]
