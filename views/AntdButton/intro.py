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
                {'title': translator.t('AntdButton 按钮')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdButton 按钮'), level=2),
        fac.AntdParagraph(translator.t('按钮用于触发一个即时操作。')),
    ]
