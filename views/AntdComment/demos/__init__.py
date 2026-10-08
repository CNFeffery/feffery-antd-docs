from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_avatar,  # noqa: F401
    from_now,  # noqa: F401
    nested,  # noqa: F401
    initial_status,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdComment')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的单条评论信息。'),
        },
        {
            'path': 'custom_avatar',
            'title': t('自定义头像'),
            'description': t('通过参数`avatarProps`进行头像的自定义配置。'),
        },
        {
            'path': 'from_now',
            'title': t('显示相对发布时间'),
            'description': t(
                '设置参数`fromNow=True`后，评论中的发布时间将以相对现在的时间形式进行展示。'
            ),
        },
        {
            'path': 'nested',
            'title': t('嵌套评论'),
            'description': t(
                '评论本身可以作为其他评论的子元素呈现出嵌套效果。'
            ),
        },
        {
            'path': 'initial_status',
            'title': t('初始化点赞反对状态'),
            'description': t(
                '设置参数`defaultAction`控制初始化时所处的的点赞反对状态。'
            ),
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
