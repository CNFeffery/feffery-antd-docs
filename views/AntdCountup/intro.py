import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdCountup 正计时'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCountup 正计时', level=2),
        fac.AntdParagraph('用于渲染实时刷新的正计时信息卡片。'),
    ]
