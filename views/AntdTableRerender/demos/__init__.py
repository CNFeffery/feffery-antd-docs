from functools import partial

from dash.dependencies import Component

from components import demos_render
from i18n import translator

from . import (
    button_mode_and_callbacks,  # noqa: F401
    button_mode_color,  # noqa: F401
    button_mode_independent_add_popconfirm,  # noqa: F401
    button_mode_independent_add_tooltip,  # noqa: F401
    checkbox_mode_and_callbacks,  # noqa: F401
    copyable_mode,  # noqa: F401
    corner_mark_mode,  # noqa: F401
    custom_component_cell_render,  # noqa: F401
    custom_format_mode,  # noqa: F401
    dropdown_links_mode,  # noqa: F401
    dropdown_mode_and_callbacks,  # noqa: F401
    ellipsis_copyable_mode,  # noqa: F401
    ellipsis_mode,  # noqa: F401
    image_avatar_mode,  # noqa: F401
    image_mode,  # noqa: F401
    link_mode,  # noqa: F401
    mini_area_mode,  # noqa: F401
    mini_bar_mode,  # noqa: F401
    mini_line_mode,  # noqa: F401
    mini_progress_color,  # noqa: F401
    mini_progress_mode,  # noqa: F401
    mini_progress_percent_position,  # noqa: F401
    mini_progress_percent_precision,  # noqa: F401
    mini_progress_round,  # noqa: F401
    mini_progress_show_percent,  # noqa: F401
    mini_progress_size,  # noqa: F401
    mini_ring_progress_mode,  # noqa: F401
    row_merge_mode,  # noqa: F401
    select_mode_and_callbacks,  # noqa: F401
    status_badge_mode,  # noqa: F401
    switch_mode_and_callbacks,  # noqa: F401
    tags_mode,  # noqa: F401
)


