from i18n import translator
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('数据展示')},
                {'title': translator.t('卡片')},
                {'title': translator.t('AntdCardMeta 结构化卡片')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdCardMeta 结构化卡片'), level=2),
        fac.AntdParagraph(translator.t('用于为卡片添加结构化展示信息。')),
    ]
