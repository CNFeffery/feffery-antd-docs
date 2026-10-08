from i18n import translator
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('其他')},
                {'title': translator.t('AntdBackTop 回到顶部')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdBackTop 回到顶部'), level=2),
        fac.AntdParagraph(translator.t('用于帮助用户在长页面中快速回到顶部。')),
    ]
