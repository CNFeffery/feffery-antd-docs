import feffery_antd_components as fac
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
        'description': fac.AntdParagraph('使用基础的四种输入模式。'),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph(
            [
                '可设置三种不同大小：',
                fac.AntdText("'small'", code=True),
                '（高度：24px）、',
                fac.AntdText("'middle'", code=True),
                '（高度：32px）、',
                fac.AntdText("'large'", code=True),
                '（高度：40px），默认值：',
                fac.AntdText("'middle'", code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'variant',
        'title': '形态变体',
        'description': fac.AntdParagraph(
            [
                '可设置三种预设形态变体：',
                fac.AntdText("'outlined'", code=True),
                '、',
                fac.AntdText("'filled'", code=True),
                '、',
                fac.AntdText("'borderless'", code=True),
                '，默认值：',
                fac.AntdText("'outlined'", code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'border',
        'title': '设置边框',
        'description': fac.AntdParagraph(
            [
                '可设置是否渲染边框，当设置为',
                fac.AntdText("'True'", code=True),
                '时等价于',
                fac.AntdText("variant='outlined'", code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '可设置是否禁用输入框。',
            ]
        ),
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': fac.AntdParagraph(
            [
                '可设置输入框状态为只读。',
            ]
        ),
    },
    {
        'path': 'status',
        'title': '强制渲染校验状态',
        'description': fac.AntdParagraph(
            [
                '可强制渲染输入框的校验状态，',
                fac.AntdText('addonBefore', strong=True),
                '、',
                fac.AntdText('addonAfter', strong=True),
                '和',
                fac.AntdText('suffix', strong=True),
                '、',
                fac.AntdText('prefix', strong=True),
                '也会被渲染。',
            ]
        ),
    },
    {
        'path': 'allow_clear',
        'title': '一键清空已输入值',
        'description': fac.AntdParagraph(
            [
                '设置为',
                fac.AntdText('True', code=True),
                '时会渲染一键清空按钮，点击清空已输入值。在',
                fac.AntdText("mode='password'", code=True),
                '时无效。',
            ]
        ),
    },
    {
        'path': 'addon',
        'title': '添加额外的前/后置元素',
        'description': fac.AntdParagraph(
            [
                '针对默认模式下的输入框，可以通过参数',
                fac.AntdText('addonBefore', strong=True),
                '、',
                fac.AntdText('addonAfter', strong=True),
                '为输入框添加额外的前/后置内容，实现功能的一体化。',
            ]
        ),
    },
    {
        'path': 'prefix_and_suffix',
        'title': '添加内嵌的前/后置元素',
        'description': fac.AntdParagraph(
            [
                '针对',
                fac.AntdText("mode='default'", code=True),
                '下的输入框，可以通过参数',
                fac.AntdText('prefix', strong=True),
                '、',
                fac.AntdText('suffix', strong=True),
                '为输入框添加内嵌的前/后置内容，实现功能的一体化。',
                fac.AntdText("mode='password'", code=True),
                '下的输入框，也可以通过参数',
                fac.AntdText('prefix', strong=True),
                '添加内嵌的前置内容。',
            ]
        ),
    },
    {
        'path': 'max_length',
        'title': '限制输入框最大内容长度',
        'description': fac.AntdParagraph(
            [
                '限制输入框内容的最大内容长度，以maxLength=10为例。',
            ]
        ),
    },
    {
        'path': 'show_count',
        'title': '展示已输入字符数量',
        'description': fac.AntdParagraph(
            [
                '在组件下方展示已输入的字符数量，仅在',
                fac.AntdText('mode="text-area"', code=True),
                '时有效。',
            ]
        ),
    },
    {
        'path': 'count_format',
        'title': '自定义字符计数规则',
        'description': fac.AntdParagraph(
            [
                '使用正则表达式自定义字符计数规则，仅在',
                fac.AntdText('showCount=True', code=True),
                '时有效。',
            ]
        ),
    },
    {
        'path': 'auto_size',
        'title': '文本域输入框自适应高度',
        'description': fac.AntdParagraph(
            [
                '输入框跟随内容自适应高度，仅在',
                fac.AntdText('mode="text-area"', code=True),
                '时有效。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                '展示常见的回调函数用法。',
            ]
        ),
    },
    {
        'path': 'debounce_callbacks',
        'title': '防抖回调监听',
        'description': fac.AntdParagraph(
            [
                '在回调函数中用debounceValue代替value可以实现对用户实时输入值变化的防抖监听，避免回调函数被频繁触发执行。在用户输入停顿超过',
                fac.AntdText('debounceWait', strong=True),
                '的时长时，才会触发回调函数。',
            ]
        ),
    },
    {
        'path': 'md5_callbacks',
        'title': 'md5加密回调监听',
        'description': fac.AntdParagraph(
            [
                '当',
                fac.AntdText('mode="password"', code=True),
                '且',
                fac.AntdText('passwordUseMd5=True', code=True),
                '时，启用md5加密功能，通过加密后的md5Value触发回调。',
            ]
        ),
    },
    {
        'path': 'n_submit_callbacks',
        'title': 'enter按键回调监听',
        'description': fac.AntdParagraph(
            [
                '当聚焦于输入框时，可监听输入框内enter键盘事件。',
            ]
        ),
    },
    {
        'path': 'n_click_search_callbacks',
        'title': '搜索按钮点击回调监听',
        'description': fac.AntdParagraph(
            [
                '当',
                fac.AntdText('mode="search"', code=True),
                '时，可监听搜索按钮点击事件。',
            ]
        ),
    },
    {
        'path': 'focusing_callbacks',
        'title': '监听是否聚焦',
        'description': fac.AntdParagraph(
            [
                '当输入框聚焦状态变化时，触发回调。',
            ]
        ),
    },
    {
        'path': 'empty_as_none',
        'title': '使用空值代替None',
        'description': fac.AntdParagraph(
            [
                '当输入框内容为空时，强制更新',
                fac.AntdText('value', code=True),
                '为',
                fac.AntdText('None', code=True),
                '。从而统一输入框内容为空字符串和None混合的情况。',
            ]
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
