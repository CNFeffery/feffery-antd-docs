import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    multiple,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    allow_no_value,  # noqa: F401
    custom_style,  # noqa: F401
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
        'path': 'multiple',
        'title': '多选模式',
        'description': None,
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': None,
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': fac.AntdParagraph('只读状态适用于单纯的数据展示场景。'),
    },
    {
        'path': 'allow_no_value',
        'title': '限制必须有选中值',
        'description': fac.AntdParagraph(
            [
                '设置',
                fac.AntdText('allowNoValue=False', code=True),
                '后，将会阻止用户对唯一选中值的取消选择行为',
            ]
        ),
    },
    {
        'path': 'custom_style',
        'title': '自定义选项样式',
        'description': None,
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('通过回调监听已选中卡片对应值。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
