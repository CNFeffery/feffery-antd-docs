import feffery_antd_components as fac
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

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的单条评论信息。'),
    },
    {
        'path': 'custom_avatar',
        'title': '自定义头像',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('avatarProps', code=True),
                '进行头像的自定义配置。',
            ]
        ),
    },
    {
        'path': 'from_now',
        'title': '显示相对发布时间',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('fromNow=True', code=True),
                '后，评论中的发布时间将以相对现在的时间形式进行展示。',
            ]
        ),
    },
    {
        'path': 'nested',
        'title': '嵌套评论',
        'description': fac.AntdParagraph(
            ['评论本身可以作为其他评论的子元素呈现出嵌套效果。']
        ),
    },
    {
        'path': 'initial_status',
        'title': '初始化点赞反对状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('defaultAction', code=True),
                '控制初始化时所处的的点赞反对状态。',
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
