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
                {'title': translator.t('AntdSlider 滑动输入条')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdSlider 滑动输入条'), level=2),
        fac.AntdParagraph(
            translator.t('用于为用户提供基于滑动交互的单值或范围设置功能。')
        ),
    ]
