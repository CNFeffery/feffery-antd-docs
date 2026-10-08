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
                {'title': translator.t('AntdWatermark 水印')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdWatermark 水印'), level=2),
        fac.AntdParagraph(translator.t('用于在指定内容上叠加水印内容。')),
    ]
