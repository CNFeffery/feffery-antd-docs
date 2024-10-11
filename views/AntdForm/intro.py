import feffery_antd_components as fac
from dash.dependencies import Component

# 国际化
from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('数据录入')},
                {'title': translator.t('表单')},
                {'title': translator.t('AntdForm 表单')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdForm 表单'), level=2),
        fac.AntdParagraph(
            translator.t('通过嵌套若干AntdFormItem的方式构建现代化表单。')
        ),
    ]
