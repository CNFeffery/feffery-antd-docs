import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '数据录入'},
                {'title': '表单'},
                {'title': 'AntdFormItem 表单项'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdFormItem 表单项', level=2),
        fac.AntdParagraph('在表单中构建单个表单项。'),
    ]
