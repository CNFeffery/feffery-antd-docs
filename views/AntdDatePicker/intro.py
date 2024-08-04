import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdDatePicker 日期选择'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdDatePicker 日期选择', level=2),
        fac.AntdParagraph('提供常见的日期选择相关功能。'),
    ]
