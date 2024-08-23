import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    with_more_info,  # noqa: F401
    custom_icon,  # noqa: F401
    percent,  # noqa: F401
    set_current,  # noqa: F401
    vertical,  # noqa: F401
    vertical_info,  # noqa: F401
    dot,  # noqa: F401
    sizes,  # noqa: F401
    current_status,  # noqa: F401
    navigation,  # noqa: F401
    inline,  # noqa: F401
    click_switch,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基础的静态步骤条。'),
    },
    {
        'path': 'with_more_info',
        'title': '带说明信息的步骤条',
        'description': fac.AntdParagraph(
            '步骤条节点可额外设置副标题及描述信息。'
        ),
    },
    {
        'path': 'custom_icon',
        'title': '自定义图标',
        'description': fac.AntdParagraph('步骤图标可传入任意组件型内容。'),
    },
    {
        'path': 'percent',
        'title': '当前步骤环状进度',
        'description': '通过设置参数`percent`控制当前步骤的环状进度显示效果。',
    },
    {
        'path': 'set_current',
        'title': '设置当前所在步骤',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('current', code=True),
                '可控制当前步骤条所在步骤。',
            ]
        ),
    },
    {
        'path': 'vertical',
        'title': '垂直步骤条',
        'description': fac.AntdParagraph('从上往下垂直展示步骤条信息。'),
    },
    {
        'path': 'vertical_info',
        'title': '垂直展示步骤条信息',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('labelPlacement', code=True),
                '可控制步骤条额外信息的展示形式。',
            ]
        ),
    },
    {
        'path': 'dot',
        'title': '点状步骤条',
        'description': fac.AntdParagraph('简洁风格的点状步骤条。'),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph('不同尺寸的步骤条。'),
    },
    {
        'path': 'current_status',
        'title': '控制当前步骤状态',
        'description': None,
    },
    {
        'path': 'navigation',
        'title': '导航风格步骤条',
        'description': None,
    },
    {
        'path': 'inline',
        'title': '内联风格步骤条',
        'description': None,
    },
    {
        'path': 'click_switch',
        'title': '允许点击切换步骤',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('allowClick=True', code=True),
                '后可直接点击步骤进行步骤切换。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            ['通过回调函数监听并控制步骤条功能。']
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
