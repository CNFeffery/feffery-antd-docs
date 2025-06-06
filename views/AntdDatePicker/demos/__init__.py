from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    hide_today,  # noqa: F401
    time_default_value,  # noqa: F401
    different_placement,  # noqa: F401
    different_picker,  # noqa: F401
    custom_format,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    prefix,  # noqa: F401
    suffix_icon,  # noqa: F401
    render_status,  # noqa: F401
    picker_value,  # noqa: F401
    disabled_dates,  # noqa: F401
    extra_footer,  # noqa: F401
    custom_cells,  # noqa: F401
    basic_callbacks,  # noqa: F401
    dynamic_disabled_dates,  # noqa: F401
    listen_picker_value,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '最基础的日期选择、日期时间选择。',
    },
    {
        'path': 'hide_today',
        'title': '隐藏今天按钮',
        'description': '隐藏“今天”快捷选择按钮。',
    },
    {
        'path': 'time_default_value',
        'title': '设置自动选定的时间值',
        'description': '由参数`showTime.defaultValue`设定的默认值，将会在用户初次选中日期后，在时间选择面板中被自动选中。',
    },
    {
        'path': 'different_placement',
        'title': '悬浮层展开方位',
        'description': '设置参数`placement`控制悬浮层展开方位。',
    },
    {
        'path': 'different_picker',
        'title': '不同的日期选择粒度',
        'description': '设置参数`picker`选择不同的日期选择粒度。',
    },
    {
        'path': 'custom_format',
        'title': '自定义format',
        'description': '设置参数`format`以实现不同粒度设置下适合的已选内容回填格式化。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`开启禁用状态。',
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': '设置参数`readOnly=True`开启只读状态。',
    },
    {
        'path': 'prefix',
        'title': '内嵌前缀内容',
        'description': '通过参数`prefix`设置选择框内嵌前缀内容。',
    },
    {
        'path': 'suffix_icon',
        'title': '内嵌后缀图标',
        'description': '通过参数`suffixIcon`设置选择框内嵌后缀图标。',
    },
    {
        'path': 'render_status',
        'title': '强制状态渲染',
        'description': '设置参数`status`强制状态渲染。',
    },
    {
        'path': 'picker_value',
        'title': '控制面板停留位置',
        'description': None,
    },
    {
        'path': 'disabled_dates',
        'title': '自定义日期禁用策略',
        'description': '设置参数`disabledDatesStrategy`控制需要禁止用户选中的日期。',
    },
    {
        'path': 'extra_footer',
        'title': '底部添加额外内容',
        'description': '通过参数`extraFooter`自定义选择面板底部额外的内容。',
    },
    {
        'path': 'custom_cells',
        'title': '控制指定日期单元格样式',
        'description': '通过参数`customCells`对指定规则对应的日期单元格添加额外样式，未填写条件的部分将视作通配规则。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
    },
    {
        'path': 'dynamic_disabled_dates',
        'title': '基于回调的动态日期禁用',
        'description': '通过回调函数实现基于当前日期时间的动态禁用策略，以“只允许选择未来7天内日期”为例。',
    },
    {
        'path': 'listen_picker_value',
        'title': '监听面板停留位置',
        'description': '通过回调函数监听`pickerValue`的变化，获取当前面板停留位置。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
