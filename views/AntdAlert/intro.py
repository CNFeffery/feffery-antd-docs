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
                {'title': translator.t('AntdAlert 警告提示')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdAlert 警告提示'), level=2),
        fac.AntdParagraph(translator.t('用于渲染不同状态类型的警告提示信息。')),
    ]
