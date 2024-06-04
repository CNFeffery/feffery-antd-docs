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
                {'title': 'AntdRadioGroup 单选框'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdRadioGroup 单选框', level=2),
        fac.AntdParagraph('用于供用户在一组选项中进行唯一项选择。'),
    ]
