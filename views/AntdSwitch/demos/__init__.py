from functools import partial

from dash.dependencies import Component

from components import demos_render

# 国际化
from i18n import translator

from . import (
    basic_callbacks,  # noqa: F401
    basic_usage,  # noqa: F401
    custom_checked_children,  # noqa: F401
    disabled,  # noqa: F401
    loading,  # noqa: F401
    read_only,  # noqa: F401
    size,  # noqa: F401
)


def demos_config() -> list:
    t = partial(translator.t, locale_topic="AntdSwitch")
    return [
        {
            "path": "basic_usage",
            "title": t("基础使用"),
            "description": t("最简单的用法。"),
        },
        {
            "path": "custom_checked_children",
            "title": t("自定义开关标签"),
            "description": t(
                "通过给`checkedChildren`和`unCheckedChildren`属性传入组件型参数，可以自定义开关标签。"
            ),
        },
        {
            "path": "size",
            "title": t("不同大小"),
            "description": t("通过`size`设置开关的尺寸。"),
        },
        {
            "path": "disabled",
            "title": t("禁用状态"),
            "description": t("可设置是否禁用开关。"),
        },
        {
            "path": "read_only",
            "title": t("只读状态"),
            "description": t("可设置开关状态为只读。"),
        },
        {
            "path": "loading",
            "title": t("加载中状态"),
            "description": t("可设置开关状态为加载中。"),
        },
        {
            "path": "basic_callbacks",
            "title": t("回调监听"),
            "description": t("通过`checked`实现对开关状态切换的监听。"),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
