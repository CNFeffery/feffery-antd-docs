import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdOTP 一次性密码框'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdOTP 一次性密码框', level=2),
        fac.AntdParagraph('用于提供验证码等一次性固定位数密码输入功能。'),
    ]
