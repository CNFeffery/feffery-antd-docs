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
                {'title': translator.t('Fragment 空节点')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('Fragment 空节点'), level=2),
        fac.AntdParagraph(
            translator.t('承载内部元素且本身不渲染占用DOM节点。')
        ),
    ]
