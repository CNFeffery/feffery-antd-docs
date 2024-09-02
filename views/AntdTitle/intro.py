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
                {'title': translator.t('通用')},
                {'title': translator.t('排版相关')},
                {'title': translator.t('AntdTitle 标题')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdTitle 标题'), level=2),
        fac.AntdParagraph(translator.t('用于渲染具有丰富样式和功能的标题。')),
    ]
