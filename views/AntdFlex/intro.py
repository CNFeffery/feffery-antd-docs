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
                {'title': translator.t('AntdFlex 弹性布局')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdFlex 弹性布局'), level=2),
        fac.AntdParagraph(
            translator.t(
                '基于css中的flex布局原理，对一组元素进行水平或垂直方向上的排列。'
            )
        ),
    ]
