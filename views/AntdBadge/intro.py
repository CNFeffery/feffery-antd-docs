import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据展示'},
                {'title': 'AntdBadge 徽标数'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdBadge 徽标数', level=2),
        fac.AntdParagraph(
            '一般出现在通知图标或头像的右上角，用于显示需要处理的消息条数，通过醒目视觉形式吸引用户处理。'
        ),
    ]
