import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdCheckCardGroup 组合选择卡片'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCheckCardGroup 组合选择卡片', level=2),
        fac.AntdParagraph('用于监听一组选择卡片的选择情况。'),
    ]
