from i18n import translator
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('数据录入')},
                {'title': translator.t('AntdTransfer 穿梭框')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdTransfer 穿梭框'), level=2),
        fac.AntdParagraph(
            translator.t(
                '用于以直观的方式在两栏中移动选项，帮助用户完成选择行为。'
            )
        ),
    ]
