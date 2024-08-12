import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    status,  # noqa: F401
    custom_height,  # noqa: F401
    pagination,  # noqa: F401
    custom_move_button_content,  # noqa: F401
    search,  # noqa: F401
    multiple_mode_search,  # noqa: F401
    custom_titles,  # noqa: F401
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
        'path': 'custom_height',
        'title': '自定义高度',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('height', code=True),
                '自定义控制穿梭框整体高度。',
            ]
        ),
    },
    {
        'path': 'pagination',
        'title': '分页展示',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('pagination', code=True),
                '启用分页功能。',
            ]
        ),
    },
    {
        'path': 'custom_move_button_content',
        'title': '自定义移项按钮内容',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('operations', code=True),
                '自定义移项按钮内容。',
            ]
        ),
    },
    {
        'path': 'search',
        'title': '添加搜索框',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('showSearch=True', code=True),
                '启用选项搜索功能。',
            ]
        ),
    },
    {
        'path': 'multiple_mode_search',
        'title': '多模式搜索',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('optionFilterMode', code=True),
                '启用不同的选项搜索模式。',
            ]
        ),
    },
    {
        'path': 'custom_titles',
        'title': '自定义两侧标题',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('titles', code=True),
                '自定义两侧标题内容。',
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
