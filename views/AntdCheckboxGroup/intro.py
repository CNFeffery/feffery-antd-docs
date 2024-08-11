import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdCheckboxGroup 组合选择框'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCheckboxGroup 组合选择框', level=2),
        fac.AntdParagraph('由若干选择框组成，用于在一组可选项中进行多项选择。'),
    ]
