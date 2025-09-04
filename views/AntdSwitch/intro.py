import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import translator


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {"title": translator.t("组件介绍")},
                {"title": translator.t("数据录入")},
                {"title": translator.t("AntdSwitch 开关")},
            ],
            style={"marginBottom": 8},
        ),
        fac.AntdTitle(translator.t("AntdSwitch 开关"), level=2),
        fac.AntdParagraph(translator.t("使用开关在两种状态之间切换。")),
    ]
