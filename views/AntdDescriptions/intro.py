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
                {'title': translator.t('描述列表')},
                {'title': translator.t('AntdDescriptions 描述列表')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdDescriptions 描述列表'), level=2),
        fac.AntdParagraph(
            translator.t('用于配合AntdDescriptionItem进行一组属性的展示。')
        ),
    ]
