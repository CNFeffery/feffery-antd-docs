from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    quickly_set_options,  # noqa: F401
    vertical,  # noqa: F401
    block,  # noqa: F401
    size,  # noqa: F401
    icon,  # noqa: F401
    only_icon,  # noqa: F401
    custom_render,  # noqa: F401
    disabled,  # noqa: F401
    shape,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdSegmented')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最简单的用法。'),
        },
        {
            'path': 'quickly_set_options',
            'title': t('快捷设置options参数'),
            'description': t('针对`options`参数的快捷设置方式。'),
        },
        {
            'path': 'vertical',
            'title': t('垂直展示'),
            'description': t('设置参数`vertical=True`开启垂直展示模式。'),
        },
        {
            'path': 'block',
            'title': t('撑满父级元素宽度'),
            'description': t(
                '设置参数`block=True`后分段控制器将撑满父元素宽度。'
            ),
        },
        {
            'path': 'size',
            'title': t('不同的尺寸规格'),
            'description': t('通过参数`size`控制分段控制器的尺寸规格。'),
        },
        {
            'path': 'icon',
            'title': t('设置图标'),
            'description': t('为选项添加图标。'),
        },
        {
            'path': 'only_icon',
            'title': t('仅展示图标'),
            'description': t('仅为选项设置图标。'),
        },
        {
            'path': 'custom_render',
            'title': t('自定义渲染'),
            'description': t('选项的`label`参数可传入自定义组件。'),
        },
        {
            'path': 'disabled',
            'title': t('禁用状态'),
            'description': t('设置参数`disabled=True`禁用当前分段控制器。'),
        },
        {
            'path': 'shape',
            'title': t('不同的形状'),
            'description': t('设置参数`shape`渲染不同的形状。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('监听当前所选项的值。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
