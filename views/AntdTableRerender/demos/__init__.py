from dash.dependencies import Component

from . import (
    link_mode,  # noqa: F401
    ellipsis_mode,  # noqa: F401
    copyable_mode,  # noqa: F401
    ellipsis_copyable_mode,  # noqa: F401
    tags_mode,  # noqa: F401
    status_badge_mode,  # noqa: F401
    image_mode,  # noqa: F401
    custom_format_mode,  # noqa: F401
    corner_mark_mode,  # noqa: F401
    row_merge_mode,  # noqa: F401
    dropdown_links_mode,  # noqa: F401
    image_avatar_mode,  # noqa: F401
    mini_line_mode,  # noqa: F401
    mini_bar_mode,  # noqa: F401
    mini_area_mode,  # noqa: F401
    mini_progress_mode,  # noqa: F401
    mini_progress_show_percent,  # noqa: F401
    mini_progress_percent_position,  # noqa: F401
    mini_progress_percent_precision,  # noqa: F401
    mini_progress_round,  # noqa: F401
    mini_progress_size,  # noqa: F401
    mini_ring_progress_mode,  # noqa: F401
    button_mode_and_callbacks,  # noqa: F401
    button_mode_color,  # noqa: F401
    button_mode_independent_add_popconfirm,  # noqa: F401
    button_mode_independent_add_tooltip,  # noqa: F401
    checkbox_mode_and_callbacks,  # noqa: F401
    switch_mode_and_callbacks,  # noqa: F401
    dropdown_mode_and_callbacks,  # noqa: F401
    select_mode_and_callbacks,  # noqa: F401
    custom_component_cell_render,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'link_mode',
        'title': 'link链接模式',
        'description': '将单元格内容快捷渲染为链接形式。',
    },
    {
        'path': 'ellipsis_mode',
        'title': 'ellipsis长内容省略模式',
        'description': '将单元格内容快捷渲染为长内容省略形式。',
    },
    {
        'path': 'copyable_mode',
        'title': 'copyable可复制模式',
        'description': '将单元格内容快捷渲染为可复制形式。',
    },
    {
        'path': 'ellipsis_copyable_mode',
        'title': 'ellipsis-copyable长内容省略+可复制模式',
        'description': '将单元格内容快捷渲染为长内容省略+可复制形式。',
    },
    {
        'path': 'tags_mode',
        'title': 'tags标签模式',
        'description': '将单元格内容快捷渲染为标签形式。',
    },
    {
        'path': 'status_badge_mode',
        'title': 'status-badge状态徽标模式',
        'description': '将单元格内容快捷渲染为状态徽标形式。',
    },
    {
        'path': 'image_mode',
        'title': 'image图片模式',
        'description': '将单元格内容快捷渲染为图片形式。',
    },
    {
        'path': 'custom_format_mode',
        'title': 'custom-format自定义格式模式',
        'description': '在这个例子中，数值测试1与数值测试2字段本质上都是数值型，但在`"custom-format"`模式下，可通过参数`customFormatFuncs`自定义的js函数来改变单元格中表面上所渲染出的内容格式。',
    },
    {
        'path': 'corner_mark_mode',
        'title': 'corner-mark角标模式',
        'description': '将单元格内容快捷渲染为角标形式。',
    },
    {
        'path': 'row_merge_mode',
        'title': 'row-merge跨行单元格合并模式',
        'description': '将单元格内容快捷渲染为跨行单元格合并形式。',
    },
    {
        'path': 'dropdown_links_mode',
        'title': 'dropdown-links下拉链接菜单模式',
        'description': '将单元格内容快捷渲染为下拉链接菜单形式。',
    },
    {
        'path': 'image_avatar_mode',
        'title': 'image-avatar图片型头像模式',
        'description': '将单元格内容快捷渲染为图片型头像形式。',
    },
    {
        'path': 'mini_line_mode',
        'title': 'mini-line迷你折线图模式',
        'description': '将单元格内容快捷渲染为迷你折线图形式。',
    },
    {
        'path': 'mini_bar_mode',
        'title': 'mini-bar迷你柱状图模式',
        'description': '将单元格内容快捷渲染为迷你柱状图形式。',
    },
    {
        'path': 'mini_area_mode',
        'title': 'mini-area迷你面积图模式',
        'description': '将单元格内容快捷渲染为迷你面积图形式。',
    },
    {
        'path': 'mini_progress_mode',
        'title': '迷你进度图模式基础使用',
        'description': '将单元格内容快捷渲染为迷你进度图形式。',
        'group': 'mini-progress迷你进度图模式',
    },
    {
        'path': 'mini_progress_show_percent',
        'title': '显示进度数值',
        'description': '基于配置项`progressShowPercent`控制是否显示进度数值。',
        'group': 'mini-progress迷你进度图模式',
    },
    {
        'path': 'mini_progress_percent_position',
        'title': '调整进度数值位置',
        'description': '基于配置项`progressPercentPosition`调整进度数值位置。',
        'group': 'mini-progress迷你进度图模式',
    },
    {
        'path': 'mini_progress_percent_precision',
        'title': '控制进度数值小数位数',
        'description': '基于配置项`progressPercentPrecision`控制进度数值小数位数。',
        'group': 'mini-progress迷你进度图模式',
    },
    {
        'path': 'mini_progress_round',
        'title': '圆角矩形风格',
        'description': '基于配置项`progressStrokeLinecap`控制进度条风格。',
        'group': 'mini-progress迷你进度图模式',
    },
    {
        'path': 'mini_progress_size',
        'title': '控制进度条尺寸',
        'description': '基于配置项`progressSize`控制进度条像素尺寸。',
        'group': 'mini-progress迷你进度图模式',
    },
    {
        'path': 'mini_ring_progress_mode',
        'title': 'mini-ring-progress迷你环形进度图模式',
        'description': '将单元格内容快捷渲染为迷你环形进度图形式。',
    },
    {
        'path': 'button_mode_and_callbacks',
        'title': 'button按钮模式及回调监听',
        'description': '将单元格内容快捷渲染为按钮形式，并通过回调监听相关事件。',
        'group': 'button按钮模式',
    },
    {
        'path': 'button_mode_color',
        'title': '控制按钮形态',
        'description': '配合`color`与`variant`参数渲染具有不同颜色和形态的按钮。',
        'group': 'button按钮模式',
    },
    {
        'path': 'button_mode_independent_add_popconfirm',
        'title': '独立控制按钮是否添加气泡确认框',
        'description': '同一单元格中的每个按钮都可以单独控制是否添加气泡确认框。',
        'group': 'button按钮模式',
    },
    {
        'path': 'button_mode_independent_add_tooltip',
        'title': '独立控制按钮是否添加文字提示框',
        'description': '同一单元格中的每个按钮都可以单独控制是否添加文字提示框。',
        'group': 'button按钮模式',
    },
    {
        'path': 'checkbox_mode_and_callbacks',
        'title': 'checkbox勾选框模式及回调监听',
        'description': '将单元格内容快捷渲染为勾选框形式，并通过回调监听相关事件。',
    },
    {
        'path': 'switch_mode_and_callbacks',
        'title': 'switch开关模式及回调监听',
        'description': '将单元格内容快捷渲染为开关形式，并通过回调监听相关事件。',
    },
    {
        'path': 'dropdown_mode_and_callbacks',
        'title': 'dropdown下拉菜单模式及回调监听',
        'description': '将单元格内容快捷渲染为下拉菜单形式，并通过回调监听相关事件。',
    },
    {
        'path': 'select_mode_and_callbacks',
        'title': 'select下拉选择模式及回调监听',
        'description': '将单元格内容快捷渲染为下拉选择形式，并通过回调监听相关事件。',
    },
    {
        'path': 'custom_component_cell_render',
        'title': '自定义单元格元素',
        'description': '目前已有的快捷再渲染模式满足不了你的需求？没关系，任何组件元素都可以作为单元格值被传入😉！（此特性建议仅用作静态展示使用）',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