def demos_config() -> list:
    t = partial(translator.t, locale_topic="AntdTableCellRender")

    return [
        {
            "path": "link_mode",
            "title": t("link链接模式"),
            "description": t("将单元格内容快捷渲染为链接形式。"),
        },
        {
            "path": "ellipsis_mode",
            "title": t("ellipsis长内容省略模式"),
            "description": t("将单元格内容快捷渲染为长内容省略形式。"),
        },
        {
            "path": "copyable_mode",
            "title": t("copyable可复制模式"),
            "description": t("将单元格内容快捷渲染为可复制形式。"),
        },
        {
            "path": "ellipsis_copyable_mode",
            "title": t("ellipsis-copyable长内容省略+可复制模式"),
            "description": t("将单元格内容快捷渲染为长内容省略+可复制形式。"),
        },
        {
            "path": "tags_mode",
            "title": t("tags标签模式"),
            "description": t("将单元格内容快捷渲染为标签形式。"),
        },
        {
            "path": "status_badge_mode",
            "title": t("status-badge状态徽标模式"),
            "description": t("将单元格内容快捷渲染为状态徽标形式。"),
        },
        {
            "path": "image_mode",
            "title": t("image图片模式"),
            "description": t("将单元格内容快捷渲染为图片形式。"),
        },
        {
            "path": "custom_format_mode",
            "title": t("custom-format自定义格式模式"),
            "description": t(
                "在这个例子中，数值测试1与数值测试2字段本质上都是数值型，"
                "但在`custom-format`模式下，可通过参数`customFormatFuncs`自定义的"
                "js函数来改变单元格中所渲染出的内容格式。"
            ),
        },
        {
            "path": "corner_mark_mode",
            "title": t("corner-mark角标模式"),
            "description": t("将单元格内容快捷渲染为角标形式。"),
        },
        {
            "path": "row_merge_mode",
            "title": t("row-merge跨行单元格合并模式"),
            "description": t("将单元格内容快捷渲染为跨行单元格合并形式。"),
        },
        {
            "path": "dropdown_links_mode",
            "title": t("dropdown-links下拉链接菜单模式"),
            "description": t("将单元格内容快捷渲染为下拉链接菜单形式。"),
        },
        {
            "path": "image_avatar_mode",
            "title": t("image-avatar图片型头像模式"),
            "description": t("将单元格内容快捷渲染为图片型头像形式。"),
        },
        {
            "path": "mini_line_mode",
            "title": t("mini-line迷你折线图模式"),
            "description": t("将单元格内容快捷渲染为迷你折线图形式。"),
        },
        {
            "path": "mini_bar_mode",
            "title": t("mini-bar迷你柱状图模式"),
            "description": t("将单元格内容快捷渲染为迷你柱状图形式。"),
        },
        {
            "path": "mini_area_mode",
            "title": t("mini-area迷你面积图模式"),
            "description": t("将单元格内容快捷渲染为迷你面积图形式。"),
        },
        {
            "path": "mini_progress_mode",
            "title": t("迷你进度图模式基础使用"),
            "description": t("将单元格内容快捷渲染为迷你进度图形式。"),
            "group": t("mini-progress迷你进度图模式"),
        },
        {
            "path": "mini_progress_show_percent",
            "title": t("显示进度数值"),
            "description": t("基于配置项`progressShowPercent`控制是否显示进度数值。"),
            "group": t("mini-progress迷你进度图模式"),
        },
        {
            "path": "mini_progress_percent_position",
            "title": t("调整进度数值位置"),
            "description": t("基于配置项`progressPercentPosition`调整进度数值位置。"),
            "group": t("mini-progress迷你进度图模式"),
        },
        {
            "path": "mini_progress_percent_precision",
            "title": t("控制进度数值小数位数"),
            "description": t(
                "基于配置项`progressPercentPrecision`控制进度数值小数位数。"
            ),
            "group": t("mini-progress迷你进度图模式"),
        },
        {
            "path": "mini_progress_round",
            "title": t("圆角矩形风格"),
            "description": t("基于配置项`progressStrokeLinecap`控制进度条风格。"),
            "group": t("mini-progress迷你进度图模式"),
        },
        {
            "path": "mini_progress_size",
            "title": t("控制进度条尺寸"),
            "description": t("基于配置项`progressSize`控制进度条像素尺寸。"),
            "group": t("mini-progress迷你进度图模式"),
        },
        {
            "path": "mini_progress_color",
            "title": t("控制进度条颜色"),
            "description": t("基于配置项`progressColor`控制进度条颜色，支持渐变色。"),
            "group": t("mini-progress迷你进度图模式"),
        },
        {
            "path": "mini_ring_progress_mode",
            "title": t("mini-ring-progress迷你环形进度图模式"),
            "description": t("将单元格内容快捷渲染为迷你环形进度图形式。"),
        },
        {
            "path": "button_mode_and_callbacks",
            "title": t("button按钮模式及回调监听"),
            "description": t(
                "将单元格内容快捷渲染为按钮形式，并通过回调监听相关事件。"
            ),
            "group": t("button按钮模式"),
        },
        {
            "path": "button_mode_color",
            "title": t("控制按钮形态"),
            "description": t(
                "配合`color`与`variant`参数渲染具有不同颜色和形态的按钮。"
            ),
            "group": t("button按钮模式"),
        },
        {
            "path": "button_mode_independent_add_popconfirm",
            "title": t("独立控制按钮是否添加气泡确认框"),
            "description": t(
                "同一单元格中的每个按钮都可以单独控制是否添加气泡确认框。"
            ),
            "group": t("button按钮模式"),
        },
        {
            "path": "button_mode_independent_add_tooltip",
            "title": t("独立控制按钮是否添加文字提示框"),
            "description": t(
                "同一单元格中的每个按钮都可以单独控制是否添加文字提示框。"
            ),
            "group": t("button按钮模式"),
        },
        {
            "path": "checkbox_mode_and_callbacks",
            "title": t("checkbox勾选框模式及回调监听"),
            "description": t(
                "将单元格内容快捷渲染为勾选框形式，并通过回调监听相关事件。"
            ),
        },
        {
            "path": "switch_mode_and_callbacks",
            "title": t("switch开关模式及回调监听"),
            "description": t(
                "将单元格内容快捷渲染为开关形式，并通过回调监听相关事件。"
            ),
        },
        {
            "path": "dropdown_mode_and_callbacks",
            "title": t("dropdown下拉菜单模式及回调监听"),
            "description": t(
                "将单元格内容快捷渲染为下拉菜单形式，并通过回调监听相关事件。"
            ),
        },
        {
            "path": "select_mode_and_callbacks",
            "title": t("select下拉选择模式及回调监听"),
            "description": t(
                "将单元格内容快捷渲染为下拉选择形式，并通过回调监听相关事件。"
            ),
        },
        {
            "path": "custom_component_cell_render",
            "title": t("自定义单元格元素"),
            "description": t(
                "目前已有的快捷再渲染模式满足不了你的需求？没关系，"
                "任何组件元素都可以作为单元格值被传入😉！（此特性建议仅用作静态展示使用）"
            ),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config(),
        section_name=section_name,
    )
