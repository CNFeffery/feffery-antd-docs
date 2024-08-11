import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdCopyText 文本复制'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCopyText 文本复制', level=2),
        fac.AntdParagraph('用于帮助用户快速复制指定文本内容。'),
    ]
