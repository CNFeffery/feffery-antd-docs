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
                {'title': translator.t('AntdDropdown 下拉菜单')},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle(translator.t('AntdDropdown 下拉菜单'), level=2),
        fac.AntdParagraph(
            translator.t('用于展示具有若干选项或链接的向下弹出的列表。')
        ),
    ]
