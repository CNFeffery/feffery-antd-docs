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
                {'title': translator.t('导航')},
                {'title': translator.t('AntdBreadcrumb 面包屑')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdBreadcrumb 面包屑'), level=2),
        fac.AntdParagraph(
            translator.t('用于展示当前页面在系统层级结构中的位置。')
        ),
    ]
