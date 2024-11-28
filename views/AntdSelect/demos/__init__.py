from dash.dependencies import Component

from . import (
    auto_spin,  # noqa: F401
    basic_usage,  # noqa: F401
    debounce_search_callbacks,  # noqa: F401
    list_height,  # noqa: F401
    placement,  # noqa: F401
    popup_container,  # noqa: F401
    popup_match_select_width,  # noqa: F401
    sizes,  # noqa: F401
    variant,  # noqa: F401
    border,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    prefix,  # noqa: F401
    status,  # noqa: F401
    allow_clear,  # noqa: F401
    show_count,  # noqa: F401
    basic_callbacks,  # noqa: F401
    multiple,  # noqa: F401
    tags,  # noqa: F401
    max_tag_count,  # noqa: F401
    short_options,  # noqa: F401
    color_select,  # noqa: F401
    group,  # noqa: F401
    addon,  # noqa: F401
    empty_content,  # noqa: F401
    options_label,  # noqa: F401
    disabled_options,  # noqa: F401
    basic_search,  # noqa: F401
    auto_clear_search_value,  # noqa: F401
    options_filter_mode,  # noqa: F401
    options_filter_prop,  # noqa: F401
    search_value_callbacks,  # noqa: F401,
    options_share,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基础的使用示例。',
    },
    {
        'path': 'multiple',
        'title': '多选模式',
        'description': '可以多选的下拉选择使用示例。',
    },
    {
        'path': 'tags',
        'title': '自由新增模式',
        'description': '自由新增模式下，在输入框中输入内容后按下`enter`键、`tab`键，或点击下拉框中的选项、使下拉选择框失焦等，都可以进行新选项的添加。',
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': '通过参数`size`控制下拉选择组件的尺寸规格。',
    },
    {
        'path': 'variant',
        'title': '形态变体',
        'description': '通过参数`variant`控制下拉选择组件的形态变体。',
    },
    {
        'path': 'border',
        'title': '设置边框',
        'description': '通过参数`bordered`控制是否渲染下拉选择组件的边框。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '通过参数`disabled`控制是否禁用当前组件。',
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': '通过参数`readOnly`控制下拉选择框是否呈现只读状态。',
    },
    {
        'path': 'prefix',
        'title': '内嵌前缀内容',
        'description': '通过参数`prefix`设置选择框内嵌前缀内容。',
    },
    {
        'path': 'status',
        'title': '强制渲染校验状态',
        'description': '通过参数`status`控制下拉选择框强制校验状态显示。',
    },
    {
        'path': 'allow_clear',
        'title': '一键清空已选项',
        'description': '通过参数`allowClear`控制是否允许清空已选项。',
    },
    {
        'path': 'max_tag_count',
        'title': '已选项最大显示数量',
        'description': '通过参数`maxTagCount`控制下拉选择组件的最大可选项数。',
    },
    {
        'path': 'options_label',
        'title': '自定义选项标签',
        'description': '选项的`label`支持传入自定义组件。',
    },
    {
        'path': 'disabled_options',
        'title': '禁用选项',
        'description': '选项的`disabled`可用于控制是否禁用对应选项。',
    },
    {
        'path': 'short_options',
        'title': '简写选项',
        'description': '参数`options`可直接传入可选值数组快捷构建常规下拉选择功能。',
    },
    {
        'path': 'color_select',
        'title': '色带选择模式',
        'description': '特殊的色带选择模式',
    },
    {
        'path': 'group',
        'title': '下拉选项分组',
        'description': '下拉选项可分组。',
    },
    {
        'path': 'addon',
        'title': '下拉菜单扩展',
        'description': '为下拉菜单设置额外的顶部或底部扩展组件型内容',
    },
    {
        'path': 'empty_content',
        'title': '自定义无选项提示内容',
        'description': '可自定义下拉选择框无选项时的提示内容。',
    },
    {
        'path': 'list_height',
        'title': '下拉选择菜单高度',
        'description': '设置下拉选择菜单的像素高度。',
    },
    {
        'path': 'placement',
        'title': '悬浮层展开方向',
        'description': '可设置不同的下拉选择菜单悬浮层展开方向。',
    },
    {
        'path': 'popup_match_select_width',
        'title': '下拉选择菜单是否与选择框同宽',
        'description': '可设置下拉选择菜单是否与选择框同宽，默认为`True`。设置为`False`时，下拉选择菜单将关闭虚拟滚动功能。在数据量较大的情况下，性能可能会有所下降。',
    },
    {
        'path': 'popup_container',
        'title': '悬浮层锚定策略',
        'description': "可设置下拉选择菜单悬浮展开层在文档流中锚定的位置。设置为`'body'`时，下拉选择菜单将被渲染到body元素下，设置为`'parent'`时，下拉选择菜单将被渲染到下拉选择框的元素下。默认值：`'body'`。关于该参数的更多说明详见：[弹出层容器设置](/popup-container)。",
    },
    {
        'path': 'basic_search',
        'title': '自带搜索选项功能',
        'description': '所有下拉选择框自带搜索选项的功能。',
    },
    {
        'path': 'auto_clear_search_value',
        'title': '选中后自动清空搜索框内容',
        'description': '控制选中后自动清空搜索框内容。',
    },
    {
        'path': 'options_filter_mode',
        'title': '搜索匹配模式',
        'description': '内置的多种搜索匹配模式。',
    },
    {
        'path': 'options_filter_prop',
        'title': '搜索目标属性',
        'description': '指定选项搜索目标字段',
    },
    {
        'path': 'basic_callbacks',
        'title': '选项监听回调',
        'description': '可监听已选项值的变化情况，触发回调。',
    },
    {
        'path': 'search_value_callbacks',
        'title': '搜索内容监听回调',
        'description': '可监听搜索框输入值，触发回调。',
    },
    {
        'path': 'debounce_search_callbacks',
        'title': '搜索内容防抖监听回调',
        'description': '通过回调监听属性`debounceValue`实现防抖版本的已输入搜索内容监听。',
    },
    {
        'path': 'auto_spin',
        'title': '配合autoSpin实现远程加载',
        'description': '基于回调函数实现远程选项搜索加载功能。',
    },
    {
        'path': 'options_share',
        'title': '回调实现多选框选项互斥',
        'description': '基于回调函数实现多选框选项互斥功能。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
