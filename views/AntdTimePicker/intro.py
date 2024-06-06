import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdTimePicker 时间选择'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdTimePicker 时间选择', level=2),
        fac.AntdParagraph('提供常用的时间选择功能。'),
    ]
