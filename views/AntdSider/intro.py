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
                {'title': translator.t('经典布局')},
                {'title': translator.t('AntdSider 侧边栏')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdSider 侧边栏'), level=2),
        fac.AntdParagraph(translator.t('用于在经典布局方案中构建侧边栏部分。')),
    ]
