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
                {'title': translator.t('AntdAffix 固钉')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdAffix 固钉'), level=2),
        fac.AntdParagraph(
            translator.t(
                '确保内部元素原有位置在被用户滚动出视口后，仍然可以在视口范围内保持可见状态。'
            )
        ),
    ]
