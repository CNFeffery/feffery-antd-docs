from functools import partial

from dash.dependencies import Component

from components import demos_render

# 国际化
from i18n import translator

from . import (
    basic_callbacks,  # noqa: F401
    basic_usage,  # noqa: F401
    custom_cells,  # noqa: F401
    custom_format,  # noqa: F401
    different_picker,  # noqa: F401
    different_placement,  # noqa: F401
    disabled,  # noqa: F401
    disabled_dates,  # noqa: F401
    dynamic_disabled_dates,  # noqa: F401
    extra_footer,  # noqa: F401
    hide_today,  # noqa: F401
    listen_picker_value,  # noqa: F401
    picker_value,  # noqa: F401
    prefix,  # noqa: F401
    read_only,  # noqa: F401
    render_status,  # noqa: F401
    suffix_icon,  # noqa: F401
    time_default_value,  # noqa: F401
)


def demos_config() -> list:
    t = partial(translator.t, locale_topic="AntdDatePicker")
    return [
        {
            "path": "basic_usage",
            "title": t("基础使用"),
            "description": t("最基础的日期选择、日期时间选择。"),
        },
        {
            "path": "hide_today",
            "title": t("隐藏今天按钮"),
            "description": t("隐藏“今天”快捷选择按钮。"),
        },
        {
            "path": "time_default_value",
            "title": t("设置自动选定的时间值"),
            "description": t(
                "由参数`showTime.defaultValue`设定的默认值，将会在用户初次选中日期后，在时间选择面板中被自动选中。"
            ),
        },
        {
            "path": "different_placement",
            "title": t("悬浮层展开方位"),
            "description": t("设置参数`placement`控制悬浮层展开方位。"),
        },
        {
            "path": "different_picker",
            "title": t("不同的日期选择粒度"),
            "description": t("设置参数`picker`选择不同的日期选择粒度。"),
        },
        {
            "path": "custom_format",
            "title": t("自定义format"),
            "description": t(
                "设置参数`format`以实现不同粒度设置下适合的已选内容回填格式化。"
            ),
        },
        {
            "path": "disabled",
            "title": t("禁用状态"),
            "description": t("设置参数`disabled=True`开启禁用状态。"),
        },
        {
            "path": "read_only",
            "title": t("只读状态"),
            "description": t("设置参数`readOnly=True`开启只读状态。"),
        },
        {
            "path": "prefix",
            "title": t("内嵌前缀内容"),
            "description": t("通过参数`prefix`设置选择框内嵌前缀内容。"),
        },
        {
            "path": "suffix_icon",
            "title": t("内嵌后缀图标"),
            "description": t("通过参数`suffixIcon`设置选择框内嵌后缀图标。"),
        },
        {
            "path": "render_status",
            "title": t("强制状态渲染"),
            "description": t("设置参数`status`强制状态渲染。"),
        },
        {
            "path": "picker_value",
            "title": t("控制面板停留位置"),
            "description": None,
        },
        {
            "path": "disabled_dates",
            "title": t("自定义日期禁用策略"),
            "description": t(
                "设置参数`disabledDatesStrategy`控制需要禁止用户选中的日期。"
            ),
        },
        {
            "path": "extra_footer",
            "title": t("底部添加额外内容"),
            "description": t("通过参数`extraFooter`自定义选择面板底部额外的内容。"),
        },
        {
            "path": "custom_cells",
            "title": t("控制指定日期单元格样式"),
            "description": t(
                "通过参数`customCells`对指定规则对应的日期单元格添加额外样式，未填写条件的部分将视作通配规则。"
            ),
        },
        {
            "path": "basic_callbacks",
            "title": t("回调监听"),
            "description": None,
        },
        {
            "path": "dynamic_disabled_dates",
            "title": t("基于回调的动态日期禁用"),
            "description": t(
                "通过回调函数实现基于当前日期时间的动态禁用策略，以“只允许选择未来7天内日期”为例。"
            ),
        },
        {
            "path": "listen_picker_value",
            "title": t("监听面板停留位置"),
            "description": t(
                "通过回调函数监听`pickerValue`的变化，获取当前面板停留位置。"
            ),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
