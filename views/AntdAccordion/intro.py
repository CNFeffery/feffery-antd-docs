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
                {"title": translator.t("AntdAccordion 手风琴")},
            ],
            style={"marginBottom": 8},
        ),
        fac.AntdTitle(translator.t("AntdAccordion 手风琴"), level=2),
        fac.AntdParagraph(translator.t("展示一组同级内容的特殊形式。")),
    ]
