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
                {'title': translator.t('AntdCardGrid 卡片网格')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdCardGrid 卡片网格'), level=2),
        fac.AntdParagraph(translator.t('用于构建内嵌的网格布局卡片。')),
    ]
