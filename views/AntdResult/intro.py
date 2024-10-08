import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '反馈'},
                {'title': 'AntdResult 结果'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdResult 结果', level=2),
        fac.AntdParagraph('用于为用户提供不同场景下的状态提示。'),
    ]
