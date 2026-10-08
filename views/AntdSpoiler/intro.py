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
                {'title': translator.t('AntdSpoiler 展开收起')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdSpoiler 展开收起'), level=2),
        fac.AntdParagraph(translator.t('用于实现对指定内容的展开收起效果。')),
    ]
