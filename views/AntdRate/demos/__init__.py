import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    half_star,  # noqa: F401
    star_tooltips,  # noqa: F401
    read_only_status,  # noqa: F401
    clear,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最简单的单选框。'),
    },
    {
        'path': 'half_star',
        'title': '半星选择',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('allowHalf=True', code=True),
                '支持选择半星。',
            ]
        ),
    },
    {
        'path': 'star_tooltips',
        'title': '文案展现',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tooltips', code=True),
                '给评分组件加上文案展示。',
            ]
        ),
    },
    {
        'path': 'read_only_status',
        'title': '只读状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('defaultValue', code=True),
                '及',
                fac.AntdText('disabled=True', code=True),
                '之后，即等价于只读模式，适合单纯的星级展示。',
            ]
        ),
    },
    {
        'path': 'clear',
        'title': '清除',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('allowClear', code=True),
                '允许或者禁用清除。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('可用于监听评分组件的选择事件。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
