import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '通用'},
                {'title': 'AntdSwitch 开关'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdSwitch 开关', level=2),
        fac.AntdParagraph('使用开关在两种状态之间切换。'),
    ]
