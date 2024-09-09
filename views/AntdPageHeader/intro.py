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
                {'title': translator.t('导航')},
                {'title': translator.t('AntdPageHeader 页头')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdPageHeader 页头'), level=2),
        fac.AntdParagraph(
            translator.t(
                '页头位于页容器顶部，起到内容概览和引导页级操作的作用。'
            )
        ),
    ]
