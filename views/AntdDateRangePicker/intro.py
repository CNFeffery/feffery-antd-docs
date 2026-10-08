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
                {'title': translator.t('AntdDateRangePicker 日期范围选择')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('AntdDateRangePicker 日期范围选择'), level=2
        ),
        fac.AntdParagraph(translator.t('提供常见的日期范围选择相关功能。')),
    ]
