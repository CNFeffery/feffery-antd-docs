from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    sizes,  # noqa: F401
    variant,  # noqa: F401
    border,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    status,  # noqa: F401
    allow_clear,  # noqa: F401
    addon,  # noqa: F401
    prefix_and_suffix,  # noqa: F401
    max_length,  # noqa: F401
    show_count,  # noqa: F401
    count_format,  # noqa: F401
    auto_size,  # noqa: F401
    basic_callbacks,  # noqa: F401
    debounce_callbacks,  # noqa: F401
    md5_callbacks,  # noqa: F401
    n_submit_callbacks,  # noqa: F401
    n_click_search_callbacks,  # noqa: F401
    focusing_callbacks,  # noqa: F401
    empty_as_none,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '输入框可用的四种功能模式。',
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': '通过参数`size`控制输入框尺寸规格。',
    },
    {
        'path': 'variant',
        'title': '形态变体',
        'description': '通过参数`variant`控制输入框形态变体。',
    },
    {
        'path': 'border',
        'title': '设置边框',
        'description': '通过参数`bordered`控制输入框是否渲染边框。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '通过参数`disabled`控制输入框是否呈现禁用状态。',
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': '通过参数`readOnly`控制输入框是否呈现只读状态。',
    },
    {
        'path': 'status',
        'title': '强制渲染校验状态',
        'description': '通过参数`status`控制输入框显示强制校验状态。',
    },
    {
        'path': 'allow_clear',
        'title': '一键清空已输入值',
        'description': '通过参数`allowClear`控制输入框是否添加内容清空图标。',
    },
    {
        'path': 'addon',
        'title': '添加额外的前/后置元素',
        'description': '通过参数`addonBefore`、`addonAfter`为输入框添加额外的前/后置元素。',
    },
    {
        'path': 'prefix_and_suffix',
        'title': '添加内嵌的前/后置元素',
        'description': '通过参数`prefix`、`suffix`为输入框添加额外的内嵌前/后置元素。',
    },
    {
        'path': 'max_length',
        'title': '限制输入框最大内容长度',
        'description': '通过参数`maxLength`控制输入框最大可输入内容长度。',
    },
    {
        'path': 'show_count',
        'title': '展示已输入字符数量',
        'description': '通过参数`showCount`控制是否展示已输入字符数量。',
    },
    {
        'path': 'count_format',
        'title': '自定义字符计数规则',
        'description': '通过参数`countFormat`自定义已输入内容计数的正则表达式规则。',
    },
    {
        'path': 'auto_size',
        'title': '文本域输入框自适应高度',
        'description': '通过参数`autoSize`控制文本域输入框的高度自适应相关功能。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '通过回调函数监听输入框已输入内容。',
    },
    {
        'path': 'debounce_callbacks',
        'title': '防抖回调监听',
        'description': '通过回调函数监听`debounceValue`变化，实现对已输入内容的防抖监听。',
    },
    {
        'path': 'md5_callbacks',
        'title': 'md5加密回调监听',
        'description': '通过回调函数监听`md5Value`变化，实现对已输入内容的**md5**加密监听。',
    },
    {
        'path': 'n_submit_callbacks',
        'title': 'enter按键回调监听',
        'description': '通过回调函数监听`nSubmit`变化，实现对输入框内`enter`键事件的监听。',
    },
    {
        'path': 'n_click_search_callbacks',
        'title': '搜索按钮点击回调监听',
        'description': '通过回调函数监听`nClicksSearch`变化，实现对输入框搜索按钮点击事件的监听。',
    },
    {
        'path': 'focusing_callbacks',
        'title': '监听是否聚焦',
        'description': '通过回调函数监听`focusing`变化，实现对输入框聚焦状态的监听。',
    },
    {
        'path': 'empty_as_none',
        'title': '使用空值代替None',
        'description': '通过参数`emptyAsNone`控制空内容的赋值策略。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
