import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    different_placement,  # noqa: F401
    expand_trigger,  # noqa: F401
    flat_options_mode,  # noqa: F401
    multiple_mode,  # noqa: F401
    change_on_select,  # noqa: F401
    disabled_status,  # noqa: F401
    show_checked_strategy,  # noqa: F401
    read_only_status,  # noqa: F401
    render_status,  # noqa: F401
    options_node_to_label,  # noqa: F401
    search_keyword,  # noqa: F401
    panel_mode,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('默认参数下，'),
                fac.AntdText('AntdCascader', strong=True),
                fac.AntdText('以单选的模式，供用户进行末端叶节点的选择'),
            ]
        ),
    },
    {
        'path': 'different_placement',
        'title': '悬浮层展开方位',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('placement', code=True),
                '控制悬浮层展开方位。',
            ]
        ),
    },
    {
        'path': 'expand_trigger',
        'title': '移入展开',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText("expandTrigger='hover'", code=True),
                '鼠标悬停触发子选项展开。',
            ]
        ),
    },
    {
        'path': 'multiple_mode',
        'title': '多选模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('multiple=True', code=True),
                '开启多选模式。',
            ]
        ),
    },
    {
        'path': 'change_on_select',
        'title': '选择非末端节点',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('changeOnSelect=True', code=True),
                '后当任意节点被选择时均对value进行更新。',
            ]
        ),
    },
    {
        'path': 'flat_options_mode',
        'title': '扁平options模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText("optionsMode='flat'", code=True),
                '开启扁平options模式。',
            ]
        ),
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled=True', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'show_checked_strategy',
        'title': '已选项回填策略',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('showCheckedStrategy', code=True),
                '控制已选项回填策略。',
            ]
        ),
    },
    {
        'path': 'read_only_status',
        'title': '只读状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('readOnly=True', code=True),
                '开启只读状态。',
            ]
        ),
    },
    {
        'path': 'render_status',
        'title': '强制状态渲染',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('status', code=True),
                '强制状态渲染。',
            ]
        ),
    },
    {
        'path': 'options_node_to_label',
        'title': '自定义选项label',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('optionsNodeKeyToLabel', code=True),
                '，针对级联结构中的指定节点，定义作为标题的组件型内容。',
            ]
        ),
    },
    {
        'path': 'search_keyword',
        'title': '关键词搜索',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('optionFilterProp', code=True),
                '指定选项关键词搜索时的目标字段。',
            ]
        ),
    },
    {
        'path': 'panel_mode',
        'title': '面板模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('panelMode=True', code=True),
                '开启面板模式，适用于一些需要内嵌适用的场景。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('用于监听级联选择的选择事件。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
