import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '导航'},
                {'title': 'AntdSteps 步骤条'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdSteps 步骤条', level=2),
        fac.AntdParagraph('用于引导用户按照流程完成一系列连贯的步骤。'),
    ]
