from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    actions,  # noqa: F401
    basic_callbacks,  # noqa: F401
    size,  # noqa: F401
    extra_link,  # noqa: F401
    head_style,  # noqa: F401
    body_style,  # noqa: F401
    card_meta,  # noqa: F401
    card_grid,  # noqa: F401
    basic_usage,  # noqa: F401
    extra,  # noqa: F401
    hoverable,  # noqa: F401
    cover,  # noqa: F401,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdCard')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('基本的使用示例。'),
        },
        {
            'path': 'size',
            'title': t('尺寸规格'),
            'description': t(
                "可设置两种不同大小：`'default'`、`'small'`、`'default'`"
            ),
        },
        {
            'path': 'extra_link',
            'title': t('添加右上角链接'),
            'description': t('可在卡片右上角添加自定义链接。'),
        },
        {
            'path': 'extra',
            'title': t('添加右上角额外内容'),
            'description': t(
                '可在卡片右上角添加自定义组件，优先级比**extraLink**更高，所以设置的**extraLink**将不会生效。'
            ),
        },
        {
            'path': 'hoverable',
            'title': t('悬停效果'),
            'description': t('可设置是否在鼠标悬停时显示特殊样式。'),
        },
        {
            'path': 'head_style',
            'title': t('标题栏CSS样式'),
            'description': t('可设置标题栏的CSS样式。'),
        },
        {
            'path': 'body_style',
            'title': t('内容区CSS样式'),
            'description': t('可设置内容区的CSS样式。'),
        },
        {
            'path': 'cover',
            'title': t('添加封面图片'),
            'description': t('可在卡片的标题栏与内容区之间插入封面图片。'),
        },
        {
            'path': 'card_grid',
            'title': t('卡片网格'),
            'description': t('使用内嵌网格模式来分隔卡片内容。'),
        },
        {
            'path': 'card_meta',
            'title': t('结构化卡片'),
            'description': t(
                '用于为卡片添加结构化信息，如头像、标题、描述等，更灵活地展示卡片内容。'
            ),
        },
        {
            'path': 'actions',
            'title': t('添加底部操作栏'),
            'description': t('可添加底部操作栏，实现更复杂的功能。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('卡片点击回调监听'),
            'description': t('可监听卡片点击事件触发回调。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
