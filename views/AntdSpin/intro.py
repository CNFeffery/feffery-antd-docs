from i18n import translator
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': translator.t('组件介绍')},
                {'title': translator.t('反馈')},
                {'title': translator.t('AntdSpin 加载动画')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdSpin 加载动画'), level=2),
        fac.AntdParagraph(translator.t('用于为正在加载中的内容添加加载动画。')),
    ]
