import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {"title": translator.t("组件介绍")},
                {"title": translator.t("数据展示")},
                {"title": translator.t("AntdTable 表格")},
                {"title": translator.t("基础功能")},
            ],
            style={"marginBottom": 8},
        ),
        fac.AntdTitle(translator.t("AntdTable 表格"), level=2),
        fac.AntdParagraph(translator.t("表格组件主要基础功能示例。")),
    ]
