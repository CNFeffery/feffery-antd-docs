import feffery_antd_components as fac
from dash.dependencies import Component

# 国际化
from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('布局')},
                {'title': translator.t('AntdCompact 紧凑排列')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdCompact 紧凑排列'), level=2),
        fac.AntdParagraph(
            translator.t(
                '用于对若干内部组件进行紧凑排列，并为相邻组件之间自动合并边框。'
            )
        ),
        fac.AntdParagraph(
            translator.t(
                '注：目前支持进行紧凑布局的组件有AntdButton、AntdCascader、AntdDatePicker、AntdInput、AntdSelect、AntdTimePicker、AntdTreeSelect'
            ),
            type='secondary',
        ),
    ]
