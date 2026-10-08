from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    length,  # noqa: F401
    sizes,  # noqa: F401
    variant,  # noqa: F401
    disabled,  # noqa: F401
    status,  # noqa: F401
    custom_display_character,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdOTP')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('英文输入法下默认接收6位数字或字母输入。'),
        },
        {
            'path': 'length',
            'title': t('输入框数量'),
            'description': t('设置参数`length`控制单体输入框的数量。'),
        },
        {
            'path': 'sizes',
            'title': t('尺寸规格'),
            'description': t('设置参数`size`控制尺寸规格。'),
        },
        {
            'path': 'variant',
            'title': t('形态变体'),
            'description': t('设置参数`variant`控制形态变体风格。'),
        },
        {
            'path': 'disabled',
            'title': t('禁用状态'),
            'description': t('设置参数`disabled`控制是否禁用当前组件。'),
        },
        {
            'path': 'status',
            'title': t('强制渲染校验状态'),
            'description': t('设置参数`status`控制强制校验状态渲染。'),
        },
        {
            'path': 'custom_display_character',
            'title': t('自定义遮罩字符'),
            'description': t('设置参数`mask`自定义遮罩显示字符。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t(
                '**AntdOTP**的属性`value`将在全部输入框均输入完毕的情况下触发更新。'
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
