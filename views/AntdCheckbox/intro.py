import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdCheckbox 选择框'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdCheckbox 选择框', level=2),
        fac.AntdParagraph(
            [
                '用于在两种状态之间进行切换，类似',
                fac.AntdText('AntdSwitch', strong=True),
                '。',
            ]
        ),
    ]
