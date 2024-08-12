import feffery_antd_components as fac
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
        'description': fac.AntdParagraph('基础的使用示例。'),
    },
    {
        'path': 'multiple',
        'title': '多选模式',
        'description': fac.AntdParagraph('可以多选的下拉选择使用示例。'),
    },
    {
        'path': 'tags',
        'title': '自由新增模式',
        'description': fac.AntdParagraph(
            [
                '自由新增模式下，在输入框中输入内容后按下',
                fac.AntdText('enter', code=True),
                '键、',
                fac.AntdText('tab', code=True),
                '键，',
                '或点击下拉框中的选项、使下拉选择框失焦等，都可以进行新选项的添加。',
            ]
        ),
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
                '可设置是否禁用下拉选择框。',
            ]
        ),
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': fac.AntdSpace(
            [
                '可设置下拉选择框状态为只读。',
                fac.AntdParagraph(
                    [
                        '在',
                        fac.AntdText("mode='multiple'", code=True),
                        '模式中，只读状态下无法进行选项的选择，但仍可以删除已选项。',
                    ],
                    style={'margin': 0},
                ),
                fac.AntdParagraph(
                    [
                        '在',
                        fac.AntdText("mode='tags'", code=True),
                        '模式中，只读状态下无法进行预设选项的选择，但仍可以自由新增选项和删除已选项。',
                    ]
                ),
            ],
            direction='vertical',
        ),
    },
    {
        'path': 'status',
        'title': '强制渲染校验状态',
        'description': fac.AntdParagraph(
            [
                '可强制渲染下拉选择框的校验状态，',
            ]
        ),
    },
    {
        'path': 'allow_clear',
        'title': '一键清空已选项',
        'description': fac.AntdParagraph(
            [
                '设置为',
                fac.AntdText('True', code=True),
                '，会在鼠标悬停时显示一键清空按钮，点击清空已选项。默认为',
                fac.AntdText('True', code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'max_tag_count',
        'title': '已选项最大显示数量',
        'description': fac.AntdParagraph(
            [
                '在',
                fac.AntdText('mode="multiple"', code=True),
                '或',
                fac.AntdText('mode="tags"', code=True),
                '时，可制定已选项超过一定数量情况下的显示策略。值为整数时，则在已选项数量超过值的情况下对后续选项省略显示。值为',
                fac.AntdText('responsive', code=True),
                '时，则会根据下拉选择框的宽度自动调整已选项的显示数量。',
            ]
        ),
    },
    {
        'path': 'options_label',
        'title': '自定义选项标签',
        'description': fac.AntdParagraph(
            [
                '自由定义选项标签，可传入样式丰富的组件型标签。',
            ]
        ),
    },
    {
        'path': 'disabled_options',
        'title': '禁用选项',
        'description': fac.AntdParagraph(
            [
                '可通过设置选项中的',
                fac.AntdText('disabled', code=True),
                '属性来禁用选项。',
            ]
        ),
    },
    {
        'path': 'short_options',
        'title': '简写选项',
        'description': fac.AntdParagraph(
            [
                '可用只含有字符串|数字的列表来简写',
                fac.AntdText('options', strong=True),
                '，',
                fac.AntdText('label', code=True),
                '和',
                fac.AntdText('value', code=True),
                '会设置为相同的值，同时不能设置',
                fac.AntdText('disabled', code=True),
                '、',
                fac.AntdText('group', code=True),
                '、',
                fac.AntdText('colors', code=True),
                '等属性。如需设置其他属性，请使用完整的列表嵌套字典形式来设置',
                fac.AntdText('options', strong=True),
                '。',
            ]
        ),
    },
    {
        'path': 'color_select',
        'title': '色带选择模式',
        'description': fac.AntdParagraph(
            [
                '可通过设置',
                fac.AntdText('options', strong=True),
                '中的',
                fac.AntdText('colors', code=True),
                '属性，启用特殊的色带选择器模式。',
            ]
        ),
    },
    {
        'path': 'group',
        'title': '下拉选项分组',
        'description': fac.AntdParagraph(
            [
                '可通过给设置',
                fac.AntdText('options', strong=True),
                '中的',
                fac.AntdText('group', code=True),
                '属性再嵌套设置',
                fac.AntdText('options', code=True),
                '的方式来实现下拉选项的分组。嵌套的',
                fac.AntdText('options', code=True),
                '不可简写。',
            ]
        ),
    },
    {
        'path': 'addon',
        'title': '下拉菜单扩展',
        'description': fac.AntdParagraph(
            [
                '可为下拉菜单设置额外的顶部或底部扩展组件型内容。',
            ]
        ),
    },
    {
        'path': 'empty_content',
        'title': '自定义无选项提示内容',
        'description': fac.AntdParagraph(
            [
                '可自定义下拉选择框无选项时的提示内容。',
            ]
        ),
    },
    {
        'path': 'list_height',
        'title': '下拉选择菜单高度',
        'description': fac.AntdParagraph(
            [
                '设置下拉选择菜单的像素高度。',
            ]
        ),
    },
    {
        'path': 'placement',
        'title': '悬浮层展开方向',
        'description': fac.AntdParagraph(
            [
                '可设置不同的下拉选择菜单悬浮层展开方向。',
            ]
        ),
    },
    {
        'path': 'popup_match_select_width',
        'title': '下拉选择菜单是否与选择框同宽',
        'description': fac.AntdParagraph(
            [
                '可设置下拉选择菜单是否与选择框同宽，默认为',
                fac.AntdText('True', code=True),
                '。设置为',
                fac.AntdText('False', code=True),
                '时，下拉选择菜单将关闭虚拟滚动功能。在数据量较大的情况下，性能可能会有所下降。',
            ]
        ),
    },
    {
        'path': 'popup_container',
        'title': '悬浮层锚定策略',
        'description': fac.AntdParagraph(
            [
                '可设置下拉选择菜单悬浮展开层在文档流中锚定的位置。设置为',
                fac.AntdText("'body'", code=True),
                '时，下拉选择菜单将被渲染到body元素下，设置为',
                fac.AntdText("'parent'", code=True),
                '时，下拉选择菜单将被渲染到下拉选择框的元素下。默认值：',
                fac.AntdText("'body'", code=True),
                '。关于该参数的更多说明详见：',
                fac.AntdButton(
                    '弹出层容器设置',
                    type='link',
                    href='popup-container',
                    style={'margin': 0, 'padding': 0, 'display': 'inline'},
                ),
                '。',
            ]
        ),
    },
    {
        'path': 'basic_search',
        'title': '自带搜索选项功能',
        'description': fac.AntdParagraph(
            [
                '所有下拉选择框自带搜索选项的功能。',
            ]
        ),
    },
    {
        'path': 'auto_clear_search_value',
        'title': '选中后自动清空搜索框内容',
        'description': fac.AntdParagraph(
            [
                '在',
                fac.AntdText('mode="multiple"', code=True),
                '或',
                fac.AntdText('mode="tags"', code=True),
                '时，可设置是否在选中项后自动清空搜索框中的内容，设置为',
                fac.AntdText('False', code=True),
                '便于连续选择。',
            ]
        ),
    },
    {
        'path': 'options_filter_mode',
        'title': '搜索匹配模式',
        'description': fac.AntdParagraph(
            [
                '可设置搜索匹配模式，可选的有：',
                fac.AntdText('case-insensitive', code=True),
                '（大小写不敏感）、',
                fac.AntdText('case-sensitive', code=True),
                '（大小写敏感）、',
                fac.AntdText('regex', code=True),
                '（正则表达式），默认为',
                fac.AntdText('case-insensitive', code=True),
                '（大小写不敏感）。',
            ]
        ),
    },
    {
        'path': 'options_filter_prop',
        'title': '搜索目标属性',
        'description': fac.AntdParagraph(
            [
                '可设置针对options中的何种属性进行搜索，可选的有：',
                fac.AntdText('value', code=True),
                '、',
                fac.AntdText('label', code=True),
                '，默认为',
                fac.AntdText('value', code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '选项监听回调',
        'description': fac.AntdParagraph(
            [
                '可监听已选项值的变化情况，触发回调。',
            ]
        ),
    },
    {
        'path': 'search_value_callbacks',
        'title': '搜索内容监听回调',
        'description': fac.AntdParagraph(
            [
                '可监听搜索框输入值，触发回调。',
            ]
        ),
    },
    {
        'path': 'debounce_search_callbacks',
        'title': '搜索内容防抖监听回调',
        'description': fac.AntdParagraph(
            [
                '在回调函数中用debounceValue代替value可以实现对用户搜索框输入值实时变化的防抖监听，避免回调函数被频繁触发执行。在用户输入停顿超过',
                fac.AntdText('debounceWait', strong=True),
                '的时长时，才会触发回调函数。',
            ]
        ),
    },
    {
        'path': 'auto_spin',
        'title': '配合autoSpin实现远程加载',
        'description': fac.AntdParagraph(
            [
                '通过设置',
                fac.AntdText('autoSpin=True', code=True),
                '，在触发耗时较长的回调时，下拉菜单内可以渲染loading效果。可通过设置',
                fac.AntdText('loadingEmptyContent', strong=True),
                '来自定义loading效果的显示内容。',
            ]
        ),
    },
    {
        'path': 'options_share',
        'title': '回调实现多选框选项互斥',
        'description': fac.AntdParagraph(
            [
                '示例：通过回调动态设置',
                fac.AntdText('options', strong=True),
                '实现多个下拉选框中的选项互斥。',
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
