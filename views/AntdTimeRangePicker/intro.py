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
                {'title': translator.t('AntdTimeRangePicker 时间范围选择')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(
            translator.t('AntdTimeRangePicker 时间范围选择'), level=2
        ),
        fac.AntdParagraph(translator.t('提供常用的时间范围选择功能。')),
    ]
