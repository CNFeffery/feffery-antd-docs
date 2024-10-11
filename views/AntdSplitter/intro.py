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
                {'title': translator.t('AntdSplitter 分隔面板')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdSplitter 分隔面板'), level=2),
        fac.AntdParagraph(
            translator.t('对指定区域进行切分，并添加交互性的尺寸调整。')
        ),
    ]
