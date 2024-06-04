import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': 'AntdForm 表单'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdForm 表单', level=2),
        fac.AntdParagraph(
            [
                '通过嵌套若干',
                fac.AntdText('AntdFormItem', strong=True),
                '的方式构建现代化表单。',
            ]
        ),
    ]
