import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    status,  # noqa: F401
    different_placement,  # noqa: F401
    multiple,  # noqa: F401
    # max_tag_placeholder,  # noqa: F401
    # max_tag_text_length,  # noqa: F401
    # suffix_icon,  # noqa: F401
    # switcher_icon,  # noqa: F401
    multiple_checkable,  # noqa: F401
    flat_tree_data,  # noqa: F401
    tree_line,  # noqa: F401
    tree_check_strictly,  # noqa: F401
    show_checked_strategy,  # noqa: F401
    multiple_mode_search,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': None,
    },
    {
        'path': 'disabled',
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
        'path': 'read_only',
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
        'path': 'status',
        'title': '强制状态渲染',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('status', code=True),
                '进行强制状态渲染。',
            ]
        ),
    },
    {
        'path': 'different_placement',
        'title': '不同的悬浮层展开方位',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('placement', code=True),
                '控制悬浮层展开方位。',
            ]
        ),
    },
    {
        'path': 'multiple',
        'title': '多选模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('multiple=True', code=True),
                '开启多选模式。',
            ]
        ),
    },
    # {
    #     'path': 'max_tag_placeholder',
    #     'title': '隐藏已选值时显示内容',
    #     'description': fac.AntdParagraph(
    #         [
    #             '多选模式下，设置参数',
    #             fac.AntdText('maxTagPlaceholder', code=True),
    #             '控制隐藏已选值tag时显示的内容。',
    #         ]
    #     ),
    # },
    # {
    #     'path': 'max_tag_text_length',
    #     'title': '已选值最大显示文本长度',
    #     'description': fac.AntdParagraph(
    #         [
    #             '多选模式下，设置参数',
    #             fac.AntdText('maxTagTextLength', code=True),
    #             '控制最大显示的已选值tag文本长度。',
    #         ]
    #     ),
    # },
    # {
    #     'path': 'suffix_icon',
    #     'title': '自定义选择框后缀图标',
    #     'description': fac.AntdParagraph(
    #         [
    #             '设置参数',
    #             fac.AntdText('suffixIcon', code=True),
    #             '自定义选择框后缀图标。',
    #         ]
    #     ),
    # },
    # {
    #     'path': 'switcher_icon',
    #     'title': '自定义树节点的展开/折叠图标',
    #     'description': fac.AntdParagraph(
    #         [
    #             '设置参数',
    #             fac.AntdText('switcherIcon', code=True),
    #             '自定义树节点的展开/折叠图标。',
    #         ]
    #     ),
    # },
    {
        'path': 'multiple_checkable',
        'title': '带勾选框的多选模式',
        'description': fac.AntdParagraph(
            [
                '多选模式下设置参数',
                fac.AntdText('treeCheckable=True', code=True),
                '为节点添加勾选框。',
            ]
        ),
    },
    {
        'path': 'flat_tree_data',
        'title': '扁平treeData模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeDataMode="flat"', code=True),
                '后可传入扁平结构',
                fac.AntdText('treeData', code=True),
                '进行树结构定义。',
            ]
        ),
    },
    {
        'path': 'tree_line',
        'title': '添加连接线',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeLine=True', code=True),
                '开启连接线。',
            ]
        ),
    },
    {
        'path': 'tree_check_strictly',
        'title': '父子节点独立选择',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeCheckStrictly=True', code=True),
                '后父子节点选择行为彼此独立。',
            ]
        ),
    },
    {
        'path': 'show_checked_strategy',
        'title': '已选项回填显示策略',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('showCheckedStrategy', code=True),
                '控制已选项回填显示策略。',
            ]
        ),
    },
    {
        'path': 'multiple_mode_search',
        'title': '多模式搜索',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('treeNodeFilterMode', code=True),
                '控制搜索模式。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
