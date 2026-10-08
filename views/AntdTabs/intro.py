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
                {'title': translator.t('标签页 AntdTabs')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('标签页 AntdTabs'), level=2),
        fac.AntdParagraph(translator.t('用于构建多标签页。')),
    ]
