from functools import partial
from i18n import translator
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


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdTransfer')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': None,
        },
        {
            'path': 'disabled',
            'title': t('禁用状态'),
            'description': t('设置参数`disabled=True`开启禁用状态。'),
        },
        {
            'path': 'read_only',
            'title': t('只读状态'),
            'description': t('设置参数`readOnly=True`开启只读状态。'),
        },
        {
            'path': 'status',
            'title': t('强制状态渲染'),
            'description': t('设置参数`status`进行强制状态渲染。'),
        },
        {
            'path': 'custom_height',
            'title': t('自定义高度'),
            'description': t('设置参数`height`自定义控制穿梭框整体高度。'),
        },
        {
            'path': 'pagination',
            'title': t('分页展示'),
            'description': t('设置参数`pagination`启用分页功能。'),
        },
        {
            'path': 'custom_move_button_content',
            'title': t('自定义移项按钮内容'),
            'description': t('设置参数`operations`自定义移项按钮内容。'),
        },
        {
            'path': 'search',
            'title': t('添加搜索框'),
            'description': t('设置参数`showSearch=True`启用选项搜索功能。'),
        },
        {
            'path': 'multiple_mode_search',
            'title': t('多模式搜索'),
            'description': t(
                '设置参数`optionFilterMode`启用不同的选项搜索模式。'
            ),
        },
        {
            'path': 'custom_titles',
            'title': t('自定义两侧标题'),
            'description': t('设置参数`titles`自定义两侧标题内容。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
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
