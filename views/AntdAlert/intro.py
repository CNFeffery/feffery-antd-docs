import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': 'AntdAlert 警告提示'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdAlert 警告提示', level=2),
        fac.AntdParagraph('用于渲染不同状态类型的警告提示信息。'),
    ]
