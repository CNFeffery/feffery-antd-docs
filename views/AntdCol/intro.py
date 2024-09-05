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
                {'title': translator.t('布局')},
                {'title': translator.t('网格系统')},
                {'title': translator.t('AntdCol 列')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdCol 列'), level=2),
        fac.AntdParagraph(translator.t('在网格系统中构建单个列元素。')),
    ]
