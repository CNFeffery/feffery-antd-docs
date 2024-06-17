import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdCheckableTag 可选择标签'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCheckableTag 可选择标签', level=2),
        fac.AntdParagraph('可以点击切换选中状态的标签。'),
    ]
