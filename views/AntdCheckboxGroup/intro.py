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
                {'title': translator.t('AntdCheckboxGroup 组合选择框')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdCheckboxGroup 组合选择框'), level=2),
        fac.AntdParagraph(
            translator.t('由若干选择框组成，用于在一组可选项中进行多项选择。')
        ),
    ]
